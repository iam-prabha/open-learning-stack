# example.py - Statistics & Hypothesis Testing

import numpy as np
from scipy import stats

# 1. Descriptive Statistics
data = [10, 12, 12, 13, 15, 18, 20, 22, 24, 100] # 100 is an outlier

print(f"Mean: {np.mean(data)}") # 24.6
print(f"Median: {np.median(data)}") # 14.0 (Better for this data!)
print(f"Variance: {np.var(data):.2f}")
print(f"Std Dev: {np.std(data):.2f}")

# 2. Rescaling Data (Standardization)
# Z = (x - mean) / std
standardized = (data - np.mean(data)) / np.std(data)
print(f"\nStandardized Data (Mean ~0, Std ~1):\n{standardized}")

# 3. Hypothesis Testing (t-test)
# Let's compare the performance of Model A vs Model B
# Does Model B (mean 0.85) actually outperform Model A (mean 0.80)?
model_a_scores = [0.78, 0.81, 0.79, 0.82, 0.80]
model_b_scores = [0.84, 0.86, 0.85, 0.83, 0.87]

t_stat, p_value = stats.ttest_ind(model_a_scores, model_b_scores)
print("\n--- Hypothesis Test ---")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.6f}")

if p_value < 0.05:
    print("Result: Statistically Significant improvement!")
else:
    print("Result: Improvement could be due to luck.")
