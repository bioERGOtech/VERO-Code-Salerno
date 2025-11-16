# Phase 2: Statistical Risk Analysis and RI Significance Modelling

## 1. Overview
This phase focused on identifying and ranking clinical predictors of oncological risk among geriatric patients.  
The key objectives were to:

- Develop and evaluate **multivariable survival models** (Cox PH and Weibull AFT).  
- Analyze **binary outcomes**, including *Severe Adverse Drug Reactions (Severe_ADRs)*, *Readmission*, and *Frailty Category*.  
- Construct a **Relative Importance (RI) Significance Table** integrating effect sizes, model stability, and predictive consistency.

Phase 2 builds upon the **data cleaning and preprocessing** tasks completed in Phase 1.

---

## 2. Computation of Outcome Variables
Multiple clinical outcomes were derived and standardized for analysis:

- **Overall_Survival** – calculated from `observation_start_date` to either `death_date` or censoring (`observation_end_date`).  
- **Survival_days** – duration in days.  
- **Frailty_Category** – recoded binary variable (Low vs. High Frailty).  
- **Severe_ADRs** – binary variable indicating grade ≥3 adverse reactions.  
- **Readmission_flag** – binary flag for hospital readmission during follow-up.  

All variables underwent consistency checks, missing data imputation, and categorical validation.

---

## 3. Univariate Screening
Each variable was initially screened to determine its individual relationship with each outcome.  
Appropriate tests were applied based on data type (log-rank, logistic, or non-parametric).  
Predictors meeting significance thresholds (p < 0.05 and meaningful effect size) were retained.

**Key Deliverables:**
- `univariate_screening_results_with_effects.xlsx`  
- `univariate_effectsize_heatmap.png`  
- Volcano and Top-15 plots for each outcome:
  - `univariate_top15_[Outcome].png`
  - `univariate_volcano_[Outcome].png`

---

## 4. Cox Proportional Hazards Model
A **Cox PH model** was fitted using `survival_days` and `Overall_Survival` as the event-time variables.

**Preprocessing Steps:**
- Categorical encoding (dummy variables).  
- Standardization of continuous features.  
- Removal of multicollinear or constant variables.  

**Key Metrics:**

| Metric | Value |
|:--|:--|
| Observations | 172 |
| Events | 30 |
| Concordance Index (C-index) | **0.96** |
| Log-likelihood Ratio Test | χ² = 129.08, p < 0.001 |

**Top Predictors:**
- Alcohol consumption (High)  
- Tumor stage (II–III)  
- Histological grade (G2–G3)  
- End-of-study period status  

**Outputs:**
- `coxph_model_summary_screened_converted_clean.xlsx`  
- `coxph_hazard_ratros_screened_converted_clean.png`

---

## 5. Weibull Accelerated Failure Time (AFT) Model
A **Weibull AFT** model was developed to complement the Cox PH model.  
It estimated *time ratios*, quantifying the acceleration or deceleration of survival times.

**Data Preparation:**
- One-hot encoding for categorical predictors.  
- Removal of missing or uniform columns.  
- Validation of survival time integrity.

**Outputs:**
- `weibull_aft_coefficients_screened_clean.png`  
- AFT summary tables with coefficients and time ratios.  

Both survival models identified **tumor stage, histological grade, and alcohol use** as strong and consistent risk factors.

---

## 6. Binary Outcome Models
Separate **Elastic Net Logistic Regression** models were fitted for:
- Severe_ADRs  
- Readmission_flag  
- Frailty_Category  

Each model used:
- Standardized numeric predictors  
- 10-fold cross-validation for α/λ optimization  
- ROC-AUC and F1-score for evaluation  

**Outputs:**
- Saved in `/binary_models_outputs/`  
- Performance plots and coefficient summaries.

---

## 7. RI (Relative Importance) Significance Analysis
The **RI Significance Table** combined the outputs from all models to rank features by their:
- **Effect Size** (Hazard/Odds/Time Ratios)  
- **Stability** (Bootstrap Coefficient Variance)  
- **Predictive Strength** (C-index or ROC-AUC weight)

**High-importance Predictors:**
- Alcohol consumption (High)  
- Observation end reasons (Study Period, Follow-Up)  
- Tumor stage (II–III)  
- Histological grade (G2–G3)  
- Death during observation  

**Deliverables:**
- `RI_Significance_Table.xlsx`  
- `RI_Significance_Table_robust.xlsx`  
- `RI_Significance_Top15_robust.png`  
- `RI_Significance_Table_TopPredictors.png`

---

## 8. Validation and Diagnostics
Validation steps ensured model reliability:

- **Schoenfeld Residual Tests:** No global PH assumption violations detected.  
- **Bootstrap Resampling (n=100):** Confirmed coefficient stability.  
- **Cross-validation:** Demonstrated consistent predictive performance.

---

## 9. Deliverables Summary

| Type | Folder / File | Description |
|------|---------------|-------------|
| **Models & Tables** | `phase-2/results/tables/` | Model summaries, effect sizes, RI tables |
| **Figures** | `phase-2/results/figures/` | Visual outputs (volcano, top predictors, heatmaps) |
| **Artifacts** | `phase-2/artifacts/` | Raw outputs for reproducibility |
| **Notebook** | `phase-2/notebooks/phase2_modeling_and_RI.ipynb` | Full analysis workflow |
| **Report** | `phase-2/README.md` | Summary of methodology and findings |

---

## 10. Key Takeaways
- Integrated modeling provides a comprehensive multi-outcome view of oncological risk.  
- **Alcohol consumption** and **tumor stage** are robust predictors across outcomes.  
- Strong agreement between Cox and Weibull models confirms result stability.  
- The **RI Significance Table** is a central interpretive tool, summarizing risk relevance across all models.  

### Next Phase
Phase 3 will extend these findings by incorporating **machine learning risk scoring** (e.g., SHAP, XGBoost) and **explainability** tools to enhance interpretability.
