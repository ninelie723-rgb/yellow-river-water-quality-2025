# Yellow River Water Quality Analysis (2025)

A historical team competition project exploring water quality in the Shaanxi section of the Yellow River basin through statistical analysis, water-quality indices, regression and SHAP explanations.

The archived project description covers January 2021–April 2025 and 18 monitoring sections. These scope statements have not been independently reconstructed from the excluded data.

## Contents

- `scripts/`: 13 historical Python analysis scripts, with publication edits documented below.
- `docs/REPRODUCIBILITY.md`: input gaps, environment limitations and methodological concerns.
- `docs/script-inputs.csv`: historical input inventory, with personal paths removed.
- `data/README.md`: data availability and provenance status.
- `requirements.txt`: inferred direct dependencies; versions and compatibility are unverified.

The scripts cover trend analysis, hierarchical clustering, PCA, normality and correlation tests, regression comparisons, Extra Trees and SHAP. Script names reflect the historical archive and do not establish that each method is implemented correctly.

## Reproduction status

**This is a research archive, not a verified runnable pipeline.** Python syntax has been checked, but dependencies have not been installed and analyses, training and reported results have not been reproduced on this Mac. No performance claim is made by this candidate.

Historical scripts use Windows paths, Chinese column names and GBK/UTF-8 encodings. Configure authorized inputs and separate output paths before running individual scripts. There is no validated execution order. Some inputs remain missing or ambiguous, and `主成分分析.py` has an empty input path.

Random 80/20 splits used by some scripts do not establish future forecasting performance. `wqi`, `WQI-DET` and water-quality grade are different targets and must not be combined in one performance claim.

## Publication edits

Personal macOS directories and chat-cache identifiers were replaced by generic `local-inputs/` paths. The environment-specific `ace_tools` display call was replaced with `print`. Numerical algorithms and historical Windows paths were retained. The paper, historical data tables, submission records and local reference materials are excluded from this candidate.

## Attribution and permissions

This was a team competition project. Per-file authorship, coauthor permission to publish and data redistribution terms remain to be confirmed. No repository-wide license has been assigned. Existing author attribution must be preserved. Publication of this candidate requires the project owner's confirmation of the code publication scope and team permissions.
