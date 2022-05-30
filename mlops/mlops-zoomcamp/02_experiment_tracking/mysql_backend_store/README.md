# MySQL Backend Store for MLflow
This is the setup for a simple MySQL docker container, which has the propose to serve as the backend store for the MLflow interface for the model registry capability, in this docker container is going to be saved the entities of the experiments that are performed in the lifecycle of the project.

This container have a database name `mlflow_entities_db`, which is going to be the one that is going to be used as the backend store of the model registry capability of MLflow.

To run this container the following command have to be used:
```bash 
docker-compose up
```