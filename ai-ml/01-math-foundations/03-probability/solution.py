# solution.py - Probability answers

import random

# TODO 1 & 2
def roll_die():
    return random.randint(1, 6)

rolls = 6000
count_six = sum(1 for _ in range(rolls) if roll_die() == 6)
print(f"Experimental Prob of 6: {count_six/rolls:.4f}")

# TODO 3
# Answer: P(A|B) = (P(B|A) * P(A)) / P(B)

# TODO 4
# Calculation: (0.9 * 0.2) / 0.4 = 0.18 / 0.4 = 0.45
print(f"P(Rain|Clouds) = {0.45}")

# TODO 5
# Answer: Discrete distributions (like Bernoulli) are 
# for things you can count (1, 2, 3 heads). Continuous 
# distributions (like Normal) are for things you can 
# measure (height, weight, time).

# TODO 6
# Answer: The Binomial Distribution (a sequence of 
# Bernoulli trials).

# CHALLENGE ANSWER
# Prob of Ace of Spades = 1/52
# 3 times in a row with replacement = (1/52)^3
prob = (1/52)**3
print(f"Triple draw probability: {prob:.8f}")

print("\n--- Why it works ---")
print("1. Decision Making: AI models don't say 'Yes'; they say '95% Yes'. Probability gives us a mathematical way to handle that doubt.")
print("2. Noise: Real data is messy. Probability distributions help us 'filter' the noise from the actual signal.")
print("3. Bayesian Learning: Updating our model's weights as we see more data is fundamentally a Bayesian update process.")
print("4. Generative AI: Large Language Models (LLMs) work by predicting the *most probable* next word in a sequence.")

export {};
