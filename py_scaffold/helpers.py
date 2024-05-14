def camel_case(s):
    """Converts a string to CamelCase."""
    return ''.join(word.capitalize() for word in s.split('_'))

def snake_case(s):
    """Converts a string to snake_case."""
    return ''.join(['_' + i.lower() if i.isupper() else i for i in s]).lstrip('_')

def format_class_name(class_name):
    """Ensure the class name is in CamelCase."""
    return camel_case(class_name.split('.')[-1])

def format_parent_class(parent_class):
    """Format the parent class string."""
    return f"({parent_class})" if parent_class else ""
