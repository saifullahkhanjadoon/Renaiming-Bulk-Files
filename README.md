# Renaming Bulk Files

This Python script, `renaiming_bulk_files.py`, renames all the files in a specified directory in bulk. It assigns new names to the files in the format "famX.jpg" where "X" is a unique number. This is particularly useful for organizing or standardizing file names in a folder.

## Key Features:
- Renames all files in a specified directory (`E:/Pictures/New`) to a sequential format (e.g., fam0.jpg, fam1.jpg, etc.).
- Automates the process of renaming files in bulk.
- Uses `os.rename()` to change the filenames.

## Technologies Used:
- Python
- `os` library to interact with the file system and rename files.

## Usage Instructions:
1. Install Python 3.x on your system.
2. Modify the `path` variable in the script to point to your desired folder.
3. Run the script `renaiming_bulk_files.py`.
4. The files in the specified folder will be renamed to the format "famX.jpg", where X is a number starting from 0.
