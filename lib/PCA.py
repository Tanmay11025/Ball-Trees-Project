import numpy as np
import pandas as pd
from math import *
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

class BallTreeNode:
    def __init__(self, data=None, left=None, right=None, center=None, radius=None):
        self.data = data         # Data points at this node
        self.left = left         # Left child
        self.right = right       # Right child
        self.center = center     # Center of the ball
        self.radius = radius     # Radius of the ball

class BallStarTree:
    def __init__(self, data, leaf_size=10, max_iterations=100, alpha=0.5, S=10):
        self.root = None             # Root node of the tree
        self.data = data             # Initial dataset (n-dimensional points)
        self.leaf_size = leaf_size   # Threshold for leaf size
        self.max_iterations = max_iterations  # Power iteration convergence
        self.alpha = alpha           # Weight for objective function
        self.S = S                   # Number of intervals for splitting

    def power_iteration(self, data):
        """
        This function performs the power iteration method to find the top principal component of the covariance matrix.
        """
        centered_data = data - np.mean(data, axis=0) # axis=0 makes sure the mean is along columns

        # Note: We're assume the data is normalized, i.e., zero mean and unit variance
        # Fix this later by adding a normalization step
        
        # Step 1: Compute covariance matrix
        covariance_matrix = np.cov(centered_data, rowvar=False)

        # Step 2: Power iteration on the covariance matrix to find the top principal component
        b_k = np.random.rand(covariance_matrix.shape[1])
        for _ in range(self.max_iterations):
            b_k1 = np.dot(covariance_matrix, b_k)
            b_k = b_k1 / np.linalg.norm(b_k1)
        
        return b_k

    def _calculate_center_and_radius(self, data):
        """
        Calculates the center and radius for a given set of points.
        """
        center = np.mean(data, axis=0) 
        radius = np.max(np.linalg.norm(data - center, axis=1))  # axis=1 calculates norm per row
        return center, radius

    def _split_node(self, node, count = 0):
        """
        Recursively split the node into two children nodes. 
        The node is split along the principal component of the data points.
        The center and radius of the ball are calculated for each node (including leaves).
        The optimal split threshold is found using an objective function that balances the size of the two children nodes.
        """
        data = node.data
        # Calculate center and radius for every node, including leaves
        node.center, node.radius = self._calculate_center_and_radius(data)

        if len(data) <= self.leaf_size:
            # Stop further splitting for leaf nodes
            return

        # Calculate the principal component
        principal_component = self.power_iteration(data)
        # Project the data points onto the principal component
        projections = data @ principal_component

        # Find the best threshold to split the data
        t_min, t_max = projections.min(), projections.max()
        N = len(projections)
        best_threshold = t_min
        min_objective = float('inf')
        optimal_N1, optimal_N2 = None, None

        # The objective function balances the size of the two children nodes
        # and the distance of the threshold from the center of the data
        for i in range(1, self.S):
            threshold = t_min + i * (t_max - t_min) / self.S
            N1 = np.sum(projections <= threshold)
            N2 = N - N1
            term1 = abs(N2 - N1) / N
            term2 = fabs(threshold - ((t_min + t_max) / 2)) / (t_max - t_min)
            objective_value = term1 + self.alpha * term2

            if objective_value < min_objective:
                min_objective = objective_value
                best_threshold = threshold
                optimal_N1, optimal_N2 = N1, N2

        # Split the data based on the best threshold
        left_data = data[projections <= best_threshold]
        right_data = data[projections > best_threshold]

        # Create left and right child nodes
        node.left = BallTreeNode(data=left_data)
        node.right = BallTreeNode(data=right_data)

        # To control the depth of the tree (uncomment below lines)
        # count += 1
        # if (count == 2):
        #     return

        # Recursively split child nodes
        self._split_node(node.left, count)
        self._split_node(node.right, count)

    def _plot_tree(self, node, ax):
        # Plot the circle for the current node
        if node is None:
            return

        # Draw the node's circle if it has a radius and center defined
        if node.radius is not None and node.center is not None:
            circle = Circle(node.center, node.radius, color='blue', fill=False, linestyle='--', linewidth=1)
            ax.add_patch(circle)
            # ax.plot(node.center[0], node.center[1], 'ro')  # Mark the center of the circle

        # Recursively plot left and right children
        if node.left is not None:
            self._plot_tree(node.left, ax)
        if node.right is not None:
            self._plot_tree(node.right, ax)

    def plot(self):
        # Check if the data is 2D
        if self.data.shape[1] != 2:
            print("Plotting is supported only for 2D data.")
            return

        # Create a plot
        fig, ax = plt.subplots(figsize=(8, 8))

        # Plot data points
        ax.scatter(self.data[:, 0], self.data[:, 1], s=10, color='black', label='Data Points')

        # Plot the tree recursively
        self._plot_tree(self.root, ax)

        # Set plot limits
        # ax.set_xlim(self.data[:, 0].min() - 1, self.data[:, 0].max() + 1)
        # ax.set_ylim(self.data[:, 1].min() - 1, self.data[:, 1].max() + 1)
        ax.set_aspect('equal', 'box')
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.title("Ball* Tree Visualization")
        plt.legend()
        plt.show()

    def print_tree(self, node=None, depth=0):
        """
        Recursively prints the Ball* Tree structure with indentation representing depth.
        """
        if node is None:
            node = self.root
        
        # Print the current node's details
        indent = "  " * depth
        print(f"{indent}Depth {depth}, Points: {len(node.data)}, Radius: {node.radius}, Center: {node.center}")

        # Recursively print the left and right children, if they exist
        if node.left is not None:
            print(f"{indent}Left:")
            self.print_tree(node.left, depth + 1)
        if node.right is not None:
            print(f"{indent}Right:")
            self.print_tree(node.right, depth + 1)

    def fit(self):
        """
        Fit the Ball* Tree on the data.
        """
        self.root = BallTreeNode(data=self.data)
        self._split_node(self.root)
        # Once tree has been built, print the structure and plot it
        self.print_tree(self.root)
        # NOTE: This works only for 2D data. 
        # For higher dimensions, modify the plot function or comment out the code below
        self.plot()



# Loading data
df = pd.read_csv('../Datasets/csv/2D_Blobs.csv')
data = df[['Feature1', 'Feature2']].to_numpy()

# Initialize and fit the Ball* Tree
ball_star_tree = BallStarTree(data=data, leaf_size=10, max_iterations=100, alpha=0.5, S=10)
ball_star_tree.fit()  # This will print the structure of the tree and plot it