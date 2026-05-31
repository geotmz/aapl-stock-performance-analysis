# Apple Inc. – Factor Analysis & Performance Dashboard

A Data‑Driven Financial Analysis Project

## 1. Project Overview
This project delivers a complete financial analysis of Apple Inc. (AAPL) using a combination of:

- Python for data cleaning and factor merging
- Fama–French factor models for risk/return decomposition
- Power BI for dashboard visualization
- Professional reporting for insights and interpretation

The goal is to demonstrate a structured, analyst‑level workflow:
from raw data → clean dataset → factor analysis → performance metrics → dashboard → final report.

## 2. Objectives
Build a clean, merged dataset combining Apple monthly returns with Fama–French factors

Evaluate Apple’s risk‑adjusted performance

Analyze exposures to Market, SMB, HML, and Momentum

Visualize long‑term performance trends

Produce a professional financial report summarizing insights

## 3. Data Sources

- Yahoo Finance
- Apple (AAPL) monthly adjusted close prices
- Kenneth French Data Library
- Fama–French 3 Factors (Mkt‑RF, SMB, HML)
- Momentum Factor (Mom)

All datasets were cleaned, aligned, and merged into a single analysis‑ready CSV.

## 4. Methodology
#### 4.1 Data Preparation (Python)
Downloaded Apple monthly returns

Downloaded Fama–French factors

Converted dates to consistent YYYY‑MM format

Merged datasets using one‑to‑one validation

Engineered Apple Excess Return (AAPL_RF)

Exported final datasets for modeling and Power BI

The full cleaning pipeline is available in:

scripts/data_cleaning.py

notebooks/data_cleaning_and_factor_merge.ipynb

#### 4.2 Regression Analysis
A linear regression model was used to estimate Apple’s exposure to:

Market Excess Return (Mkt‑RF)

Size (SMB)

Value (HML)

Momentum (Mom)

Residual diagnostics were performed to validate model assumptions.

#### 4.3 Dashboard (Power BI)
The dashboard includes:

- CAGR
- Annualized Volatility
- Sharpe Ratio
- Max Drawdown

- Rolling 12‑Month Volatility
- Cumulative Return
- Factor Scatter Plots

A preview image is included in the repository.

#### 4.4 Additional Analysis (Exploratory)

Additional exploratory charts used during the analysis phase are included in the `dashboard/extra/` folder. 
These visuals supported the research process but were intentionally excluded from the final Power BI dashboard 
to maintain a clean and focused design.

The folder contains:
- Annual Average Returns (exploratory)
- Drawdowns Over Time
- Factor Time Series


## 5. Key Insights
- [x] Apple delivered strong long‑term compounding with a CAGR of 18.55%

- [x] Volatility declined significantly after 2010 as Apple matured

- [x] Apple shows high sensitivity to market movements (positive beta)

- [x] Minimal exposure to value factor (HML) / consistent with growth profile

- [x] Momentum relationship is weak but slightly positive

- [x] Drawdowns were deep but followed by strong recoveries

## 6. Tools & Technologies
Python (pandas, yfinance, statsmodels)

- Power BI
- Python
- Fama–French Data Library
- Matplotlib / Seaborn
- GitHub for versioning and project structure

## 7. Final Deliverables
✔ Clean merged dataset

✔ Python data preparation script

✔ Exploratory notebook with outputs

✔ Power BI dashboard

✔ Professional 2‑page financial report

✔ Full GitHub repository
