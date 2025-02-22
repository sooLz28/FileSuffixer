import sys
import os
import shutil
from pathlib import Path
import os
import magic
# import filetype
import mimetypes

# Get all arguments (excluding script name)
arguments = sys.argv[1:]  # sys.argv[0] is the script name

print("Arguments:", arguments)

def restore_extension(file_path):
    # # Detect file type
    # mime = magic.Magic(mime=True)
    # file_type = mime.from_file(file_path)

    # # Detect file type
    # kind = filetype.guess(file_path)
    
    # if kind is None:
    #     print(f"Could not determine file type for: {file_path}")
    #     return  # Exit function if file type is unknown
    
    # default_extension = "." + kind.extension  # Ensure extension starts with a dot
    # More accurate detection with python-magic
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(file_path)

    # Guess the correct extension
    default_extension = mimetypes.guess_extension(file_type)



    if default_extension:
        dist_file_fullpath = os.path.join("output",f)
        shutil.copy(file_path,"output")
        p = Path(dist_file_fullpath)
        p.rename(p.with_suffix(f"{default_extension}"))
    
    else:
        print("Could not determine file type.")

# Example: Access specific arguments
if len(arguments) == 1:

    files_path = arguments[0]
    print(f"First argument: {files_path}")

    files = os.listdir(files_path)

    print(files)
    if os.path.exists("output") == False:
        os.mkdir("output")

    for f in files:
        restore_extension(os.path.join(files_path,f))
    
