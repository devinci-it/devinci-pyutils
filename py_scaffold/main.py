import os
import argparse
from helpers import camel_case, snake_case, format_class_name,format_parent_class
from template_hydrator import generate_content


def create_nested_directories(class_name, package):
    """Create nested directories if needed and return the file name."""
    if '.' in class_name:
        nested_path = os.path.join(*class_name.split('.')[:-1])
        package_name = snake_case(class_name.split('.')[-1])
        os.makedirs(nested_path, exist_ok=True)
        if package:
            file_name = os.path.join(nested_path, package_name , f"{package_name}.py")
            os.makedirs(os.path.join(nested_path, package_name), exist_ok=True)
            return file_name, os.path.join(nested_path, package_name,'__init__.py'), package_name
        else:
            return os.path.join(nested_path, f"{package_name}.py"), None, None
    else:
        if package:
            package_name = snake_case(class_name)
            os.makedirs(package_name, exist_ok=True)
            return os.path.join(package_name,
                                f"{package_name}.py"), os.path.join(
                package_name, '__init__.py'), package_name
        else:
            return f"{snake_case(class_name)}.py", None, None


def write_to_file(file_name, content):
    """Write the content to the class file."""
    with open(file_name, 'w') as file:
        file.write(content)


def create_init_file(init_file_name, class_name, package_name):
    """Create __init__.py with import statement."""
    init_file_content = f"from .{package_name} import {class_name}\n"
    with open(init_file_name, 'w') as init_file:
        init_file.write(init_file_content)


def create_class_file(class_name, parent_class=None, package=False,
                      attributes=None):
    class_name = format_class_name(class_name)
    parent_class = format_parent_class(parent_class)
    content = generate_content(class_name, parent_class, attributes or [])
    file_name, init_file_name, package_name = create_nested_directories(
        class_name, package)

    write_to_file(file_name, content)
    if init_file_name and package_name:
        create_init_file(init_file_name, class_name, package_name)

    print(f"Class file '{file_name}' has been created successfully.")


def main():
    parser = argparse.ArgumentParser(
        description="Generate a scaffolded Python class file.")
    parser.add_argument("class_name",
                        help="The name of the class to create, possibly with nested package path.")
    parser.add_argument("parent_class", nargs="?",
                        help="The parent class to inherit from (optional).")
    parser.add_argument("--package", action="store_true",
                        help="Create a package instead of a single module.")
    parser.add_argument("--attributes", nargs="*",
                        help="List of attributes for the class (optional).")
    args = parser.parse_args()

    create_class_file(args.class_name, args.parent_class, args.package,
                      args.attributes)


if __name__ == "__main__":
    main()
