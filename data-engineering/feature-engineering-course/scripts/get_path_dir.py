# Built-int imports
import os

def get_desired_folder_path(dir):
    # Desired folder is located 1 directories up (double parent dir)
    PROJECT_DIR = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), os.path.pardir
        )
    )

    DESIRED_FOLDER_PATH = os.path.abspath(
        os.path.join(PROJECT_DIR, dir)
    )
    return DESIRED_FOLDER_PATH


if __name__ == "__main__":
    print(get_desired_folder_path("data"))
