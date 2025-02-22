# SuffixSwap

A collection of Python tools for modifying file suffixes within a folder. Choose the appropriate script for your needs – either automatically restoring the default file extension based on MIME type or applying a single, user-specified extension to all files.

## Repository Structure

```
.
├── change_to_default_suffix.py
├── change_to_single_suffix.py
└── output/           # Created automatically by the scripts
```

## Requirements

- **Python 3.x**
- **Modules:**
  - [python-magic](https://github.com/ahupp/python-magic) (for detecting file MIME types in `change_to_default_suffix.py`)
  - Built-in modules: `os`, `sys`, `shutil`, `pathlib`, `mimetypes`

To install the third-party module, run:

```bash
pip install python-magic
```

## Usage

### `change_to_default_suffix.py`

This script reads all files from a specified folder, determines each file's MIME type, guesses the appropriate extension, and then copies the file into an output directory with the new extension.

**Command-line usage:**

```bash
python change_to_default_suffix.py <folder_path>
```

**Example:**

```bash
python change_to_default_suffix.py /path/to/your/files
```

**What it does:**

- Reads the list of files from the provided folder.
- Uses `python-magic` and `mimetypes` to determine the default extension based on MIME type.
- Copies each file into an `output` directory and renames it with the detected extension.

---

### `change_to_single_suffix.py`

This script applies a single, user-defined file extension to every file in a given folder. It copies each file into an output directory, then renames the file using the extension you specify.

**Command-line usage:**

```bash
python change_to_single_suffix.py <folder_path> <extension>
```

**Example:**

```bash
python change_to_single_suffix.py /path/to/your/files txt
```

**What it does:**

- Reads all files from the provided folder.
- Copies each file into an `output` directory.
- Renames each file to have the extension provided (e.g., `.txt`).

---

## Notes

- The scripts automatically create an `output` directory if it does not exist.
- Make sure you have read permissions for the input folder and write permissions for the directory where `output` will be created.
- If a file's MIME type cannot be determined in `change_to_default_suffix.py`, the script will print an error message.

## Contributing

Contributions, bug reports, and feature requests are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---

Feel free to customize the README further to suit your project's style and additional details.
