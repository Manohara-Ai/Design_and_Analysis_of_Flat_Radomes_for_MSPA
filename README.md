# Design and Analysis of Flat Radomes for MSPA

This project explores the electromagnetic performance of **flat dielectric radomes** enclosing **Microstrip Patch Antennas (MSPAs)**, using full-wave simulations in ANSYS HFSS. The focus is on understanding how dielectric materials, geometry, and placement influence antenna behavior such as S-parameters, gain, and radiation patterns.

This work was completed as part of **Krittika Summer Projects (KSP) 6.0** by [Krittika: The Astronomy Club of IIT Bombay](https://krittikaiitb.github.io/).  
Read the full report [here](#) *(link will be updated after release)*.

## Table of Contents

- [Overview](#overview)  
- [Repository Structure](#repository-structure)  
- [Usage](#usage)  
- [Contributor](#contributor)

## Overview

The project includes:

- HFSS simulations of MSPAs with and without radomes  
- Parametric sweep over radome-air gap distance  
- Overlay plots of gain, S11, and VSWR for comparison  
- Theoretical background and references on radome behavior  
- A LaTeX report with all analysis and figures

## Repository Structure

```
.
├── Assignments/                    # Misc documents and visual references
│   └── Design_and_Analysis_of_Flat_Radomes_for_MSPA.pdf
├── Plots/                          # All processed data, visualizations, and plotting scripts
│   ├── data/                       # CSV exports from HFSS
│   ├── overlay_results/           # Comparison plots (gain, S11, etc.)
│   ├── patch_antenna_without_radome/
│   └── utils.py                   # Helper for plotting
├── Report/                         # LaTeX source + compiled report
│   ├── chapters/                  # Chapter-wise .tex files
│   ├── figures/                   # All simulation figures
│   ├── bibliography/
│   └── main.tex                   # Main report file
├── Simulations/                   # HFSS simulation files and radome models
│   ├── Patch Antenna.aedt
│   └── Rectangular_Radome/
│       ├── rectangular_radome_extruded.step
│       ├── rectangular_radome.FCStd
│       └── ...
├── Theory/                        # Reference papers
│   └── *.pdf / *.md
└── README.md
```

## Usage

1. **Simulation Files**  
   Open `.aedt` projects using **ANSYS HFSS 2023 R2** or later.

2. **Plots & Data**  
   - Run or modify `Plots/utils.py` to regenerate comparison plots.
   - Data used for plotting is stored in `Plots/data/`.

3. **Report Compilation**  
   Navigate to `Report/` and compile `main.tex` using `pdflatex` + `bibtex` or `latexmk`.

4. **Resources**  
   Additional theory references are in the `Theory/` directory.

**Note:** The simulation files are large and may require appropriate system resources and HFSS licenses to open.

## Contributor

**B M Manohara**  
GitHub: [@Manohara-Ai](https://github.com/Manohara-Ai)
# Design_and_Analysis_of_Flat_Radomes_for_MSPA
