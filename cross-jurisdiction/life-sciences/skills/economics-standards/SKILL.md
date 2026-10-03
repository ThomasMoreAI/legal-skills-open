---
name: economics-standards
title: Economics Research Standards
description: Standards and conventions for economics research — econometrics, applied economics, finance, development economics
author: sencersoylu
author_url: https://github.com/sencersoylu/scholar-flow/tree/main/skills/discipline/economics-standards
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: life-sciences
language: en
---

# Economics Research Standards

Comprehensive standards for economics research covering methodology, econometric reporting, causal inference, data practices, and publication conventions across microeconomics, macroeconomics, econometrics, finance, development economics, behavioral economics, and health economics.

## When to Use

- When conducting empirical economics research (micro, macro, applied)
- When specifying and estimating econometric models
- When designing causal identification strategies
- When preparing regression tables and results for publication
- When writing or reviewing NBER working papers
- When submitting to AEA journals (AER, AEJ, JEP, JEL)
- When working with panel data, time series, or cross-sectional datasets
- When pre-registering randomized controlled trials or field experiments
- When preparing replication packages for journal submission

---

## Protocol

### 1. Research Standards

#### 1.1 Citation and Style

1. **Chicago Manual of Style (Author-Date)** -- the dominant citation style in economics
   - In-text: (Acemoglu & Robinson, 2012)
   - Bibliography: Acemoglu, Daron, and James A. Robinson. 2012. *Why Nations Fail*. New York: Crown.
2. **Journal-specific styles** -- always check the target journal's style guide; AER, QJE, Econometrica, and JPE each have minor variations
3. **BibTeX** -- use `@article`, `@book`, `@techreport` (for working papers), and `@incollection` (for handbook chapters); maintain a clean `.bib` file
4. **Working paper convention** -- cite as "(Author, Year)" with the working paper number; update citations to published versions before final submission

#### 1.2 NBER Working Paper Conventions

1. Include NBER working paper number prominently
2. Add the JEL classification codes (e.g., C23, D72, O15)
3. Include a structured abstract (250 words or fewer for most journals)
4. Acknowledge funding sources, data providers, and seminar participants
5. Standard disclaimer: "The views expressed herein are those of the authors and do not necessarily reflect the views of the National Bureau of Economic Research."

#### 1.3 AEA (American Economic Association) Guidelines

1. **Data and Code Availability Policy** -- mandatory for all AEA journals since 2019
   - Submit a complete replication package to the AEA Data and Code Repository (openICPSR)
   - Include all code, data (or instructions to obtain restricted data), and a README
   - README must follow the AEA template (see references)
2. **Pre-registration** -- encouraged for experimental and quasi-experimental work
   - AEA RCT Registry (https://www.socialscienceregistry.org/) for RCTs
   - EGAP registry or OSF for observational studies
   - Pre-analysis plans should specify primary outcomes, sample, and estimation strategy
3. **Disclosure policy** -- authors must disclose funding sources, relevant financial relationships, and IRB approvals
4. **Data availability statements** -- mandatory for top journals; specify whether data are public, restricted, proprietary, or confidential

#### 1.4 Manuscript Structure (Empirical Papers)

Standard ordering for an empirical economics paper:
1. Introduction (motivation, contribution, preview of results)
2. Background / Institutional Context
3. Data (sources, construction, summary statistics)
4. Empirical Strategy / Identification
5. Results (main estimates, interpretation)
6. Robustness Checks and Extensions
7. Conclusion
8. References
9. Appendix (additional tables, proofs, data details)

### 2. Methodology Conventions

#### 2.1 Causal Identification Strategies

The credibility revolution in economics demands explicit identification of causal effects. Common strategies:

| Strategy | Key Assumption | Diagnostic Tests |
|----------|---------------|-----------------|
| **Instrumental Variables (IV)** | Exclusion restriction; relevance | First-stage F-statistic (F > 10); overidentification tests (Hansen J) |
| **Regression Discontinuity (RDD)** | Continuity of potential outcomes at cutoff | McCrary density test; covariate balance at cutoff; bandwidth sensitivity |
| **Difference-in-Differences (DiD)** | Parallel trends in absence of treatment | Pre-treatment trend plots; event study coefficients; placebo tests |
| **Synthetic Control** | Pre-treatment fit quality | RMSPE ratios; placebo tests (in-space, in-time) |
| **Natural Experiments** | As-if random assignment | Balance tests; institutional narrative |
| **Propensity Score Methods** | Conditional independence (selection on observables) | Covariate balance after matching; sensitivity analysis (Rosenbaum bounds) |

#### 2.2 Panel Data Methods

1. **Fixed Effects (FE)** -- absorbs time-invariant unobserved heterogeneity
   - Use entity and/or time fixed effects
   - Cluster standard errors at the entity level (or the level of treatment variation)
   - Report within R-squared
2. **Random Effects (RE)** -- assumes unobserved effects are uncorrelated with regressors
   - More efficient than FE when the assumption holds
   - **Hausman test** -- compare FE and RE estimates; reject RE if they differ systematically
3. **Correlated Random Effects (CRE / Mundlak)** -- include group means of time-varying regressors to relax the RE assumption
4. **Two-way fixed effects (TWFE)** -- caution with staggered treatment timing; use modern DiD estimators (Callaway & Sant'Anna 2021; Sun & Abraham 2021; de Chaisemartin & d'Haultfoeuille 2020)
5. **Dynamic panels** -- Arellano-Bond / Blundell-Bond GMM for short T, large N panels with lagged dependent variables

#### 2.3 Time Series Methods

1. **Stationarity** -- test with Augmented Dickey-Fuller (ADF), Phillips-Perron, or KPSS tests before modeling
2. **Cointegration** -- Engle-Granger two-step or Johansen test for long-run relationships among I(1) variables
3. **VAR/VECM** -- Vector Autoregression for reduced-form dynamics; Vector Error Correction Model when cointegration is present
   - Report impulse response functions (IRFs) with confidence bands
   - Granger causality tests for directional relationships
4. **Structural VARs (SVARs)** -- impose identification restrictions (Cholesky, sign restrictions, narrative identification)
5. **ARCH/GARCH** -- for modeling volatility clustering in financial time series
6. **Local projections (Jorda, 2005)** -- flexible alternative to VAR-based IRFs; robust to misspecification

#### 2.4 Structural vs. Reduced-Form

- **Reduced-form** -- estimates causal effects without specifying a full economic model; transparent, easy to interpret, but limited in counterfactual analysis
- **Structural estimation** -- specifies and estimates an economic model (utility functions, production functions, equilibrium conditions); allows counterfactual simulations but depends on model assumptions
- Many papers now combine both: reduced-form evidence for causal effects + structural model for welfare/counterfactual analysis
- When using structural models, clearly state all assumptions, the estimation method (MLE, GMM, simulated method of moments), and provide model fit diagnostics

#### 2.5 Experimental and Quasi-Experimental Designs

1. **Randomized Controlled Trials (RCTs)**
   - Pre-register on the AEA RCT Registry
   - Report CONSORT-style flow diagrams
   - Analyze by intention-to-treat (ITT) as the primary specification
   - Report treatment-on-the-treated (TOT/LATE) using random assignment as an instrument for take-up
   - Account for multiple hypothesis testing (Bonferroni, Benjamini-Hochberg, or Westfall-Young)
2. **Regression Discontinuity Design (RDD)**
   - Plot the raw data around the discontinuity
   - Use local polynomial regression (triangular kernel preferred)
   - Report estimates across multiple bandwidths (optimal bandwidth via Calonico, Cattaneo, & Titiunik 2014)
   - Run McCrary (2008) density test to check for manipulation
   - Test for covariate smoothness at the cutoff
3. **Difference-in-Differences (DiD)**
   - Plot pre-treatment trends for treatment and control groups
   - Include event study specification with leads and lags
   - Test for pre-trends (joint significance of pre-treatment coefficients)
   - For staggered adoption: use Callaway-Sant'Anna, Sun-Abraham, or Borusyak-Jaravel-Spiess estimators

### 3. Econometric Reporting

#### 3.1 Regression Tables

Economics has highly specific conventions for presenting regression results:

1. **Standard errors in parentheses** below the coefficient estimate -- never report t-statistics in parentheses (some journals accept brackets for t-statistics; always clarify in a table note)
2. **Significance stars** -- use the standard notation:
   - \* p < 0.10
   - \*\* p < 0.05
   - \*\*\* p < 0.01
   - Include a note at the bottom of every table: "Standard errors in parentheses. \* p < 0.10, \*\* p < 0.05, \*\*\* p < 0.01."
3. **Multiple specifications** -- present results across columns, progressively adding controls:
   - Column (1): Bivariate regression
   - Column (2): Add demographic controls
   - Column (3): Add fixed effects
   - Column (4): Preferred specification
   - Column (5): Robustness (alternative sample, specification, or estimator)
4. **Bottom-panel statistics** -- report at the bottom of each table:
   - Number of observations (N)
   - R-squared (or adjusted R-squared, or within R-squared for FE)
   - Fixed effects included (entity, time, entity x time)
   - Clustering level for standard errors
   - First-stage F-statistic (for IV regressions)
   - Dependent variable mean (useful for interpreting effect sizes)
5. **Formatting**
   - Use `stargazer` (R), `esttab`/`estout` (Stata), or `fixest::etable` (R) for consistent table generation
   - Align decimal points across columns
   - Use consistent number of decimal places (typically 3 for coefficients, 3 for standard errors)
   - Label variables with readable names, not variable codes

#### 3.2 Example Table Format

```
Table 3: Effect of Minimum Wage on Employment

                           (1)        (2)        (3)        (4)
                          OLS        OLS        FE         IV

Log(minimum wage)       -0.152**   -0.134**   -0.098*    -0.215**
                        (0.061)    (0.058)    (0.052)    (0.089)

Controls                  No        Yes        Yes        Yes
State fixed effects       No         No        Yes        Yes
Year fixed effects        No         No        Yes        Yes
Observations            1,530      1,530      1,530      1,530
R-squared               0.043      0.127      0.891      0.887
First-stage F                                             23.4
Dependent variable mean  4.82       4.82       4.82       4.82

Notes: Standard errors clustered at the state level in parentheses.
* p < 0.10, ** p < 0.05, *** p < 0.01. The dependent variable is
log(employment). Column (4) instruments for log(minimum wage) using
the interaction of federal minimum wage changes with state-level
exposure.
```

#### 3.3 Robust and Clustered Standard Errors

1. **Always specify the type of standard errors** -- never report uncorrected OLS standard errors without justification
2. **Heteroskedasticity-robust (HC)** -- use HC1 (Stata default) or HC2/HC3 for small samples
3. **Cluster-robust standard errors** -- cluster at the level of treatment variation:
   - State-level policy: cluster at state level
   - Individual-level treatment in a school: cluster at school level
   - Firm-level event: cluster at firm level
4. **Two-way clustering** -- when error correlation occurs along two dimensions (e.g., firm and year), use Cameron, Gelbach, & Miller (2011) two-way clustering
5. **Few clusters problem** -- if fewer than ~40 clusters, standard cluster-robust errors are unreliable:
   - Use wild cluster bootstrap (Cameron, Gelbach, & Miller 2008)
   - Or use the effective number of clusters correction (Imbens & Kolesar 2016)
6. **Conley standard errors** -- for spatial correlation in cross-sectional data

#### 3.4 IV-Specific Reporting

1. **First-stage regression** -- always report; include the first-stage F-statistic
2. **Staiger-Stock rule of thumb** -- F > 10 for a single endogenous regressor; for multiple instruments, use the Stock-Yogo critical values or the effective F-statistic (Olea & Pflueger 2013)
3. **Weak instrument diagnostics** -- report Anderson-Rubin confidence intervals if the instrument is potentially weak
4. **Overidentification test** -- Hansen J test when there are more instruments than endogenous regressors
5. **Reduced-form** -- present the reduced-form (regress outcome on instrument) alongside 2SLS; if the reduced form is not significant, the IV result is suspect
6. **Report both OLS and IV** -- compare to assess the direction and magnitude of endogeneity bias

### 4. Common Methods

#### 4.1 Core Estimation Methods

| Method | When to Use | Key Assumptions | Software |
|--------|-------------|-----------------|----------|
| **OLS** | Linear relationships, exogenous regressors | E[u\|X] = 0, homoskedasticity (or use robust SEs) | Stata: `reg`; R: `lm()`, `fixest::feols()` |
| **2SLS / IV** | Endogenous regressor with valid instrument | Relevance, exclusion restriction | Stata: `ivregress 2sls`; R: `ivreg()`, `fixest::feols()` |
| **LIML** | IV with potentially weak instruments | Same as 2SLS but less bias with weak instruments | Stata: `ivregress liml`; R: `ivreg(method="LIML")` |
| **DiD** | Treatment and control groups, pre/post periods | Parallel trends | Stata: `did_multiplegt`, `csdid`; R: `did`, `fixest` |
| **RDD** | Treatment assigned by a running variable cutoff | Continuity at cutoff | Stata: `rdrobust`; R: `rdrobust` |
| **Propensity Score Matching** | Selection on observables | Conditional independence, common support | Stata: `psmatch2`, `teffects`; R: `MatchIt` |
| **Quantile Regression** | Heterogeneous effects across the outcome distribution | Correctly specified conditional quantile | Stata: `qreg`; R: `quantreg` |
| **MLE** | Discrete choice, structural models, censored/truncated data | Correctly specified likelihood | Stata: `ml`; R: `maxLik`, `optim()` |
| **GMM** | Overidentified models, dynamic panels | Moment conditions valid | Stata: `gmm`, `xtabond2`; R: `gmm`, `plm` |
| **Tobit** | Censored dependent variable (e.g., hours worked >= 0) | Normal, homoskedastic errors | Stata: `tobit`; R: `censReg`, `AER::tobit()` |
| **Heckman Selection** | Sample selection bias (observed only if selected) | Exclusion restriction in selection equation | Stata: `heckman`; R: `sampleSelection` |

#### 4.2 Robustness Check Checklist

For any empirical paper, standard robustness checks include:
- [ ] Alternative functional forms (log vs. level, quadratic terms)
- [ ] Alternative control variable sets (add/remove controls)
- [ ] Alternative sample restrictions (trim outliers, exclude subgroups)
- [ ] Alternative standard error specifications (robust, clustered at different levels)
- [ ] Alternative estimators (OLS vs. IV, parametric vs. nonparametric)
- [ ] Placebo tests (fake treatment timing, fake treatment groups)
- [ ] Leave-one-out analysis (drop one state/country/sector at a time)
- [ ] Sensitivity to outliers (winsorize at 1%/99%, Cook's distance)
- [ ] Bounding exercises (Oster 2019 for omitted variable bias; Conley, Hansen, & Rossi 2012 for IV)

### 5. Data Standards

#### 5.1 Reproducibility Requirements

1. **Replication package** -- must include:
   - All code (numbered or clearly ordered scripts)
   - Raw data or clear instructions for obtaining restricted/proprietary data
   - A master script that runs everything from raw data to final tables and figures
   - A README following the AEA template (data sources, computational requirements, instructions)
2. **Software documentation** -- specify exact versions:
   - Stata: version number + all user-written packages with version (`ssc install ...`)
   - R: `sessionInfo()` or `renv` lockfile
   - Python: `requirements.txt` with pinned versions
3. **Runtime estimates** -- state how long the code takes to run and on what hardware
4. **Random seed** -- set and document seeds for any stochastic procedure (bootstrap, simulation, MCMC)

#### 5.2 Code Standards

1. **Stata .do files** -- the traditional workhorse of empirical economics
   - Use `version XX` at the top of the master .do file
   - Use relative file paths from a project root
   - Comment extensively; use section headers
   - Log output: `log using "output/main_results.log", replace`
2. **R scripts** -- increasingly common, especially for visualization and newer econometric methods
   - Use R projects (`.Rproj`) for path management
   - Prefer `fixest` for fixed effects estimation (fast, flexible)
   - Use `modelsummary` or `stargazer` for table generation
3. **Python** -- growing presence for machine learning, NLP in economics, and large-scale data processing
   - Use `linearmodels` for panel data, `statsmodels` for core econometrics
   - Jupyter notebooks for exploration; `.py` scripts for production code
4. **File organization**:
   ```
   project/
   ├── data/
   │   ├── raw/          # Never modify raw data
   │   ├── processed/    # Cleaned and merged datasets
   │   └── README.md     # Data dictionary and sources
   ├── code/
   │   ├── 01_clean.do
   │   ├── 02_merge.do
   │   ├── 03_analysis.do
   │   ├── 04_tables.do
   │   └── 05_figures.do
   ├── output/
   │   ├── tables/
   │   └── figures/
   ├── paper/
   │   └── manuscript.tex
   └── README.md
   ```

#### 5.3 FAIR Data Principles

1. **Findable** -- deposit data in a searchable repository with a DOI (openICPSR, Zenodo, Dataverse)
2. **Accessible** -- use open formats (CSV, Parquet) over proprietary ones (.dta is acceptable in economics but include CSV versions)
3. **Interoperable** -- use standard variable naming conventions; include a codebook
4. **Reusable** -- attach a clear license; document provenance and transformations

#### 5.4 Common Datasets in Economics

| Dataset | Coverage | Access | Common Uses |
|---------|----------|--------|-------------|
| **PSID** (Panel Study of Income Dynamics) | US households, 1968-present | Restricted (free registration) | Income dynamics, intergenerational mobility |
| **CPS** (Current Population Survey) | US labor force, monthly | Public (IPUMS-CPS) | Labor economics, wage analysis |
| **ACS** (American Community Survey) | US demographics, annual | Public (IPUMS-USA) | Regional analysis, immigration, housing |
| **World Bank WDI** | Country-level development indicators | Public | Development economics, cross-country analysis |
| **Penn World Table** | Cross-country GDP, productivity | Public | Growth economics, international comparisons |
| **Compustat / CRSP** | US firm financials / stock returns | Licensed (WRDS) | Corporate finance, asset pricing |
| **NLSY** (National Longitudinal Survey of Youth) | US youth cohorts (1979, 1997) | Public/restricted | Returns to education, labor market outcomes |
| **DHS** (Demographic and Health Surveys) | Developing countries, health + demographics | Public (registration) | Health economics, development |
| **LISS / Understanding Society** | Dutch / UK household panels | Public (registration) | Behavioral economics, labor, health |
| **World Values Survey** | Cross-country attitudes and values | Public | Institutional economics, culture |

### 6. Additional Conventions

#### 6.1 Figures

1. **Publication quality** -- use vector formats (PDF, EPS) for journal submission; minimum 300 DPI for rasters
2. **Binned scatter plots** -- the workhorse visualization in applied micro; use `binscatter` (Stata) or `binsreg` (Stata/R) for proper implementation with controls
3. **Event study plots** -- plot coefficients and 95% confidence intervals relative to treatment timing; normalize the period before treatment to zero
4. **RDD plots** -- show raw data with a fitted polynomial on each side of the cutoff; include the confidence interval
5. **Coefficient plots** -- preferred over tables for presenting many estimates; use `coefplot` (Stata) or `ggplot2::geom_pointrange` (R)
6. **Color and accessibility** -- use colorblind-friendly palettes; ensure figures are legible in grayscale

#### 6.2 JEL Classification Codes

Include 2-3 JEL codes with every paper. Common codes:

- **C** -- Mathematical and Quantitative Methods (C23: Panel Data Models; C26: IV)
- **D** -- Microeconomics (D12: Consumer Economics; D72: Political Processes)
- **E** -- Macroeconomics (E24: Employment; E52: Monetary Policy)
- **F** -- International Economics (F13: Trade Policy; F31: Foreign Exchange)
- **G** -- Financial Economics (G12: Asset Pricing; G21: Banks)
- **H** -- Public Economics (H23: Externalities; H75: State and Local Government)
- **I** -- Health, Education, Welfare (I12: Health Behavior; I26: Returns to Education)
- **J** -- Labor and Demographic Economics (J16: Gender; J31: Wage Level)
- **L** -- Industrial Organization (L11: Market Structure; L86: IT Services)
- **O** -- Economic Development (O15: Human Resources; O33: Technological Change)

#### 6.3 Authorship in Economics

1. **Author order** -- alphabetical ordering is the strong norm in economics (unlike most other social sciences)
   - Exceptions exist for very unequal contributions, but alphabetical is the default expectation
2. **Acknowledgments** -- thank seminar participants, conference discussants, referees, and editors by convention
3. **Working paper circulation** -- it is standard to circulate working papers (NBER, SSRN, CEPR) well before journal publication; most economics papers are cited in working paper form for years

---

## Checklist

### Research Design
- [ ] Identification strategy clearly stated and defended
- [ ] Key assumptions explicitly listed and discussed
- [ ] Threats to identification addressed
- [ ] Pre-registration completed (if experimental or quasi-experimental)
- [ ] IRB approval obtained (if human subjects involved)
- [ ] JEL codes assigned

### Econometric Reporting
- [ ] Standard errors in parentheses below coefficients
- [ ] Type of standard errors specified (robust, clustered, bootstrap)
- [ ] Clustering level matches level of treatment variation
- [ ] Multiple specifications presented (progressively adding controls)
- [ ] Number of observations reported for each specification
- [ ] R-squared (or within R-squared) reported
- [ ] Significance stars with footnote explaining levels
- [ ] Dependent variable mean reported
- [ ] First-stage F-statistic reported (if IV)

### Robustness
- [ ] Placebo tests conducted
- [ ] Alternative samples and specifications tested
- [ ] Sensitivity to outliers assessed
- [ ] Omitted variable bias bounds computed (Oster 2019)
- [ ] Pre-trends tested (if DiD)
- [ ] Bandwidth sensitivity shown (if RDD)
- [ ] Weak instrument diagnostics reported (if IV)

### Data and Reproducibility
- [ ] Replication package prepared (code + data + README)
- [ ] Master script runs from raw data to final output
- [ ] Software versions documented
- [ ] Random seeds set and recorded
- [ ] Data availability statement included
- [ ] Data deposited in a permanent repository with DOI
- [ ] README follows AEA template

### Manuscript
- [ ] Chicago Author-Date citation style used
- [ ] Abstract under 250 words
- [ ] Figures are publication quality (vector format)
- [ ] Tables generated programmatically (not manually typed)
- [ ] All variables defined in text before use in equations
- [ ] Funding and conflicts of interest disclosed

---

## References

### Textbooks and Methodological Guides

- Angrist, Joshua D., and Jorn-Steffen Pischke. 2009. *Mostly Harmless Econometrics: An Empiricist's Companion*. Princeton: Princeton University Press.
- Angrist, Joshua D., and Jorn-Steffen Pischke. 2014. *Mastering 'Metrics: The Path from Cause to Effect*. Princeton: Princeton University Press.
- Wooldridge, Jeffrey M. 2010. *Econometric Analysis of Cross Section and Panel Data*. 2nd ed. Cambridge, MA: MIT Press.
- Cameron, A. Colin, and Pravin K. Trivedi. 2005. *Microeconometrics: Methods and Applications*. New York: Cambridge University Press.
- Greene, William H. 2018. *Econometric Analysis*. 8th ed. New York: Pearson.
- Cunningham, Scott. 2021. *Causal Inference: The Mixtape*. New Haven: Yale University Press. (https://mixtape.scunning.com/)
- Huntington-Klein, Nick. 2022. *The Effect: An Introduction to Research Design and Causality*. Boca Raton: Chapman & Hall/CRC. (https://theeffectbook.net/)
- Stock, James H., and Mark W. Watson. 2020. *Introduction to Econometrics*. 4th ed. New York: Pearson.

### Key Methodology Papers

- Callaway, Brantly, and Pedro H. C. Sant'Anna. 2021. "Difference-in-Differences with Multiple Time Periods." *Journal of Econometrics* 225 (2): 200-230.
- Sun, Liyang, and Sarah Abraham. 2021. "Estimating Dynamic Treatment Effects in Event Studies with Heterogeneous Treatment Effects." *Journal of Econometrics* 225 (2): 175-199.
- Calonico, Sebastian, Matias D. Cattaneo, and Rocio Titiunik. 2014. "Robust Nonparametric Confidence Intervals for Regression-Discontinuity Designs." *Econometrica* 82 (6): 2295-2326.
- Oster, Emily. 2019. "Unobservable Selection and Coefficient Stability: Theory and Evidence." *Journal of Business & Economic Statistics* 37 (2): 187-204.
- Cameron, A. Colin, Jonah B. Gelbach, and Douglas L. Miller. 2008. "Bootstrap-Based Improvements for Inference with Clustered Errors." *Review of Economics and Statistics* 90 (3): 414-427.
- Conley, Timothy G., Christian B. Hansen, and Peter E. Rossi. 2012. "Plausibly Exogenous." *Review of Economics and Statistics* 94 (1): 260-272.
- McCrary, Justin. 2008. "Manipulation of the Running Variable in the Regression Discontinuity Design: A Density Test." *Journal of Econometrics* 142 (2): 698-714.
- Olea, Jose Luis Montiel, and Carolin Pflueger. 2013. "A Robust Test for Weak Instruments." *Journal of Business & Economic Statistics* 31 (3): 358-369.

### Policies and Guidelines

- American Economic Association. "Data and Code Availability Policy." https://www.aeaweb.org/journals/data/data-code-policy
- American Economic Association. "AEA RCT Registry." https://www.socialscienceregistry.org/
- Vilhuber, Lars. 2021. "Reproducibility and Replicability in Economics." *Harvard Data Science Review* 3 (4).
- NBER. "Working Paper Submission Guidelines." https://www.nber.org/papers
