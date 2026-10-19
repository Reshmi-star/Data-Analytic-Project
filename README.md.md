# Logistics Delivery Performance and Cost Analysis — Week 1

## Project purpose
This repository contains the Week 1 strategic planning report and a small Python starter script for a proposed logistics analytics project.

## Files
- `Week1_Logistics_Data_Analyst_Strategic_Planning_Report.docx` — report for the Week 1 deliverable.
- `logistics_analysis_starter.py` — runnable example that calculates basic KPIs from a small illustrative dataset.
- `README_GitHub.md` — this project guide.

## Important data note
The six rows inside the starter script are illustrative examples only. They are not real company records and must not be presented as real research findings. For a full analysis, choose a public dataset, check its license and documentation, then adapt the script to its actual column names.

## Run the starter script
Install Python and pandas, then run:

```bash
python -m pip install pandas
python logistics_analysis_starter.py
```

The script prints example KPIs and creates `regional_kpi_summary.csv`.

## Proposed workflow
1. Select and document a suitable public delivery/shipment dataset.
2. Inspect columns, data types, missing values, duplicates, and unusual values.
3. Define KPI formulas and calculate descriptive statistics.
4. Explore patterns by region, distance, delivery status, and cost where those fields exist.
5. If suitable data are available, test a delivery-time regression model and evaluate it on held-out data.
6. Translate verified findings into operational recommendations.

## References
- pandas documentation: https://pandas.pydata.org/docs/getting_started/
- scikit-learn train/test split: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
- Kaggle Time to Delivery dataset page: https://www.kaggle.com/c/time-to-delivery/data

## Suggested repository name
`logistics-delivery-performance-analysis`
