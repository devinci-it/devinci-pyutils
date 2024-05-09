## Banner Module

The `banner.py` file contains a utility function, `print_banner`, for printing formatted banners in the console. Here's a brief overview of its method:

- `print_banner(text: str, width: int = 80, border_char: str = "#", alignment: str = 'center', newline: bool = True)`: Prints a formatted banner with the specified text. The width of the banner, border character, alignment of the text, and whether to print a newline before and after the banner can be customized.

Example usage:

```python
from banner import print_banner

# Print a centered banner with default width and border character
print_banner("Hello, World!")

# Print a left-aligned banner with custom width and border character
print_banner("Welcome", width=60, border_char="-", alignment="left")

# Print a right-aligned banner without newline
print_banner("Goodbye", width=50, border_char="*", alignment="right", newline=False)