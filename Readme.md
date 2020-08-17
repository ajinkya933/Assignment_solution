# Solution

### Attached is the jupyter notebook 
```
Mumbai Tile: (solution-2.ipynb) 

Crop Tile: (crop_segment.ipynb)

Clouds Tile: (cloud.ipynb)
```
### ML Flow

### SQL table details and running MLflow details are mentioned in PDF stored at mlflow_integration/Mlflow_assignment

Keep all logs of your data on MLflow + MySql(backend) using

``` Assignment_solution/mlflow_integration/mlflow_assignment.ipynb ``` 

### Design considerations before designing MLflow:
```
Parameters (via mlflow.log_param() ). Parameters are variables that you change or tweak when tuning your model.

Metrics (using mlflow.log_metric() ). Metrics are values that you want to measure as a result of tweaking your parameters. - Typical metrics that are tracked can be items like F1 score, RMSE, MAE etc.

Artifacts (using mlflow.log_artifact() ). Artifacts are any other items that you wish to store. Typical artifacts that we can keep track of are pickled models , PNGs of graphs, lists of feature importance variables …
```

Example run:
```
Mumbai tile
    -- run1
    -- run2
```

I change a matric in ML experiment and run that experiment,name this experiment(run1)
whenever I change a metric in experiment it forms a new run

MLflow Dashbord:

![alt text](https://github.com/ajinkya933/Assignment_solution/blob/master/images/dashbord.png)

MLflow Experiment run:

![alt text](https://github.com/ajinkya933/Assignment_solution/blob/master/images/1.png)
![alt text](https://github.com/ajinkya933/Assignment_solution/blob/master/images/2.png)


### Mysql data stored on backend for the above 2 runs:

![alt text](https://github.com/ajinkya933/Assignment_solution/blob/master/images/sql.png)




