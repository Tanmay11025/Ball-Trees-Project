import numpy as np
from scipy.stats import qmc

def generate_sobol_samples(n):
    # Create a Sobol sequence sampler for 2D
    sampler = qmc.Sobol(d=2, scramble=True)
    points = sampler.random(n)  # Generate n samples
    return points

# Set the number of samples
n_samples = 500000

# Generate Sobol samples
data = generate_sobol_samples(n_samples)

# Save to CSV file, one data point per line
with open('sobol_data.csv', 'w') as f:
    for sample in data:
        f.write(f"{sample[0]},{sample[1]}\n")

print("CSV file 'sobol_data.csv' created with 500,000 samples.")
