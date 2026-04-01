# example.py - Probability & Bayes in Python

import random
import numpy as np

# 1. Frequentist probability (Coin Flips)
def simulate_coin_flips(n=1000):
    heads = sum(1 for _ in range(n) if random.random() > 0.5)
    return heads / n

print(f"Prob of Heads after 1000 flips: {simulate_coin_flips():.4f}")

# 2. Bayes' Theorem Implementation
# P(A|B) = [ P(B|A) * P(A) ] / P(B)
# Example: Probability of having a disease (D) given a positive test (+)
# P(D|+) = [ P(+|D) * P(D) ] / P(+)

def bayes_calc(prob_d, prob_pos_if_d, prob_pos_if_no_d):
    # P(D) = prior (disease rate)
    prior = prob_d
    # P(+) = P(+|D)*P(D) + P(+|noD)*P(noD)
    marginal_likelihood = (prob_pos_if_d * prior) + (prob_pos_if_no_d * (1 - prior))
    # Posterior P(D|+)
    posterior = (prob_pos_if_d * prior) / marginal_likelihood
    return posterior

# Disease rate: 1 in 1000 (0.001)
# Test Accuracy: 99% (prob_pos_if_d = 0.99)
# False Positive: 5% (prob_pos_if_no_d = 0.05)
result = bayes_calc(0.001, 0.99, 0.05)
print(f"\nProb of disease given positive test: {result:.4f} (Only {result*100:.2f}%)")
print("Interpretation: Even with a 99% accurate test, a rare prior makes a false positive more likely!")

# 3. Generating a Normal Distribution
mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 10)
print(f"\nRandom samples from Normal distribution:\n{s}")
