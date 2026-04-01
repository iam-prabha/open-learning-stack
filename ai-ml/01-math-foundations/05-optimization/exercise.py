# exercise.py - Practice with Optimization

import numpy as np

# TODO 1: Given a loss function f(w) = w^2 + 4w, 
# find the gradient at w = 0.
# (Hint: f'(w) = 2w + 4)

# TODO 2: If the gradient is +4 and our learning 
# rate is 0.1, what will be our next weight 
# if we start at w=0?
# (Formula: w_new = w_old - lr * grad)

# TODO 3: Define 'Stochastic Gradient Descent' 
# in one sentence.
# Answer: ...

# TODO 4: What happens to the optimization process 
# if the learning rate is EXTREMELY small (e.g. 0.0000001)?
# Answer: ...

# TODO 5: Define a simple 'Momentum' update. 
# (It uses the PREVIOUS step's velocity to speed up 
# a slow descent).

# TODO 6: Why is 'MSE' (Mean Squared Error) a common 
# choice for a Loss Function in regression?
# Answer: ...

# CHALLENGE: Write a loop that runs Gradient Descent 
# for f(w) = w^2 until the loss is smaller than 0.001. 
# Print the number of steps taken.

# --- Verification ---
print("--- Results ---")
# Check your logic vs the solution!
