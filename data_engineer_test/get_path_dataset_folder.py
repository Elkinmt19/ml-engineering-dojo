# Built-int imports
import os


def get_dataset_folder_path():
    # Dataset folder which is in the same level of the file
    WORK_FOLDER = os.path.abspath(
        os.path.dirname(__file__)
    )

    DATASET_FOLDER_PATH = os.path.abspath(
        os.path.join(WORK_FOLDER, "dataset")
    )
    return DATASET_FOLDER_PATH


if __name__ == "__main__":
    print(get_dataset_folder_path())