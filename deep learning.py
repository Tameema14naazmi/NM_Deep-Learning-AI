import pandas as pd
try:
    df = pd.read_csv('test.csv')
    display(df.head())
except FileNotFoundError:
    print("Error: 'test.csv' not found. Please ensure the file exists in the current directory.")
    df = None  # Assign None to df to indicate failure
except pd.errors.EmptyDataError:
    print("Error: 'test.csv' is empty.")
    df = None
except pd.errors.ParserError:
    print("Error: 'test.csv' could not be parsed correctly.")
    df = None
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    df = None
   # Check the shape of the DataFrame
print("Shape of the DataFrame:", df.shape)

# Examine the data types of each column
print("\nData types of each column:\n", df.dtypes)

# Identify and count missing values in each column
print("\nMissing values per column:\n", df.isnull().sum())

# Analyze numerical features
print("\nSummary statistics for numerical features:\n", df.describe())

# Since all features appear to be numerical, analyze their distributions with histograms
import matplotlib.pyplot as plt

# Select a sample for faster plotting (optional, but recommended for large datasets)
sample_df = df.sample(n=100, random_state=42)

plt.figure(figsize=(15, 6))  # Adjust figure size for better visibility
plt.hist(sample_df['pixel0'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.title("Distribution of Pixel 0 Values (Sample)")
plt.show()

# Check for categorical features (though none are expected given the column names)
# If there were categorical features, you would examine unique values and frequencies:
# for col in df.columns:
#     if df[col].dtype == 'object':  # Check if the column is of object type (string/categorical)
#         print(f"\nUnique values and frequencies for {col}:")
#         print(df[col].value_counts())
# Since no categorical columns are found, this part of the code is commented out.
#  import matplotlib.pyplot as plt

# Calculate descriptive statistics
descriptive_stats = df.describe()
display(descriptive_stats)

# Visualize the distribution of a few sample pixel columns
num_columns_to_plot = 5  # Number of pixel columns to visualize
fig, axes = plt.subplots(1, num_columns_to_plot, figsize=(15, 4))  # Adjust figure size

for i, col in enumerate(df.columns[:num_columns_to_plot]):
    axes[i].hist(df[col], bins=20, color='skyblue', edgecolor='black')
    axes[i].set_xlabel("Pixel Value")
    axes[i].set_ylabel("Frequency")
    axes[i].set_title(f"Distribution of {col}")

plt.tight_layout()
plt.show()

# Analyze the frequency distribution if there were any categorical columns
# Since we know all columns are numerical, this part is commented
# for col in df.columns:
#    if df[col].dtype == 'object':
#        print(f"\nUnique values and frequencies for {col}:\n{df[col].value_counts()}")
import matplotlib.pyplot as plt

# Number of columns to plot per figure
columns_per_figure = 10

# Iterate through the columns and create histograms in groups
for i in range(0, len(df.columns), columns_per_figure):
    fig, axes = plt.subplots(2, 5, figsize=(16, 8))  # Adjust figure size
    axes = axes.flatten()  # Flatten the axes array for easier iteration
    for j in range(columns_per_figure):
      if i + j < len(df.columns):
          column_name = df.columns[i + j]
          axes[j].hist(df[column_name], bins=20, color='skyblue', edgecolor='black')
          axes[j].set_title(column_name)
          axes[j].set_xlabel("Pixel Value")
          axes[j].set_ylabel("Frequency")
      else:
          axes[j].axis('off') # Hide empty subplots
    plt.tight_layout()
    plt.show()