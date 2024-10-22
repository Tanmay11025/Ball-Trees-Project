import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot2DGraph(csv_file):
    # Load the CSV file into a DataFrame
    data = pd.read_csv(csv_file)
    
    # Check if the file contains 'X' and 'Y' columns
    if 'Feature1' in data.columns and 'Feature2' in data.columns:
        # Plot the data
        plt.scatter(data['Feature1'], data['Feature2'])
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('2D Scatter Plot')
        plt.show()
    else:
        print("The CSV file is not two dimensional!")
   

def plot_3d_blobs(csv_file):
    # Load the CSV file into a DataFrame
    data = pd.read_csv(csv_file)
    
    # Check if the file contains 'X', 'Y', and 'Z' columns
    if 'Feature1' in data.columns and 'Feature2' in data.columns and 'Feature3' in data.columns:
        # Create a 3D plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot the data
        ax.scatter(data['Feature1'], data['Feature2'], data['Feature3'])

        # Label the axes
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('3D Scatter Plot')

        # Show the plot
        plt.show()
    else:
        print("The CSV file does not contain 'X', 'Y', and 'Z' columns.")
        
# Usage example:
plot_3d_blobs('3D_S_Curve.csv')

# Usage example:
plot2DGraph('2D_Blobs.csv')
