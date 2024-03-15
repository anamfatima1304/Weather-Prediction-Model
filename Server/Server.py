from flask import Flask, request, jsonify, render_template
import util
import ast
import os

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

@app.route('/predict_weather', methods=['GET','POST'])
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
    file_path = "C:/Users/HP/Downloads/Weather_Prediction_Variable_File.txt";
    file_path2 = "C:/Users/HP/Downloads/Weather_Prediction_Variable_File (1).txt";
    file_path3 = "C:/Users/HP/Downloads/Weather_Prediction_Variable_File (1).txt";
    if os.path.exists(file_path2):
        print("File Path Removed.")
        os.remove(file_path)
        os.rename(file_path2, file_path)
    with open(file_path, "r") as file:
    # Read the file content
        data_string = file.read()

    # Convert the string to a dictionary using ast.literal_eval (caution advised)
        data_dict = ast.literal_eval(data_string)

    response = jsonify({
        'estimated_temperature': util.get_estimated_temperature(data_dict['Humidity'], data_dict['Wind_Speed'],data_dict['Wind_Bearing'],data_dict['Visibility'],data_dict['Pressure'],data_dict['hour'],data_dict['month'],data_dict['Summary'],data_dict['Precip_Type'])
    })

    if os.path.exists(file_path3):
        print("File Path Removed.")
        if(os.path.exists(file_path2)):
            os.remove(file_path2)
        os.rename(file_path3, file_path2)
    # response = jsonify({
    #     'estimated_temperature': util.get_estimated_temperature(0.89, 3.9284, 204.0, 14.9569, 1015.94, 2, 4, "Summary_Mostly Cloudy","Precip Type_rain")
    # })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Weather Prediction...")
    util.load_saved_artifacts()
    app.run()
