#!/usr/bin/env bash
set -e

BASE=~/smartestfactory/data
mkdir -p "$BASE"/{kinetics,thermo,balances,optimization,process_improvement}

echo "[INFO] Downloading open reference materials to $BASE ..."
cd "$BASE"

# Function to handle downloads robustly
fetch() {
    url="$1"
    out="$2"
    echo "[>] Fetching: $url"
    wget -c \
         --max-redirect=50 \
         --retry-connrefused \
         --waitretry=5 \
         --timeout=60 \
         --tries=5 \
         --no-check-certificate \
         -O "$out" "$url" || echo "[!] Failed: $url"
}

# --- KINETICS / REACTOR ENGINEERING ---
cd kinetics
fetch "https://ocw.mit.edu/courses/chemical-engineering/10-37-chemical-and-biological-reaction-engineering-spring-2007/10-37s07_lec1.pdf" mit_reaction_kinetics_intro.pdf
fetch "https://ocw.mit.edu/courses/chemical-engineering/10-37-chemical-and-biological-reaction-engineering-spring-2007/lecture-notes/MIT10_37S07_lec6.pdf" mit_reactor_design_nonisothermal.pdf
fetch "https://arxiv.org/pdf/2204.02067.pdf" arxiv_microkinetic_modeling_review.pdf
cd ..

# --- THERMODYNAMICS / ENERGY BALANCES ---
cd thermo
fetch "https://ocw.mit.edu/courses/chemical-engineering/10-40-chemical-engineering-thermodynamics-fall-2003/lecture-notes/lec1_intro.pdf" mit_thermo_intro.pdf
fetch "https://ocw.mit.edu/courses/chemical-engineering/10-40-chemical-engineering-thermodynamics-fall-2003/lecture-notes/lec9_energy_balances.pdf" mit_energy_balance_examples.pdf
fetch "https://www.nrel.gov/docs/fy22osti/81567.pdf" nrel_process_energy_efficiency.pdf
cd ..

# --- MATERIAL / MASS BALANCES ---
cd balances
fetch "https://ocw.mit.edu/courses/chemical-engineering/10-10-introduction-to-chemical-engineering-fall-2006/lecture-notes/lec3_massbalance.pdf" mit_mass_balance_examples.pdf
fetch "https://ocw.mit.edu/courses/chemical-engineering/10-10-introduction-to-chemical-engineering-fall-2006/lecture-notes/lec6_energybalance.pdf" mit_energy_balance_examples.pdf
cd ..

# --- OPTIMIZATION / CONTROL / DATA-DRIVEN TECHNIQUES ---
cd optimization
fetch "https://nptel.ac.in/content/storage2/nptel_data3/html/mhrd/ict/text/103106052/lec1.pdf" nptel_process_optimization_intro.pdf
fetch "https://nptel.ac.in/content/storage2/nptel_data3/html/mhrd/ict/text/103106052/lec10.pdf" nptel_nonlinear_optimization.pdf
fetch "https://arxiv.org/pdf/2206.11862.pdf" arxiv_process_optimization_ai_review.pdf
fetch "https://www.energy.gov/sites/default/files/2023-02/AMO-Advanced-Manufacturing-Optimization-Roadmap.pdf" doe_advanced_manufacturing_optimization.pdf
cd ..

# --- PROCESS IMPROVEMENT / INDUSTRIAL OPTIMIZATION ---
cd process_improvement
fetch "https://www.nist.gov/system/files/documents/el/isd/lean-manufacturing-implementation-guide.pdf" nist_lean_manufacturing_guide.pdf
fetch "https://www.epa.gov/sites/default/files/2015-08/documents/lean_and_environment_toolkit.pdf" epa_lean_environment_toolkit.pdf
fetch "https://eippcb.jrc.ec.europa.eu/sites/default/files/2023-01/BREF_LCP_2021.pdf" eu_best_available_techniques_large_combustion.pdf
fetch "https://www.energy.gov/sites/default/files/2020/10/f79/Chemical_Manufacturing_Energy_Intensity_Reduction_Opportunities.pdf" doe_chemical_manufacturing_efficiency.pdf
cd ..

echo "[✓] All downloads complete!"
tree -L 2 "$BASE"
