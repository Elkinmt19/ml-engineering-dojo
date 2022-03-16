""" SCRIPT TO GET "SPECIFIC" FOLDER BASED ON REPOSITORY STRUCTURE """

# Built-int imports
import os


def get_directory_folder_path(directory):
    # Directory folder is located 1 directories up (double parent dir)
    PROJECT_FOLDER = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), os.path.pardir
        )
    )

    PROJECT_FOLDER_PATH = os.path.abspath(
        os.path.join(PROJECT_FOLDER, directory)
    )
    return PROJECT_FOLDER_PATH


if __name__ == "__main__":
    print(get_directory_folder_path("assets"))