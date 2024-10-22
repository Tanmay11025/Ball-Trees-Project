import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def plotReducedNDimensionalGraph(csv_file, n_components=2):
    """
    Load data from a CSV file, apply PCA to reduce it to 'n_components' dimensions,
    and plot a 2D scatter plot of the reduced data.
    
    Args:
        csv_file (str): Path to the CSV file containing the data.
        n_components (int): Number of principal components to reduce the data to (default is 2).
    """
    # Load CSV data
    data = pd.read_csv(csv_file)
    
    # Apply PCA to reduce to n_components dimensions for visualization
    pca = PCA(n_components=n_components)
    reduced_data = pca.fit_transform(data)
    
    # Check if the data has been reduced to 2 components for plotting
    if n_components == 2:
        # Plot 2D scatter plot of PCA-reduced data
        plt.scatter(reduced_data[:, 0], reduced_data[:, 1])
        plt.xlabel('PCA1')
        plt.ylabel('PCA2')
        plt.title('2D Scatter Plot (PCA)')
        plt.show()
    else:
        print(f"PCA reduced data to {n_components} dimensions. Plotting is only possible for 2 dimensions.")

# Usage example:
plotReducedNDimensionalGraph('5D_Blobs.csv')
