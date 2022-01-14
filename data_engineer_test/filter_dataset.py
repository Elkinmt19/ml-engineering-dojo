# Built-in imports
import os
import sys

# My Own imports
import get_path_dataset_folder as gpaf

# Get dataset folder in repo for the samples
DATASET_FOLDER = gpaf.get_dataset_folder_path()

def get_path_file(file):
    path_dataset_file = os.path.join(
        DATASET_FOLDER,
        file
    )

    return path_dataset_file

def main():
    # Get the lines of the original dataset file
    with open(get_path_file("USvideos.csv"), 'r', encoding="utf8") as f:
        lines = f.readlines()
        f.close()

    # Create a new file with just the important data
    with open(get_path_file("USvideos_clean.csv"), "w", encoding="utf8") as f:
        for line in lines:
           if (line[0:2] != r"\n" and len(line) > 200):
                f.write(line)



if __name__=='__main__':
    sys.exit(main())