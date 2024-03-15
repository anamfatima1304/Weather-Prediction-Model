

function onClickedEstimateTemperature() {
  console.log("Estimate Temperature button clicked");
  var Humidity = document.getElementById("in1");
  var Wind_Speed = document.getElementById("in2");
  var Wind_Bearing = document.getElementById("in3");
  var Visibility = document.getElementById("in4");
  var Pressure = document.getElementById("in5");
  var hour = document.getElementById("in6");
  // var months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"];
  var month = document.getElementById("Month");
  // month = (months.indexOf(month))+1;
  var Summary = document.getElementById("weather_summary");
  var Precip = document.getElementById("Precip");

  // var url = "http://127.0.0.1:5000/predict_weather"; 

  var output = {Humidity: parseFloat(Humidity.value), Wind_Speed: parseFloat(Wind_Speed.value), Wind_Bearing: parseFloat(Wind_Bearing.value), Visibility: parseFloat(Visibility.value), Pressure: parseFloat(Pressure.value), hour: parseFloat(hour.value), month: parseFloat(month.value),Summary: Summary.value, Precip_Type: Precip.value};

    console.log(output);
  const content = JSON.stringify(output);
  const blob = new Blob([content], { type: 'text/plain' });
  const url = window.URL.createObjectURL(blob);

  const link = document.createElement('a');
  link.href = url;
  link.download = "Weather_Prediction_Variable_File.txt";
  link.click();

  // Revoke object URL to avoid memory leaks
  window.URL.revokeObjectURL(url);

  var url2 = "http://127.0.0.1:5000/predict_weather"; 
    $.get(url2,function(data, status) {
      console.log("got response for predict_weather request");
      if(data) {
          var Summary_data = data.estimated_temperature;
          console.log(data.estimated_temperature);
          estTemperature.innerHTML = "<h2>" + data.estimated_temperature.toString() + " °C</h2>";
      }
  });
  // $.post(url, JSON.stringify({
  //   Humidity: parseFloat(Humidity.value),
  //   // Wind_Speed: parseFloat(Wind_Speed.value),
  //   // Wind_Bearing: parseFloat(Wind_Bearing.value),
  //   // Visibility: parseFloat(Visibility.value),
  //   // Pressure: parseFloat(Pressure.value),
  //   // hour: parseFloat(hour.value),
  //   // month: parseFloat(month.value),
  //   // Summary: Summary.value,
  //   // Precip_Type: Precip.value
  // }),function(data, status) {
  //     console.log(data.estimated_temperature);
  //     stTemperature.innerHTML = "<h2>" + data.estimated_temperature.toString() + " °C</h2>";
  //     console.log(status);
  // });
}

function onPageLoad() {
  console.log( "document loaded" );
  // var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  var url = "http://127.0.0.1:5000/get_Summary"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_Summary request");
      if(data) {
          var Summary_data = data.Summary;
          var Summary = document.getElementById("weather_summary");
          $('#weather_summary').empty();
          for(var i in Summary_data) {
            var n = Summary_data[i];
              n = n.slice(8);
              var opt = new Option(n);
              $('#weather_summary').append(opt);
          }

          var Precip_data = data.Precip_Type;
          var Precip = document.getElementById("Precip");
          $('#Precip').empty();
          for(var i in Precip_data) {
              var n = Precip_data[i];
              n = n.slice(12);
              var opt = new Option(n);
              $('#Precip').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;
