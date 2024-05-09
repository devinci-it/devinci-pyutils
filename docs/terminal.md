## Terminal Utility Module

The `terminal.py` file contains a utility class, `TerminalUtility`, for printing formatted messages and headers in the command-line interface. Here's a brief overview of its methods:

- `header(title: str)`: Prints a formatted header with the specified title. The title is displayed in bright white text color.

- `info(message: str)`: Prints an informational message with a prefixed INFO label. The message is displayed in cyan color.

- `warning(message: str)`: Prints a warning message with a prefixed WARNING label. The message is displayed in yellow color.

- `error(message: str)`: Prints an error message with a prefixed ERROR label. The message is displayed in red color.

- `success(message: str)`: Prints a success message with a prefixed SUCCESS label. The message is displayed in green color.

All methods are static, so they can be called directly from the class without creating an instance of it.