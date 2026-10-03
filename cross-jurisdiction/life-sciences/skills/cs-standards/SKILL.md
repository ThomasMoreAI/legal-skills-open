---
name: cs-standards
title: Computer Science Research Standards
description: Computer science research standards including algorithm complexity analysis, benchmark standards, and artifact evaluation
author: sencersoylu
author_url: https://github.com/sencersoylu/scholar-flow/tree/main/skills/discipline/cs-standards
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: life-sciences
language: en
---

# Computer Science Research Standards

Comprehensive standards for computer science research covering reproducibility, benchmarking, evaluation methodology, artifact evaluation, ethics, licensing, and authorship.

## When to Use

- When designing experiments for CS or ML research
- When preparing code and data for publication
- When selecting and reporting benchmarks
- When evaluating machine learning models with statistical rigor
- When submitting artifacts for badge review
- When addressing AI ethics and responsible computing
- When choosing a license for research software

---

## Protocol

### 1. Reproducibility

#### 1.1 Code Sharing Requirements

1. **Public repository** -- host code on GitHub, GitLab, or similar platform before submission
2. **Clean codebase** -- remove dead code, add comments, organize into logical modules
3. **Dependency management** -- provide exact dependency versions:
   - Python: `requirements.txt` (pinned versions) or `pyproject.toml` with lock file
   - R: `renv.lock`
   - Julia: `Project.toml` + `Manifest.toml`
4. **Entry point clarity** -- a single command or script to reproduce main results
5. **Version tagging** -- tag the exact code version used in the paper (e.g., `git tag v1.0-paper`)

#### 1.2 Data Sharing

1. **Public datasets** -- use established repositories (Zenodo, Figshare, Dryad, Hugging Face Datasets)
2. **Persistent identifiers** -- obtain a DOI for datasets
3. **Data documentation** -- provide a datasheet or data card describing:
   - Collection methodology
   - Size, format, and structure
   - Preprocessing steps applied
   - Known limitations or biases
   - License and usage terms
4. **Synthetic data** -- if real data cannot be shared, provide synthetic data that reproduces key statistical properties
5. **Versioning** -- use dataset versioning (e.g., DVC, Hugging Face dataset versions)

#### 1.3 Containerization and Environment

1. **Dockerfile** -- provide a Dockerfile that builds the complete environment:
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   COPY . .
   CMD ["python", "run_experiments.py"]
   ```
2. **Docker Compose** -- for multi-service setups (e.g., database + compute)
3. **Singularity/Apptainer** -- for HPC environments where Docker is unavailable
4. **Environment variables** -- document all required environment variables in `.env.example`

#### 1.4 README Standards

Every research repository README must include:
- Paper title, authors, and publication venue
- Abstract or one-paragraph summary
- Installation instructions (step-by-step)
- Hardware requirements (GPU, RAM, disk space)
- Expected runtime for main experiments
- Instructions to reproduce each table and figure in the paper
- Pre-trained model links (if applicable)
- License
- Citation in BibTeX format

### 2. Benchmarks and Experimental Design

#### 2.1 Fair Comparison Guidelines

1. **Use established benchmarks** -- prefer widely-used benchmarks over custom datasets
2. **Report baseline results** -- re-run baselines in your environment rather than copying numbers from papers (results vary by hardware, library versions, and random seeds)
3. **Hyperparameter tuning** -- apply equal tuning effort to baselines and proposed method
4. **Tuning protocol** -- report:
   - Search strategy (grid, random, Bayesian)
   - Search space for each hyperparameter
   - Number of trials
   - Validation set used for selection
5. **Multiple runs** -- report mean and standard deviation over at least 3-5 runs with different random seeds
6. **Statistical significance** -- use appropriate tests (see Section 3) to determine if improvements are significant

#### 2.2 Hardware and Runtime Reporting

Report in the paper:
- GPU model and count (e.g., "4x NVIDIA A100 80GB")
- CPU model and core count
- RAM available
- Training time (wall-clock hours)
- Inference time (per sample or per batch)
- Total compute cost (GPU-hours)
- Software versions (PyTorch, TensorFlow, CUDA, cuDNN)

#### 2.3 Dataset Reporting

For each dataset used, report:
- Source and version
- Train/validation/test split sizes and method
- Preprocessing applied
- Whether results are on the official test split
- Class distribution (for classification tasks)

### 3. ML Evaluation and Statistical Testing

#### 3.1 Statistical Tests for Model Comparison

| Scenario | Recommended Test |
|----------|-----------------|
| Two models, one test set | McNemar's test (classification), paired bootstrap (any metric) |
| Two models, multiple datasets | Wilcoxon signed-rank test |
| Multiple models, one dataset | Friedman test + Nemenyi post-hoc |
| Multiple models, multiple datasets | Friedman test + Nemenyi post-hoc |
| Two models, k-fold CV | Corrected paired t-test (Nadeau & Bengio, 2003) |

Important considerations:
- Standard paired t-test on k-fold CV results violates independence assumptions -- use the corrected version (1/k + 1/(k-1) variance correction)
- Report p-values alongside effect sizes
- Use bootstrap confidence intervals for metrics without closed-form variance (e.g., F1, BLEU)
- For deep learning, account for variance from random initialization

#### 3.2 Effect Sizes for ML

- **Cohen's d** -- for continuous performance differences between two models
- **Rank-biserial correlation** -- for Wilcoxon tests
- **Kendall's W** -- for Friedman tests (agreement among datasets)
- Report 95% confidence intervals for all metrics

#### 3.3 Cross-Validation Best Practices

1. Use stratified splits for imbalanced classification
2. Use grouped splits when data has natural groupings (e.g., patients, documents)
3. Never use test data for model selection or hyperparameter tuning
4. Report the inner/outer loop structure for nested cross-validation
5. Fix random seeds and report them

### 4. ACM Artifact Evaluation

#### 4.1 Badge Types

| Badge | Meaning | Requirements |
|-------|---------|-------------|
| **Artifacts Available** | Artifacts are publicly accessible | Archived on a permanent repository (Zenodo, Figshare) with a DOI. GitHub alone is insufficient. |
| **Artifacts Evaluated -- Functional** | Artifacts are complete, documented, and exercisable | Reviewers can run the artifacts. Documentation is sufficient. All key results can be produced. |
| **Artifacts Evaluated -- Reusable** | Artifacts are well-structured for reuse and extension | Code is modular, well-documented, and easily extensible. Follows best practices. |
| **Results Reproduced** | Main results independently verified | Independent reviewers obtain results consistent with the paper using the provided artifacts. |

#### 4.2 Preparing for Artifact Evaluation

1. **Package early** -- do not wait until the camera-ready deadline
2. **Test on a clean machine** -- verify the setup works outside your development environment
3. **Provide a "kick-the-tires" guide** -- a 30-minute guide for reviewers to verify basic functionality
4. **Estimate resource requirements** -- if experiments need 100+ GPU-hours, provide pre-computed intermediate results
5. **Archive permanently** -- deposit on Zenodo or Figshare (not just GitHub)
6. **Include a LICENSE file** -- see Section 6

### 5. AI Ethics and Responsible Computing

#### 5.1 Dataset Ethics

1. **Consent and licensing** -- verify that data was collected with appropriate consent and that usage terms permit research use
2. **Bias audit** -- assess and report demographic biases in datasets
3. **Representation** -- document which populations are represented and underrepresented
4. **Datasheets for Datasets** -- complete the Gebru et al. (2021) datasheet template
5. **Privacy** -- ensure no personally identifiable information (PII) is exposed; apply de-identification if needed

#### 5.2 Model Ethics

1. **Model cards** -- provide a model card (Mitchell et al., 2019) documenting:
   - Intended use and out-of-scope uses
   - Training data summary
   - Performance across demographic groups
   - Ethical considerations and limitations
2. **Dual use** -- acknowledge potential misuse and describe mitigation steps
3. **Environmental impact** -- report estimated carbon emissions using tools such as ML CO2 Impact (https://mlco2.github.io/impact/) or CodeCarbon; include compute region and energy source if known

#### 5.3 Human Subjects in CS Research

- User studies, surveys, and crowdsourced annotations typically require IRB approval
- MTurk/Prolific workers are human subjects -- ensure fair compensation (minimum local wage equivalent)
- Report annotator demographics, training, and inter-annotator agreement

### 6. Software Licensing Guide

| License | Permissions | Conditions | Use When |
|---------|------------|------------|----------|
| **MIT** | Commercial use, modification, distribution, private use | Include license and copyright notice | Maximum permissiveness desired |
| **Apache 2.0** | Same as MIT + patent grant | Include license, copyright, state changes, NOTICE file | Patent protection needed |
| **BSD 2-Clause** | Same as MIT | Include license and copyright notice | Simple permissive license preferred |
| **GPL 3.0** | Commercial use, modification, distribution | Derivative works must use GPL; disclose source | Ensuring all derivatives remain open |
| **LGPL 3.0** | Same as GPL but allows linking from proprietary code | Library modifications must be GPL | Library that proprietary software may use |
| **CC BY 4.0** | Sharing, adaptation, commercial use | Attribution required | Datasets and documentation (not software) |
| **CC BY-NC 4.0** | Sharing, adaptation | Attribution required; non-commercial only | Datasets restricted to research use |

Recommendation: Use **MIT** or **Apache 2.0** for research code. Use **CC BY 4.0** for datasets. Include a `LICENSE` file in the repository root.

### 7. Authorship in CS

#### 7.1 ACM Authorship Policy

ACM requires that all co-authors:
1. Made significant intellectual contributions to the work
2. Are aware of and approve the submission
3. Accept responsibility for the work

Key differences from medical authorship:
- Author order conventions vary by subfield:
  - **Alphabetical** -- common in theory and some AI venues
  - **Contribution-based** -- first author did the most work; last author is the senior/PI
  - **Equal contribution** -- denoted by asterisk or footnote
- Ghost authorship and gift authorship are prohibited
- AI tools (e.g., ChatGPT) cannot be listed as authors

#### 7.2 CRediT for CS

Increasingly adopted by CS venues. Map contributions to the 14 CRediT roles (see medical-standards skill for the full taxonomy). Particularly relevant CS roles:
- **Software** -- programming, implementation
- **Formal analysis** -- proofs, complexity analysis
- **Investigation** -- running experiments
- **Data curation** -- dataset creation and annotation
- **Methodology** -- algorithm design

---

## Checklist

### Reproducibility
- [ ] Code publicly available in a version-controlled repository
- [ ] Dependencies pinned with exact versions
- [ ] Dockerfile or equivalent containerization provided
- [ ] README includes installation, hardware requirements, and reproduction steps
- [ ] Random seeds fixed and reported
- [ ] Pre-trained models/checkpoints available (if applicable)
- [ ] Data publicly available or synthetic substitute provided
- [ ] Dataset documented with datasheet or data card

### Benchmarks and Experiments
- [ ] Established benchmarks used where available
- [ ] Baselines re-run in the same environment
- [ ] Equal hyperparameter tuning effort for baselines and proposed method
- [ ] Tuning protocol documented (search space, strategy, number of trials)
- [ ] Results averaged over multiple runs with standard deviations reported
- [ ] Statistical significance tests applied for key comparisons
- [ ] Hardware and software versions reported
- [ ] Training and inference times reported

### Artifact Evaluation
- [ ] Artifacts archived with a DOI (Zenodo/Figshare)
- [ ] Tested on a clean machine
- [ ] Kick-the-tires guide provided
- [ ] Resource requirements documented

### Ethics
- [ ] Dataset consent and licensing verified
- [ ] Bias assessment performed and reported
- [ ] Model card provided (for released models)
- [ ] Environmental impact estimated and reported
- [ ] IRB approval obtained for human subjects research
- [ ] Fair compensation for crowdworkers documented

### Licensing and Authorship
- [ ] LICENSE file included in repository
- [ ] All authors meet ACM authorship criteria
- [ ] Author contributions documented
- [ ] AI tool usage disclosed per venue policy

---

## References

- ACM. Artifact Review and Badging, Version 1.1. https://www.acm.org/publications/policies/artifact-review-and-badging-current
- ACM. Policy on Authorship. https://www.acm.org/publications/policies/new-acm-policy-on-authorship
- Gebru T, Morgenstern J, Vecchione B, et al. Datasheets for Datasets. Communications of the ACM. 2021;64(12):86-92. doi:10.1145/3458723
- Mitchell M, Wu S, Zaldivar A, et al. Model Cards for Model Reporting. In: Proc. FAT* 2019. pp. 220-229. doi:10.1145/3287560.3287596
- Nadeau C, Bengio Y. Inference for the Generalization Error. Machine Learning. 2003;52(3):239-281. doi:10.1023/A:1024068626366
- Demsar J. Statistical Comparisons of Classifiers over Multiple Data Sets. JMLR. 2006;7:1-30.
- Pineau J, et al. Improving Reproducibility in Machine Learning Research (A Report from the NeurIPS 2019 Reproducibility Program). JMLR. 2021;22(164):1-20.
- Henderson P, Islam R, Bachman P, Pineau J, Precup D, Meger D. Deep Reinforcement Learning that Matters. In: Proc. AAAI 2018. pp. 3207-3214.
- Strubell E, Ganesh A, McCallum A. Energy and Policy Considerations for Deep Learning in NLP. In: Proc. ACL 2019. pp. 3645-3650. doi:10.18653/v1/P19-1355
- choosealicense.com. Choose an open source license. https://choosealicense.com/
