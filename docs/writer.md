## Writer Module

The `writer.py` file contains a utility function, `write_file_with_prompt`, for writing content to files with user prompt for overwriting. Here's a brief overview of its method:

- `write_file_with_prompt(file_path: str, content: str, force: bool = False)`: Writes the given content to a file at the given path. If the file already exists and `force` is not set to `True`, the user is prompted to confirm whether they want to overwrite it.

Example usage:

```python
from writer import write_file_with_prompt

# Write to a file with user prompt for overwriting
write_file_with_prompt("file.txt", "Hello, World!")

# Write to a file and overwrite without prompting
write_file_with_prompt("file.txt", "Goodbye, World!", force=True)