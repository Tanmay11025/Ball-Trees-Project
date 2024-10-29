import numpy as np
import pandas as pd

def highleyman_samples(n):
    # Generate n samples using the Highleyman distribution
    u = np.random.uniform(0, 1, n)
    v = np.random.uniform(0, 1, n)
    
    # Transform to Highleyman distribution in 2D
    x = np.cos(2 * np.pi * u) * np.sqrt(v)
    y = np.sin(2 * np.pi * u) * np.sqrt(v)
    
    return np.column_stack((x, y))

# Set the number of samples
n_samples = 500000

# Generate Highleyman samples
data = highleyman_samples(n_samples)

# Save to CSV file, one data point per line
with open('highleyman_data.csv', 'w') as f:
    for sample in data:
        f.write(f"{sample[0]},{sample[1]}\n")

print("CSV file 'highleyman_data.csv' created with 500,000 samples.")
