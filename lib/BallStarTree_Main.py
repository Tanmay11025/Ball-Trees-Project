import pandas as pd
from BallStarTree import BallStarTree

# Loading data
df = pd.read_csv('../Datasets/csv/2D_Blobs.csv')
data = df[['Feature1', 'Feature2']].to_numpy()

# Initialize and fit the Ball* Tree
ball_star_tree = BallStarTree(data=data, leaf_size=10, max_iterations=100, alpha=0.5, S=10)
ball_star_tree.fit()  # This will print the structure of the tree and plot it