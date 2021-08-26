import logging
import os
import pickle
import zipfile


def create_folder(directory):
    """Creates a data folder if it doesn't exist.

    Returns:
        None
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info("Data folder created.")
    else:
        logging.info("Data folder already existed.")


def check_execution_path():
    """Check if the function and therefore all subsequent functions
        are executed from the root of the project
    Returns:
        boolean -- returns False if execution path isn't the root,
            otherwise True
    """
    file_name = "Makefile"
    if not os.path.exists(file_name):
        logging.error(
            "Don't execute the script from a sub-directory. "
            "Switch to the root of the project folder"
        )
        return False
    return True


def extract_file(directory, extension=".zip"):
    """Extract compress file.

    Args:
        directory (str): Path to directory
        extension (str, optional): Extension of compress file. Defaults to ".zip".
    """
    input_path = os.path.join(os.getcwd(), directory)
    os.chdir(input_path)
    for item in os.listdir(input_path):
        if item.endswith(extension):
            file_name = os.path.abspath(item)
            zip_ref = zipfile.ZipFile(file_name)
            zip_ref.extractall(input_path)
            zip_ref.close()
            os.remove(file_name)
    print("Finish processing data!")


def save_model(model):
    pickle.dump(model, open("model.pkl", "wb"))
