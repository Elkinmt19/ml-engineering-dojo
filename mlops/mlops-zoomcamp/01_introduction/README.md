# Module 01 - Introduction to MLOps 
In this module the basic concepts of Machine learning Operations are explained in order to have a clear knowledge about the content of this course .

First at all, it is used the [NYC taxi dataset](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page) in order to train some models to predict the duration time of a specific taxi ride in NYC, these models are gonna be trained using a single Jupyter notebook with using any other tool to tracking experiments or models.

The file structure is the following:

```bash 
# Files tree of the 01-introduction directory
.
|____models # This directory contains all the serialize models (artifacts)
|____README.md
|____data # This directory contains the .parquet files (dataset)
|____assets # This directory contains some assets
|____notebooks # This directory contains the notebooks used in this module
```

The main goal of this module is to build and train a model in order to add to it the good practices of mlops along the course, starting the next module adding to it the experiment tracking capability using the **mlflow** tool.

## Linear Regression model 
The algorithm used to build and train the model to predict the duration time of a specific taxi ride in NYC was a linear regression algorithm, the residuals plot of the resulted model was the following:

<p align="center">
  <img src="assets/imgs/residuals_plot.png" width=80%/>
</p>

The resulted model doesn't have a great performance how we can see in the residuals plot, in the next modules of the course we are going to improve the performance of this model using the good practices and tools of MLOps.