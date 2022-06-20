# This is a simple bash scripts that setup the dependencies of this repo.
# 1: Upgrade the version of pip.
# 2: Download the pipenv tool to manage the dependencies and virtual envs of this repo.

export REPO_NAME="ml-engineering-dojo"
export REPO_AUTHOR="Elkin Javier Guerra Galeano"

echo "Setting up the $REPO_NAME by $REPO_AUTHOR as $USER..."

python3 -m pip install --upgrade pip

pip install pipenv

echo "The setup is completed!!!"