#!/usr/bin/env python3
"""
Scrape wiki.gg sites for LLM training corpus.
Handles rate limiting, retries, and saves in multiple formats.
"""

import argparse
import json
import time
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse, parse_qs
import requests
from bs4 import BeautifulSoup

try:
    import html2text
    HAS_HTML2TEXT = True
except ImportError:
    HAS_HTML2TEXT = False
    print("Warning: html2text not installed. Use: uv add html2text")


class WikiScraper:
    def __init__(self, base_url, out_dir, namespaces, rate_limit, user_agent):
        self.base_url = base_url.rstrip('/')
        self.out_dir = Path(out_dir)
        self.namespaces = namespaces
        self.rate_limit = rate_limit
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': user_agent})
        
        # Create output directories
        self.out_dir.mkdir(parents=True, exist_ok=True)
        (self.out_dir / 'html').mkdir(exist_ok=True)
        (self.out_dir / 'markdown').mkdir(exist_ok=True)
        (self.out_dir / 'metadata').mkdir(exist_ok=True)
        
        # Track progress
        self.progress_file = self.out_dir / 'progress.json'
        self.scraped_pages = self.load_progress()
        
        # Setup html2text converter
        if HAS_HTML2TEXT:
            self.h2t = html2text.HTML2Text()
            self.h2t.ignore_links = False
            self.h2t.ignore_images = True
            self.h2t.body_width = 0  # No wrapping
    
    def load_progress(self):
        """Load previously scraped pages to allow resume."""
        if self.progress_file.exists():
            with open(self.progress_file) as f:
                return set(json.load(f))
        return set()
    
    def save_progress(self):
        """Save progress after each page."""
        with open(self.progress_file, 'w') as f:
            json.dump(list(self.scraped_pages), f)
    
    def get_all_pages(self):
        """Get list of all pages using MediaWiki API."""
        pages = []
        for ns in self.namespaces:
            print(f"Fetching page list for namespace {ns}...")
            continue_token = None
            
            while True:
                params = {
                    'action': 'query',
                    'list': 'allpages',
                    'apnamespace': ns,
                    'aplimit': 500,
                    'format': 'json'
                }
                if continue_token:
                    params['apcontinue'] = continue_token
                
                try:
                    resp = self.session.get(f"{self.base_url}/api.php", params=params)
                    resp.raise_for_status()
                    data = resp.json()
                    
                    if 'query' in data and 'allpages' in data['query']:
                        batch = data['query']['allpages']
                        pages.extend(batch)
                        print(f"  Found {len(batch)} pages (total: {len(pages)})")
                    
                    # Check for continuation
                    if 'continue' in data and 'apcontinue' in data['continue']:
                        continue_token = data['continue']['apcontinue']
                        time.sleep(self.rate_limit)
                    else:
                        break
                        
                except Exception as e:
                    print(f"Error fetching page list: {e}")
                    break
            
            time.sleep(self.rate_limit)
        
        return pages
    
    def sanitize_filename(self, title):
        """Convert page title to safe filename."""
        # Replace problematic characters
        safe = re.sub(r'[<>:"/\\|?*]', '_', title)
        # Limit length
        if len(safe) > 200:
            safe = safe[:200]
        return safe
    
    def scrape_page(self, page_title, page_id):
        """Scrape a single page and save in multiple formats."""
        if page_title in self.scraped_pages:
            print(f"  Skipping (already scraped): {page_title}")
            return True
        
        try:
            # Get page content via API
            params = {
                'action': 'parse',
                'page': page_title,
                'prop': 'text|categories|links|sections',
                'format': 'json'
            }
            
            resp = self.session.get(f"{self.base_url}/api.php", params=params, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            
            if 'error' in data:
                print(f"  Error: {data['error'].get('info', 'Unknown error')}")
                return False
            
            if 'parse' not in data:
                print(f"  No content found")
                return False
            
            parse_data = data['parse']
            html_content = parse_data.get('text', {}).get('*', '')
            
            # Clean up HTML
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Remove edit sections
            for edit_section in soup.find_all('span', class_='mw-editsection'):
                edit_section.decompose()
            
            safe_filename = self.sanitize_filename(page_title)
            
            # Save HTML
            html_path = self.out_dir / 'html' / f"{safe_filename}.html"
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(soup.prettify())
            
            # Save Markdown
            if HAS_HTML2TEXT:
                markdown = self.h2t.handle(str(soup))
                md_path = self.out_dir / 'markdown' / f"{safe_filename}.md"
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(f"# {page_title}\n\n")
                    f.write(markdown)
            
            # Save metadata
            metadata = {
                'title': page_title,
                'pageid': page_id,
                'categories': [c['*'] for c in parse_data.get('categories', [])],
                'sections': [s['line'] for s in parse_data.get('sections', [])],
                'url': f"{self.base_url}/wiki/{page_title.replace(' ', '_')}"
            }
            meta_path = self.out_dir / 'metadata' / f"{safe_filename}.json"
            with open(meta_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2)
            
            # Mark as complete
            self.scraped_pages.add(page_title)
            self.save_progress()
            
            return True
            
        except Exception as e:
            print(f"  Exception: {e}")
            return False
    
    def scrape(self):
        """Main scraping loop."""
        print(f"Scraping wiki: {self.base_url}")
        print(f"Output directory: {self.out_dir}")
        print(f"Namespaces: {self.namespaces}")
        print(f"Rate limit: {self.rate_limit}s between requests\n")
        
        # Get all pages
        pages = self.get_all_pages()
        print(f"\nTotal pages to scrape: {len(pages)}")
        print(f"Already scraped: {len(self.scraped_pages)}")
        print(f"Remaining: {len(pages) - len(self.scraped_pages)}\n")
        
        # Scrape each page
        success_count = 0
        for i, page in enumerate(pages, 1):
            title = page['title']
            page_id = page['pageid']
            
            print(f"[{i}/{len(pages)}] {title}")
            
            if self.scrape_page(title, page_id):
                success_count += 1
            
            # Rate limiting
            if i < len(pages):
                time.sleep(self.rate_limit)
        
        print(f"\n✓ Scraping complete!")
        print(f"  Successfully scraped: {success_count} pages")
        print(f"  Output directory: {self.out_dir}")


def main():
    parser = argparse.ArgumentParser(
        description='Scrape wiki.gg sites for LLM corpus building'
    )
    parser.add_argument(
        '--base-url',
        required=True,
        help='Base URL of the wiki (e.g., https://satisfactory.wiki.gg)'
    )
    parser.add_argument(
        '--out-dir',
        default='data',
        help='Output directory for scraped content (default: data)'
    )
    parser.add_argument(
        '--namespaces',
        type=int,
        nargs='+',
        default=[0, 14, 10, 12],
        help='MediaWiki namespaces to scrape (default: 0 14 10 12 = main/category/template/help)'
    )
    parser.add_argument(
        '--rate',
        type=float,
        default=1.0,
        help='Seconds between requests (default: 1.0)'
    )
    parser.add_argument(
        '--user-agent',
        default='WikiScraper/1.0 (Educational/Research)',
        help='User agent string'
    )
    
    args = parser.parse_args()
    
    scraper = WikiScraper(
        base_url=args.base_url,
        out_dir=args.out_dir,
        namespaces=args.namespaces,
        rate_limit=args.rate,
        user_agent=args.user_agent
    )
    
    scraper.scrape()


if __name__ == '__main__':
    main()