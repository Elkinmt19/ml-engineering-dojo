# Module 04 - Deployment
In this module of the MLOps ZoomCamp is going to be covered the different ways of deployment a model into production environments, in order to achieve this goal is going to be used Docker as the containerization tool.

<p align="center">
  <img src="../assets/imgs/docker-kubernetes.png" width=70%/>
</p>

The file structure is the following:

```bash
📦 04_deployment
 ┣ 📂 notebooks # This directory contains the notebooks used in this module
 ┃ ┣ 📜 homework.ipynb
 ┃ ┗ 📜 ride-duration-prediction.ipynb
 ┣ 📂 scripts # This directory contains of the useful scripts to run this project
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 get_path_dir.py
 ┃ ┣ 📜 ride-duration.py.py
 ┃ ┗ 📜 ride_prediction_prd.py
 ┣ 📜 Dockerfile # Dockerfile to build the docker image of the model
 ┣ 📜 Pipfile
 ┣ 📜 Pipfile.lock
 ┗ 📜 README.md
```

There are different ways of deploy a Machine Learning model, the most popular are:

- Batch
- Streaming 
- Web Service

Based on the context and the application the ML model is deploy using one way or another, the **batch** approach is used when there is not a need of making predictions so often, this deployment is perfect when the predictions are made following a schedule like every year or every month. The **streaming** approach is used in real-time applications, and finally the **web service** approach is used when is needed an event based Machine Learning model.

## Built and deploy the model 
In order to be able to do all the tasks of the module, it is necessary to have docker installed in the local machine.

To build the docker image that is going to be used to spins up the container of the application the following command have to be used:
```bash
docker build -t mlops/zoomcamp/ride_prediction:<tag> <Dockerfile-path>
```
To execute the model to make predictions the following command have to be use:
```bash 
docker run --rm mlops/zoomcamp/ride_prediction:<tag> -y <year> -m <month>
```