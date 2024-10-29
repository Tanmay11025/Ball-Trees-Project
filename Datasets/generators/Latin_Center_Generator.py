import numpy as np
from pyDOE import lhs

# Set the number of samples and dimensions
n_samples = 500000
n_dimensions = 2

# Generate Latin hypercube samples
lhs_samples = lhs(n_dimensions, samples=n_samples)

# Save the samples to a CSV file, one data point per line
with open('latin_center_data.csv', 'w') as f:
    for sample in lhs_samples:
        f.write(f"{sample[0]},{sample[1]}\n")

print("CSV file 'latin_center_data.csv' created with 500,000 samples.")
