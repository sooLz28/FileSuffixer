import sys
import os
import shutil
from pathlib import Path

# Get all arguments (excluding script name)
arguments = sys.argv[1:]  # sys.argv[0] is the script name

print("Arguments:", arguments)

# Example: Access specific arguments
if len(arguments) == 2:

    files_path = arguments[0]
    file_extension = arguments[1]
    print(f"First argument: {files_path}, Second argument: {file_extension}")

    files = os.listdir(files_path)

    print(files)
    if os.path.exists("output") == False:
        os.mkdir("output")

    for f in files:
        src_file_fullpath = os.path.join(files_path,f)
        dist_file_fullpath = os.path.join("output",f)
        shutil.copy(src_file_fullpath,"output")
        p = Path(dist_file_fullpath)
        p.rename(p.with_suffix(f'.{file_extension}'))
    


