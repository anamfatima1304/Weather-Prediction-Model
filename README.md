
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

