import os

# Define the path
file_path = r"C:\path\to\your\file.txt"

# Check if the path exists
if os.path.exists(file_path):
    print(f"The path exists: {file_path}")
else:
    print(f"The path does not exist: {file_path}")
