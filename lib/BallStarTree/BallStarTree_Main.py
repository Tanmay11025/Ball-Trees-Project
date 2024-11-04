import pandas as pd
import os
from BallStarTree import BallStarTree

# Double check the path to the dataset if you encounter a FileNotFoundError

# Define the relative path to the dataset
file_dir = os.path.dirname(__file__)  # Directory of the current Python file
csv_path = os.path.join(file_dir, '..', '..', 'Datasets', 'csv', '2D_Moons.csv')  # Go up and locate Datasets

# Loading data
df = pd.read_csv(csv_path)
data = df[['Feature1', 'Feature2']].to_numpy()

# Initialize and fit the Ball* Tree
ball_star_tree = BallStarTree(data=data, leaf_size=10, max_iterations=100, alpha=0.5, S=10)
ball_star_tree.fit()  # This will print the structure of the tree and plot it