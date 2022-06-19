# Module 02 - Experiment Tracking
In this module of the course is going to be covered the use of the MLflow tool in order to keep track of the experiments in a ML workflow, and also versioning the resulted models using the model registry tool of MLflow.

<p align="center">
  <img src="../assets/imgs/mlflow_logo.png" width=50%/>
</p>

In this module is going to be MLflow to build a ML env in order to make some experiments with the propose of improving the performance of the distance time model that was built in the first module of this course.

The file structure is the following:

```bash
📦 02_experiment_tracking
 ┣ 📂 artifacts # This directory contains all the serialize models (artifacts)
 ┃ ┣ 📜 README.md
 ┣ 📂 mysql_backend_store # Setup of the MySQL docker container
 ┃ ┣ 📂 db
 ┃ ┃ ┣ 📜 create_db_schema.sql
 ┃ ┃ ┗ 📜 refresh_root_config.sql
 ┃ ┣ 📜 README.md
 ┃ ┗ 📜 docker-compose.yml
 ┣ 📂 notebooks # This directory contains the notebooks used in this module
 ┃ ┗ 📜 homework.ipynb
 ┣ 📂 scripts # This directory contains of the useful scripts to run this project
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 get_path_dir.py
 ┃ ┣ 📜 hpo.py
 ┃ ┣ 📜 preprocess_pipeline.py
 ┃ ┣ 📜 register_model.py
 ┃ ┗ 📜 train.py
 ┣ 📜 README.md
 ┗ 📜 setup.py
```

Before start executing the different scripts and notebooks of this module it is necessary to first setup the MySQL docker container that going to be used as the backend store of the MLflow model registry capability.

To setup correctly this container refer to [mysql_backend_store](mysql_backend_store/README.md).

After setting up the MySQL docker container, the tracking local server of MLflow can be launch using the container as the backend store using the following command:

```bash 
mlflow server --backend-store-uri mysql+mysqldb://root:root@127.0.0.1/mlflow_entities_db --default-artifact-root <artifacts_root_dir>
```
