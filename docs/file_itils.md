## File Utility Module

The `file_utils.py` file contains a utility function, `copy_file_with_prompt`, for copying files with user prompt for overwriting. Here's a brief overview of its method:

- `copy_file_with_prompt(src_file: str, dst_file: str, force: bool = False)`: Copies a file from source to destination, prompting the user if the destination file already exists. If `force` is set to `True`, it overwrites the destination file without prompting.

Example usage:

```python
from file_utils import copy_file_with_prompt

# Copy a file with user prompt for overwriting
copy_file_with_prompt("source.txt", "destination.txt")

# Copy a file and overwrite without prompting
copy_file_with_prompt("source.txt", "destination.txt", force=True)