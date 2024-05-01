import os
import shutil


def get_current_directory():
    """
    Gets the current working directory path.
    """
    return os.getcwd()

def list_dir_contents(path):
    """
    Returns:
        list: A list of filenames and directory names within the path.
    """
    return os.listdir(path)

def path_exists(path):
    """
    Returns:
        bool: True if the path exists, False otherwise.
    """
    return os.path.exists(path)

def create_directory(path):
  os.makedirs(path, exist_ok=True)  # Handles cases where parent directories don't exist



def delete_directory(path):
  shutil.rmtree(path, ignore_errors=True)  # Handles cases where directory may be empty

