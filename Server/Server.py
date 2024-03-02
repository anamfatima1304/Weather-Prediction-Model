from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)

@app.route('/get_Summary', methods=['GET'])
def get_Summary():
    response = jsonify({
        'Summary': util.get_Summary(),
        'Precip_Type' : util.get_Precip_Type()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

# @app.route('/', methods=['GET'])
# def get_Precip_Type():
#     response = jsonify({
#         'Precip_Type': util.get_Precip_Type()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')

#     return response

@app.route('/predict_weather', methods=['POST','GET'])
def predict_weather():
    # Humidity = float(request.form['Humidity'])
    # Wind_Speed = float(request.form['Wind_Speed'])
    # Wind_Bearing = float(request.form['Wind_Bearing'])
    # Visibility = float(request.form['Visibility'])
    # Pressure = float(request.form['Pressure'])
    # hour = float(request.form['hour'])
    # month = float(request.form['month'])
    # Summary = request.form['Summary']
    # Precip_Type = request.form['Precip_Type']

    # response = jsonify({
    #     'estimated_temperature': util.get_estimated_temperature(Humidity,Wind_Speed,Wind_Bearing,Visibility,Pressure,hour,month,Summary,Precip_Type)
    # })
    response = jsonify({
        'estimated_temperature': util.get_estimated_temperature(0.89, 3.9284, 204.0, 14.9569, 1015.94, 2, 4, "Summary_Mostly Cloudy","Precip Type_rain")
    })
    # response = request.form
    response.headers.add('Access-Control-Allow-Origin', '*')

    # return response
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Weather Prediction...")
    util.load_saved_artifacts()
    app.run()