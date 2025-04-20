import sys
import os
import shutil
from pathlib import Path

# Get all arguments (excluding script name)
arguments = sys.argv[1:]  # sys.argv[0] is the script name

if len(arguments) != 2:
    print("Usage: python change_to_single_suffix.py <directory_path> <file_extension>")
    sys.exit(1)

files_path = arguments[0]
file_extension = arguments[1].lstrip('.')  # Remove leading dot if provided

# Validate the directory path
if not os.path.isdir(files_path):
    print(f"Error: The directory '{files_path}' does not exist.")
    sys.exit(1)

# Validate the file extension
if not file_extension.isalnum():
    print(f"Error: Invalid file extension '{file_extension}'.")
    sys.exit(1)

# Get the list of files in the directory
files = os.listdir(files_path)
if not files:
    print(f"Error: The directory '{files_path}' is empty.")
    sys.exit(1)

# Create the output directory inside the input directory
output_dir = os.path.join(files_path, "output")
os.makedirs(output_dir, exist_ok=True)

# Process each file
for file_name in files:
    src_file_fullpath = os.path.join(files_path, file_name)

    # Skip directories and the output directory itself
    if os.path.isdir(src_file_fullpath) or file_name == "output":
        continue

    dist_file_fullpath = os.path.join(output_dir, file_name)
    shutil.copy(src_file_fullpath, output_dir)

    # Rename the file with the new extension
    p = Path(dist_file_fullpath)
    p.rename(p.with_suffix(f'.{file_extension}'))

print(f"All files have been processed and saved in the '{output_dir}' directory.")