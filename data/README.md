# Water-Quality Data Guide / 数据导航 / Guide des données

[中文](#中文) | [English](#english) | [Français](#français)

## 中文

先从下表选择分析任务，再检查候选输入的列名、单位、编码和时间范围。候选关系来自源码路径与文件名匹配，不代表已验证完整生成链。所有数据原样保留；相同内容的副本也未删除。

| 目录 | 内容与用途 |
| --- | --- |
| `raw/` | 原始提交的4份CSV；作为观测数据入口 |
| `processed/` | 合并、清洗、月度汇总、WQI及等级相关中间表 |
| `supplementary/csv/`、`supplementary/xlsx/` | 按监测断面组织的表格；不同格式不自动视为同一版本 |
| `supplementary/统计建模数据/` | 站点表及总氮、总磷、氨氮等指标相关WQI表 |
| `supplementary/统计建模数据 (3)/` | 另一组站点与汇总表，以及90天预测工作簿 |
| `supplementary/resultat/` | 模型统计与辅助计算工作簿 |

[完整文件索引](catalog.csv)列出每份表的大小、CSV编码、数据行数和字段。`identical_to` 指向内容完全相同的另一份文件，便于识别重复而不破坏原路径。Excel工作簿的行数和字段不在此CSV索引中推断。

`average_data_with_grade.csv` 和 `time.xlsx` 有候选文件，但原脚本使用的版本仍未确认。`绿色.xlsx` 和 `副本数据2.xlsx` 未提供；PCA脚本未指定输入。不要把“候选存在”理解为可以直接运行。预测表是模型输出，不是未来实测观测。各脚本的 `wqi`、`WQI-DET`、水质等级目标应分别理解。

## English

Choose an analysis from the script/input table below, then verify the candidate's schema, units, encoding and date coverage. Matches are based on source paths and filenames, not a validated transformation pipeline. All supplied data are retained, including byte-identical copies.

`raw/` contains four submitted CSV files. `processed/` contains combined, cleaned, monthly and index-related tables. `supplementary/csv/` and `xlsx/` hold station tables; `统计建模数据/` also includes indicator-specific WQI tables. `统计建模数据 (3)/` contains another table collection and prediction workbooks; `resultat/` contains supporting model-statistics workbooks.

The [catalog](catalog.csv) lists file sizes and, for CSV files, encoding, data-row counts and column names. `identical_to` identifies an exact-content duplicate. Workbook row counts and schemas are not inferred.

Candidates exist for `average_data_with_grade.csv` and `time.xlsx`, but the intended versions are unresolved. `绿色.xlsx` and `副本数据2.xlsx` are absent, and the PCA input is unset. Prediction workbooks are model outputs, not future measured observations. The `wqi`, `WQI-DET` and grade targets describe different tasks.

## Français

Choisir une analyse dans le tableau ci-dessous, puis vérifier les colonnes, unités, encodages et périodes. Les correspondances reposent sur les chemins et noms de fichiers ; elles ne constituent pas une chaîne de traitement validée. Toutes les données fournies sont conservées, y compris les copies identiques.

`raw/` contient quatre CSV soumis initialement ; `processed/` les tableaux regroupés, nettoyés, mensuels et les indices. Les sous-dossiers `csv/` et `xlsx/` de `supplementary/` contiennent les données par station. `统计建模数据/` comprend aussi des indices par indicateur ; `统计建模数据 (3)/` d’autres tableaux et des prédictions ; `resultat/` des classeurs statistiques complémentaires.

Le [catalogue](catalog.csv) donne les tailles et, pour les CSV, les encodages, nombres de lignes et colonnes. `identical_to` désigne une copie au contenu strictement identique. Les schémas et nombres de lignes des classeurs ne sont pas déduits.

Des candidats existent pour `average_data_with_grade.csv` et `time.xlsx`, mais les versions attendues restent à confirmer. `绿色.xlsx` et `副本数据2.xlsx` sont absents et l’entrée de l’ACP n’est pas configurée. Les prédictions ne sont pas des observations futures mesurées. Les cibles `wqi`, `WQI-DET` et classe de qualité correspondent à des tâches différentes.

## Script → Input / 脚本 → 输入 / Script → Entrée

| Script | Input | Repository candidates |
| --- | --- | --- |
| [`M-K final.py`](../scripts/M-K%20final.py) | `all.csv` | [data/supplementary/统计建模数据 (3)/all.csv](../data/supplementary/%E7%BB%9F%E8%AE%A1%E5%BB%BA%E6%A8%A1%E6%95%B0%E6%8D%AE%20%283%29/all.csv) |
| [`M-K WQI.py`](../scripts/M-K%20WQI.py) | `高家川.csv` | [data/supplementary/统计建模数据/高家川.csv](../data/supplementary/%E7%BB%9F%E8%AE%A1%E5%BB%BA%E6%A8%A1%E6%95%B0%E6%8D%AE/%E9%AB%98%E5%AE%B6%E5%B7%9D.csv)<br>[data/supplementary/统计建模数据 (3)/高家川.csv](../data/supplementary/%E7%BB%9F%E8%AE%A1%E5%BB%BA%E6%A8%A1%E6%95%B0%E6%8D%AE%20%283%29/%E9%AB%98%E5%AE%B6%E5%B7%9D.csv) |
| [`M-K PREDICT.py`](../scripts/M-K%20PREDICT.py) | `千河公路桥WQI预测.xlsx` | [data/supplementary/统计建模数据 (3)/千河公路桥WQI预测.xlsx](../data/supplementary/%E7%BB%9F%E8%AE%A1%E5%BB%BA%E6%A8%A1%E6%95%B0%E6%8D%AE%20%283%29/%E5%8D%83%E6%B2%B3%E5%85%AC%E8%B7%AF%E6%A1%A5WQI%E9%A2%84%E6%B5%8B.xlsx) |
| [`extratrees.py`](../scripts/extratrees.py) | `千河公路桥.csv` | [data/supplementary/统计建模数据/千河公路桥.csv](../data/supplementary/%E7%BB%9F%E8%AE%A1%E5%BB%BA%E6%A8%A1%E6%95%B0%E6%8D%AE/%E5%8D%83%E6%B2%B3%E5%85%AC%E8%B7%AF%E6%A1%A5.csv)<br>[data/supplementary/统计建模数据 (3)/千河公路桥.csv](../data/supplementary/%E7%BB%9F%E8%AE%A1%E5%BB%BA%E6%A8%A1%E6%95%B0%E6%8D%AE%20%283%29/%E5%8D%83%E6%B2%B3%E5%85%AC%E8%B7%AF%E6%A1%A5.csv) |
| [`predict.py`](../scripts/predict.py) | `average_data_with_grade.csv` | [data/supplementary/统计建模数据 (3)/average_data_with_grade.csv](../data/supplementary/%E7%BB%9F%E8%AE%A1%E5%BB%BA%E6%A8%A1%E6%95%B0%E6%8D%AE%20%283%29/average_data_with_grade.csv) |
| [`predictdata.py`](../scripts/predictdata.py) | `average_data_with_grade.csv` | [data/supplementary/统计建模数据 (3)/average_data_with_grade.csv](../data/supplementary/%E7%BB%9F%E8%AE%A1%E5%BB%BA%E6%A8%A1%E6%95%B0%E6%8D%AE%20%283%29/average_data_with_grade.csv) |
| [`shapmodule.py`](../scripts/shapmodule.py) | `柏树林.csv` | [data/processed/柏树林.csv](../data/processed/%E6%9F%8F%E6%A0%91%E6%9E%97.csv) |
| [`taylor.py`](../scripts/taylor.py) | `time.xlsx` | [data/supplementary/resultat/time.xlsx](../data/supplementary/resultat/time.xlsx) |
| [`层次聚类分析.py`](../scripts/%E5%B1%82%E6%AC%A1%E8%81%9A%E7%B1%BB%E5%88%86%E6%9E%90.py) | `ALL_cleaned_gbk.csv` | [data/processed/ALL_cleaned_gbk.csv](../data/processed/ALL_cleaned_gbk.csv) |
| [`斯皮尔曼.py`](../scripts/%E6%96%AF%E7%9A%AE%E5%B0%94%E6%9B%BC.py) | `ALL_cleaned_gbk.csv` | [data/processed/ALL_cleaned_gbk.csv](../data/processed/ALL_cleaned_gbk.csv) |
| [`主成分分析.py`](../scripts/%E4%B8%BB%E6%88%90%E5%88%86%E5%88%86%E6%9E%90.py) | Not configured | — |
| [`巴特利 KMO.py`](../scripts/%E5%B7%B4%E7%89%B9%E5%88%A9%20KMO.py) | `绿色.xlsx` | — |
| [`正态检验2.py`](../scripts/%E6%AD%A3%E6%80%81%E6%A3%80%E9%AA%8C2.py) | `副本数据2.xlsx` | — |

See [runtime notes](../docs/REPRODUCIBILITY.md) for statistical assumptions and configuration.
