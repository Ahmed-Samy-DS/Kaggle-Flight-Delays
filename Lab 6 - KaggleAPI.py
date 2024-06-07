# --------------------------------------------------------------------------------------------------------- #
    
import kaggle
import os
import zipfile
import pandas as pd


# Set your Kaggle API key (replace with your actual values)
kaggle.api.authenticate()

# Specify the Kaggle dataset (replace with your dataset details)
dataset_name = "usdot/flight-delays"

# Specify the directory where you want to download and extract the dataset
directory_path = "F:/Power BI Development Nov.2023 - Mar.2024/19- Power BI/6/flight-delays"

# Download the dataset
kaggle.api.dataset_download_files(dataset_name, path=directory_path, unzip=True)

# Extract all ZIP files in the directory
for file in os.listdir(directory_path):
    if file.endswith(".zip"):
        file_path = os.path.join(directory_path, file)
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(directory_path)
        os.remove(file_path)  # Remove the ZIP file after extraction 

# # Your existing code to read CSV files and create DataFrames
# csv_files = [file for file in os.listdir(directory_path) if file.endswith(".csv")]
# dfs = {}
# for file in csv_files:
#     file_path = os.path.join(directory_path, file)
#     df = pd.read_csv(file_path, low_memory=False)
#     dfs[file] = df


# --------------------------------------------------------------------------------------------------------- #


































































