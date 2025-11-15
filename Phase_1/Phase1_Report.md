# VERO – Phase 1 Report
## Data Profiling, Cleaning, and Standardization

### Objective
Prepare a clinically consistent, analysis ready baseline dataset for the VERO Oncological Risk Age Assessment.

### Methods 
1) Profiling: completeness, consistency, types. Outputs: Profiling_Master_Report.xlsx, Type+Missingness.xlsx.
2) Cleaning & Standardization: vocab harmonization, derived variables (BMI, NLR, eGFR), date alignment. Output: VERO_Phase1_Clean_Final.csv.
3) Imputation: MICE and Bayesian regression (+ flags). Outputs: VERO_MICE_Imputed.csv, VERO_Bayesian_Imputed.csv.
4) Unit Standardization to mg: conversion map + mg/m2 via BSA, mg/kg via weight, UI flagged. Outputs: VERO_Phase1_Dose_Standardized.csv, VERO_Dose_Standardization_Log.xlsx.
5) Range Extraction: numeric range parsing, removal of gender tags. Outputs: VERO_Phase1_Clean_Ranges.csv, VERO_Range_Extraction_Report.xlsx.
6) Visuals: before/after plots for numeric and categorical distributions. Outputs: /outputs/visuals/vero_plots/*.png.

### Acceptance
- Missingness reduced where appropriate; categorical “Unknown/Non noto” strategy applied.
- Units harmonized where deterministically convertible; UI/mL flagged.
- Negative imputation artifacts corrected via column-wise medians for dose columns.
- Reproducible notebooks with clear IO paths.

### Next steps
- Finalize feature set for modeling (Phase 2).
- Train/validate risk models; calibration and sensitivity analyses.
