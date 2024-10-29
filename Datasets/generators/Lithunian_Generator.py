import numpy as np

def lithuanian_samples(n):
    # Generate n samples in 2D using a uniform distribution
    # For a more structured distribution, you can modify the generation logic
    x = np.random.uniform(0, 1, n)
    y = np.random.uniform(0, 1, n)
    
    return np.column_stack((x, y))

# Set the number of samples
n_samples = 500000

# Generate Lithuanian samples
data = lithuanian_samples(n_samples)

# Save to CSV file, one data point per line
with open('lithuanian_data.csv', 'w') as f:
    for sample in data:
        f.write(f"{sample[0]},{sample[1]}\n")

print("CSV file 'lithuanian_data.csv' created with 500,000 samples.")
