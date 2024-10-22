from sklearn.datasets import make_blobs,make_swiss_roll,make_s_curve,make_moons
import pandas as pd

# Function to save a dataset (X, y) to a CSV file
def save_to_csv(X, y, filename, feature_names=None):
    if feature_names is None:
        feature_names = [f"Feature{i+1}" for i in range(X.shape[1])]
    
    # Create a DataFrame
    df = pd.DataFrame(X, columns=feature_names)
    df['Target'] = y  # Add the target column
    
    # Save to CSV
    df.to_csv(filename, index=False)
    print(f"Saved {filename}")

# create 2D datasets with 100 sample points
def create2DSetsWith100Samples():
    x,y = make_blobs(n_samples=100, centers=2, n_features=2)
    save_to_csv(x,y,'2D_Blobs.csv')
    x,y = make_moons(n_samples=100)
    save_to_csv(x,y,'2D_Moons.csv')


# create 3D datasets with 500 sample points, 3 centers
def create3DSetsWith500Samples():
    x,y = make_blobs(n_samples=500, centers=3, n_features=3)
    save_to_csv(x,y,'3D_Blobs.csv')
    x,y = make_s_curve(n_samples=500)
    save_to_csv(x,y,'3D_S_Curve.csv')
    x,y = make_swiss_roll(n_samples=500)
    save_to_csv(x,y,'3D_Swiss_Roll.csv')

# create 5D datasets with 2000 sample points, 5 centers
def create5DSetsWith3000Samples():
    x,y = make_blobs(n_samples=2000, centers=5, n_features=5)
    save_to_csv(x,y,'5D_Blobs.csv')

# create 10D datasets with 10000 sample points
def create10DSetWith10000Samples():
    x,y = make_blobs(n_samples=10000, centers=7, n_features=10)
    save_to_csv(x,y,'10D_Blobs.csv')


create2DSetsWith100Samples()
create3DSetsWith500Samples()
create5DSetsWith3000Samples()
create10DSetWith10000Samples()

print('Datasets have been generated successfully')