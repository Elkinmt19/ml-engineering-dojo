# Module 03 - Orchestration
In this module of the MLOps ZoomCamp is going to be covered the use of the `prefect` python tool on order to manage and orchestrate the ML workflows of the ML pipelines.

<p align="center">
  <img src="../assets/imgs/prefect_logo.png" width=60%/>
</p>

The file structure is the following:

```bash
📦 03-orchestration
 ┣ 📂 artifacts # This directory contains all the serialize models (artifacts)
 ┃ ┣ 📜 README.md
 ┣ 📂 notebooks # This directory contains the notebooks used in this module
 ┃ ┗ 📜 homework.ipynb
 ┣ 📂 scripts # This directory contains of the useful scripts to run this project
 ┃ ┣ 📜 get_path_dir.py
 ┃ ┗ 📜 training_fhv_model.py
 ┗ 📜 README.md
```

Prefect is going to be used as the workflow orchestration tool to build the ML projects with the best practices of the MLOps culture.

In order to spin up a local prefect server the following command has to be use:
```bash 
prefect orion start
```
This will start a local server a port 4200 of prefect having all the information related two the flow runs and more features.

To see te env variables of aur own installation of prefect, we need to use the following command:
```bash 
prefect config view
```
One of the most important env variables that we are going to work with a lot is the `PREFECT_ORION_UI_API_URL` which tells prefect where it should point at in every flow run.

In order to change the value of this env variable we need to used the following commands:
```bash 
prefect config unset PREFECT_ORION_UI_API_URL # To unset the env variable

prefect config set PREFECT_ORION_UI_API_URL="http://<external-ip>:4200/api" # To set the env variable, to use an external server like an ec2 instance
```
Another useful feature of prefect is the ability to manage storages in order to save the information about the flow runs, to see the configuration anf the list of storages define in our prefect installation, the following command is needed:
```bash 
prefect storage ls
```
This is and important step, because if this is not done, then the information about the flow runs won't be saved. To create and config a storage for prefect we need to use the following command:
```bash 
prefect storage create 
```
```text
Found the following storage types:
0) Azure Blob Storage
    Store data in an Azure blob storage container.
1) File Storage
    Store data as a file on local or remote file systems.
2) Google Cloud Storage
    Store data in a GCS bucket.
3) Local Storage
    Store data in a run's local file system.
4) S3 Storage
    Store data in an AWS S3 bucket.
5) Temporary Local Storage
    Store data in a temporary directory in a run's local file system.
```
There are some options to define a storage for prefect, we just have to use one.

One important functionality of prefect is the ability to deploy and program schedule jobs in order to create and run workflows automatically, in order to deploy this kind of jobs we first need to define a python script defining an `DeploymentSpec` prefect object and then use the following command:
```bash
prefect deployment create <python_script_file> # This is the python scripts where the <DeploymentSpec> was define
```
Now that the deployment has been setup and programmed we need an agent to run the workflows, for this are use the `work-queue`, this can be created using the following command:
```bash 
prefect work-queue create <work-queue-name> --params
```