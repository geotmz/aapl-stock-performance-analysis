# -*- coding: utf-8 -*-
"""
Finance Project – Data Cleaning & Factor Merging
Clean version for GitHub (no GitHub commands)
"""

import pandas as pd
import pandas_datareader.data as pdr
import matplotlib.pyplot as plt
import yfinance as yf
import statsmodels.api as sm
from statsmodels.api import OLS

# -----------------------------
# 1. Load Fama-French Factors
# -----------------------------
ff = pdr.DataReader('F-F_Research_Data_Factors', 'famafrench', start='1926-01-01')
df = ff[0]
df.index = df.index.to_timestamp()

# -----------------------------
# 2. Load Momentum Factor
# -----------------------------
start = "1980-01-01"
ff_mom = pdr.DataReader('F-F_Momentum_Factor', 'famafrench', start=start)[0]
ff_mom.index = ff_mom.index.to_timestamp()

# -----------------------------
# 3. Merge FF Factors + Momentum
# -----------------------------
ffav_merged_df = pd.merge(
    ff[0],
    ff_mom,
    how='inner',
    left_index=True,
    right_index=True,
    sort=True,
    copy=True,
    indicator=True
)

# -----------------------------
# 4. Download Apple Monthly Returns
# -----------------------------
AAPL_df = yf.download('AAPL', start=start)['Close'].resample('ME').ffill().pct_change()

# Convert index to YYYY-MM format
AAPL_df['str_date'] = AAPL_df.index.astype(str)
AAPL_df['dt_date'] = pd.to_datetime(AAPL_df['str_date']).dt.strftime('%Y-%m')

# -----------------------------
# 5. Prepare FF dataset for merge
# -----------------------------
ffav_merged_df['str_date'] = ffav_merged_df.index.astype(str)
ffav_merged_df['dt_date'] = pd.to_datetime(ffav_merged_df['str_date']).dt.strftime('%Y-%m')

# -----------------------------
# 6. Merge Apple + Factors
# -----------------------------
AAPL_ffav_merge_df = pd.merge(
    AAPL_df,
    ffav_merged_df,
    how='inner',
    on='dt_date',
    sort=True,
    copy=True,
    indicator='AAPL_FF_merge_indicator',
    validate='one_to_one'
)

AAPL_ffav_merge_df.drop(columns=['str_date_x', 'str_date_y'], inplace=True)

# -----------------------------
# 7. Compute Apple Excess Return
# -----------------------------
AAPL_ffav_merge_df['AAPL_RF'] = AAPL_ffav_merge_df['AAPL'] * 100 - AAPL_ffav_merge_df['RF']

# Drop missing rows
AAPL_ffav_merge_df.dropna(axis=0, inplace=True)

# -----------------------------
# 8. Regression Model
# -----------------------------
AAPL_ffav_merge_df_c = sm.tools.add_constant(AAPL_ffav_merge_df, prepend=True)

results = OLS(
    AAPL_ffav_merge_df_c['AAPL_RF'],
    AAPL_ffav_merge_df_c[['const', 'Mkt-RF', 'SMB', 'HML', 'Mom']],
    missing='drop'
).fit()

# -----------------------------
# 9. Residual Analysis Plots
# -----------------------------
residuals = results.resid
fitted_values = results.fittedvalues

plt.figure(figsize=(10, 6))
plt.hist(residuals, bins=30)
plt.title("Histogram of Residuals")
plt.show()

sm.qqplot(residuals, line='45')
plt.title("Normal Q-Q Plot of Residuals")
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(fitted_values, residuals)
plt.axhline(0, color='red', linestyle='--')
plt.title("Residuals vs Fitted Values")
plt.show()

# -----------------------------
# 10. Export Final CSVs
# -----------------------------
AAPL_ffav_merge_df.to_csv('AAPL_ffav_merge_df.csv', index=False)
AAPL_ffav_merge_df_c.to_csv('AAPL_ffav_merge_df_c.csv', index=False)

print("Export complete.")
