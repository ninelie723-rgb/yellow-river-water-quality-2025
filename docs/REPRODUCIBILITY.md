# Running the Water-Quality Analyses

## Environment

`requirements.txt` lists the directly imported analysis libraries. Original package versions are unavailable, so the environment is not pinned. Use a dedicated environment and record versions when reproducing an analysis.

Scripts use Chinese column names, GBK/UTF-8 encodings and fonts such as SimHei. Configure the appropriate encoding and an installed font. The scripts run independently; no validated pipeline order is provided.

## Inputs

See `script-inputs.csv` for the per-script input inventory. Configure input paths before execution and choose a separate output location for generated predictions.

- Trend scripts use historical station tables or prediction workbooks.
- `extratrees.py` uses the 千河公路桥 station table and writes a prediction workbook.
- `shapmodule.py` uses 柏树林.csv. Do not silently substitute 柏树坪.csv: these are different filenames.
- `predict.py` and `predictdata.py` require a compatible average_data_with_grade.csv. The intended input version remains unresolved.
- `taylor.py` requires time.xlsx with model comparison statistics; the intended version remains unresolved.
- `巴特利 KMO.py` and `正态检验2.py` refer to 绿色.xlsx and 副本数据2.xlsx; their intended input versions remain unresolved.
- `主成分分析.py` has an empty input path and selects fluoride, hexavalent chromium and cyanide among its variables. Supply a dataset with the required fields and establish its relationship to the study data before use.

Matching a filename alone does not establish that a table is the correct analysis input. Check column names, units, date coverage and transformations.

## Model targets and validation

The scripts use different targets: `wqi`, `WQI-DET` and water-quality grade. Interpret and evaluate each task separately.

`extratrees.py` uses year/month/day/hour features, 100 Extra Trees estimators and a random 80/20 split. It exports 90 daily predictions starting on 2025-05-01. The script computes test predictions but does not produce a complete RMSE/R² evaluation report. Random holdout results do not validate independent future-period forecasting.

## Statistical interpretation

- `巴特利 KMO.py` and the PCA script call `scipy.stats.bartlett`, which tests equality of variances; this is not Bartlett’s test of sphericity. KMO is not implemented in the named script.
- `taylor.py` derives correlation from the square root of R² and supplies ordinary RMSE as centered RMS difference. Recompute the required statistics from paired observations and predictions before interpreting the Taylor diagram.
- The Mann–Kendall implementations differ in continuity correction and do not provide complete handling of ties or serial dependence. Review these assumptions before drawing inferential conclusions.

## Reproduction status

The analyses and paper results have not been reproduced end to end in the current environment. Treat the scripts as the study implementation, with the input and methodological constraints described above.
