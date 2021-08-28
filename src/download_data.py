import logging

import requests

from src.utils import check_execution_path
from src.utils import create_folder
from src.utils import extract_file

DATASET_URL = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/creditcard.csv.zip"

# Initial local dataset location
LOCAL_FILE_NAME = "data/wine_quality.csv.zip"


def download_dataset(url=DATASET_URL, filename=LOCAL_FILE_NAME):
    print(f"Downloading from {url} to {filename}")
    response = requests.get(url)

    with open(filename, "wb") as file:
        file.write(response.content)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Started download script")
    directory = "data"

    if check_execution_path():
        create_folder(directory=directory)
        download_dataset()
        extract_file(directory=directory)

    logging.info("Finished download script")
