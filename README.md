
# Weather Prediction Model

Weather Prediction is an important factor. Weather affects a lot of our day-to-day activities. The aim of this project is to create a basic level weather prediction system that would tell the temperature in degree Celsius based on   Humidity,Wind_Speed,Wind_Bearing,Visibility,Pressure,hour, month and Precip_Type. This uses **weather-history.csv** dataset available on Kaggle.

## Technologies 
The **weather prediction project** follows a step-by-step procedure to build an interactive model to predict the weather based on the given output. The following technologies are used in the project:

- **Python**
- **Numpy and Pandas for data cleaning**
- **Matplotlib for data visualization**
- **Sklearn for model building**
- **Jupyter notebook and visual studio code as IDE**
- **Flask for Server**
- **HTML/CSS/Javascript for UI**

The **Weather_Prediction.ipynb** implements various Algorithms on the data. These Algorithms include:

- **LinearRegression**
- **Lasso**
- **Decision_Tree**

After comparing the result of all these algorithms, **Decision_Tree** seems to be the most suitable Algorithm. The **Decision_Tree** overfitted since it gave 0.0 error on training data so used the **min_samples_leaf** method to reduce the overfitting. The accuracy of our training model is **93.0%**. The accuracy of our testing  model is **90.0%**.

The Flask server is written in the **Server** folder. The GUI developed using HTML, CSS and Javascriptare present in the **Client** folder.





## Deployment

To use the project, run the following command in the folder where you want to get the project.

```bash
  https://github.com/anamfatima1304/Weather-Prediction-Model.git
```
Now play around with the model and enjoy.


## Installation

To run this project, you should have python istalled on your computer. You might also need an IDE like VSCode that could run the flask server on locat host and host the website too. Also install the following packages

```bash
  pip install pandas
  pip install numpy
  pip install seaborn
  pip install sklearn
  pip install matplotlib
  pip install flask
```
    
## Code Guide

Import the following packages

```bash
  import pandas as pd
  import numpy as np
  import seaborn as sns
  from matplotlib import pyplot as plt
  %matplotlib inline
  import matplotlib
  matplotlib.rcParams["figure.figsize"] = (20,10)
  from sklearn.model_selection import train_test_split
  from sklearn.linear_model import LinearRegression
  from sklearn.metrics import mean_squared_error
  from sklearn.tree import DecisionTree
```

Now let's move to read the dataset
```bash
  df = pd.read_csv("weatherHistory.csv")
  
```
After reading the data, we will apply use pandas and nupy to clean the data. After cleaning, the data will be in the form to apply the machine learning algorithms.

Now, after the data is in its processed form, its time to apply the Algorithms. the Next part applies all the Algorithms and save their error and number of mis-classified Examples in the text file.

In the last part the model and column names are stored in .pickle and .json file respectively. 

```bash
  import pickle
  with open('weather_prediction.pickle', 'wb') as f:
    pickle.dump(model, f)
```

Also, writing the columns in .json file.

```bash
  import json
  columns = {
    'data_columns' : [col.lower() for col in X.columns]
  }
  with open("columns.json","w") as f:
    f.write(json.dumps(columns))
```

Then, comes the part where we would create the flask server that would serve as a backend for the application. The GUI is written in HTML, CSS and Javascript and is attached t the backend.

To run the front end go to the **Server->Server.py** folder and click run. Then the server will be enabled. Then, go to the **Client->app.html** to run the frontend.



## Errors

The frontend of the model is facing an error yet and is not in the correct form yet. The error is in the flask application. The javascript can get the values from the flask but flask is not accessing the value from javascript. The error encountered is **Error:405** which is method not recognized error and the method I am using is POST method. Note that GET method is recognized correctly. The code used in JS is 

```bash
    $.post(url, JSON.stringify({
    Humidity: parseFloat(Humidity.value),
    Wind_Speed: parseFloat(Wind_Speed.value),
    Wind_Bearing: parseFloat(Wind_Bearing.value),
    Visibility: parseFloat(Visibility.value),
    Pressure: parseFloat(Pressure.value),
    hour: parseFloat(hour.value),
    month: parseFloat(month.value),
    Summary: Summary.value,
    Precip_Type: Precip.value
  }),function(data, status) {
      console.log(data.estimated_temperature);
      stTemperature.innerHTML = "<h2>" + data.estimated_temperature.toString() + " °C</h2>";
      console.log(status);
  });
```
While the one in flask is:

```bash
    Humidity = float(request.form['Humidity'])
    Wind_Speed = float(request.form['Wind_Speed'])
    Wind_Bearing = float(request.form['Wind_Bearing'])
    Visibility = float(request.form['Visibility'])
    Pressure = float(request.form['Pressure'])
    hour = float(request.form['hour'])
    month = float(request.form['month'])
    Summary = request.form['Summary']
    Precip_Type = request.form['Precip_Type']

    response = jsonify({
        'estimated_temperature': util.get_estimated_temperature(Humidity,Wind_Speed,Wind_Bearing,Visibility,Pressure,hour,month,Summary,Precip_Type)
})
```
This isn't working for the time being. So, GUI is also distorted. Once, flask is being able to access the values from js the project wil be in good shape. Any contributions or suggestions on this will be highly appreciable and willl be taken with gratitude,.

## Contributing

Contributions are always welcome!

Find out an Error or give any suggestion to improve the project.

If you want to add any new features, make a pull request.

ThankYou for your attention.
## Errors

The frontend of the model is facing an error yet and is not in the correct form yet. The error is in the flask application. The javascript can get the values from the flask but flask is not accessing the value from javascript. The error encountered is **Error:405** which is method not recognized error and the method I am using is POST method. Note that GET method is recognized correctly. The code used in JS is 

```bash
    $.post(url, JSON.stringify({
    Humidity: parseFloat(Humidity.value),
    Wind_Speed: parseFloat(Wind_Speed.value),
    Wind_Bearing: parseFloat(Wind_Bearing.value),
    Visibility: parseFloat(Visibility.value),
    Pressure: parseFloat(Pressure.value),
    hour: parseFloat(hour.value),
    month: parseFloat(month.value),
    Summary: Summary.value,
    Precip_Type: Precip.value
  }),function(data, status) {
      console.log(data.estimated_temperature);
      stTemperature.innerHTML = "<h2>" + data.estimated_temperature.toString() + " °C</h2>";
      console.log(status);
  });
```
While the one in flask is:

```bash
    Humidity = float(request.form['Humidity'])
    Wind_Speed = float(request.form['Wind_Speed'])
    Wind_Bearing = float(request.form['Wind_Bearing'])
    Visibility = float(request.form['Visibility'])
    Pressure = float(request.form['Pressure'])
    hour = float(request.form['hour'])
    month = float(request.form['month'])
    Summary = request.form['Summary']
    Precip_Type = request.form['Precip_Type']

    response = jsonify({
        'estimated_temperature': util.get_estimated_temperature(Humidity,Wind_Speed,Wind_Bearing,Visibility,Pressure,hour,month,Summary,Precip_Type)
})
```
This isn't working for the time being. So, GUI is also distorted. Once, flask is being able to access the values from js the project wil be in good shape. Any contributions or suggestions on this will be highly appreciable and willl be taken with gratitude,.

