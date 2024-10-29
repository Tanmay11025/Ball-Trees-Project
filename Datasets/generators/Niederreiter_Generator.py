import numpy as np

def niederreiter_samples(n):
    # Generate n Niederreiter sequence points in 2D
    points = np.zeros((n, 2))
    for i in range(n):
        x = 0
        y = 0
        for j in range(1, 2 * i + 2):
            x += (1 / (2 ** j)) * ((i >> (j - 1)) & 1)
            y += (1 / (3 ** j)) * ((i >> (j - 1)) & 1)
        points[i, 0] = x
        points[i, 1] = y
    
    return points

# Set the number of samples
n_samples = 500000

# Generate Niederreiter samples
data = niederreiter_samples(n_samples)

# Save to CSV file, one data point per line
with open('niederreiter_data.csv', 'w') as f:
    for sample in data:
        f.write(f"{sample[0]},{sample[1]}\n")

print("CSV file 'niederreiter_data.csv' created with 500,000 samples.")
