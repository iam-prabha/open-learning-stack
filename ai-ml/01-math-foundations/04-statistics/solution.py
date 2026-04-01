# solution.py - Statistics answers

import numpy as np

# TODO 1 & 2
sample = np.random.randint(0, 101, 50)
print(f"Mean: {np.mean(sample):.2f}")
print(f"Var: {np.var(sample):.2f}")

# TODO 3
# Answer: Because house prices are highly skewed (a few 
# multi-million dollar mansions can pull the 'Mean' 
# way up). The 'Median' represents the 'middle' house, 
# which is more realistic for the average buyer.

# TODO 4
# Answer: 0.0 (The data does not vary at all!)

# TODO 5
# Z = (85 - 70) / 10 = 1.5
print(f"Standardized Z-score: 1.5")

# TODO 6
# Answer: The probability that the observed difference 
# between models happened by pure chance. A p-value 
# < 0.05 is the standard threshold for 'Significance'.

# CHALLENGE ANSWER
def find_outliers(data):
    m = np.mean(data)
    s = np.std(data)
    return [x for x in data if abs(x - m) > 3 * s]

test_data = [10, 11, 12, 10, 11, 1000]
print(f"Outliers found: {find_outliers(test_data)}")

print("\n--- Why it works ---")
print("1. Data Cleaning: Statistics helps us spot outliers (errors) that would otherwise confuse our AI model.")
print("2. Normalization: Most AI models work best when all input features are at the same scale (Z-scores).")
print("3. Integrity: Statistics prevents us from 'cherry-picking' lucky results; it forces us to prove our model is actually better.")
print("4. Generalization: By understanding the distribution of our training data, we can predict how well the model will perform on new, unseen data.")

export {};
