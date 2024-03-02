import pickle
import json
import numpy as np

__Summary = None
__Precip_Type = None
__data_columns = None
__model = None

def get_estimated_temperature(Humidity,Wind_Speed,Wind_Bearing,Visibility,Pressure,hour,month,Summary,Precip_Type):
    try:
        loc_index1 = __data_columns.index(Summary.lower())
    except:
        loc_index1 = -1
    
    try:
        loc_index2 = __data_columns.index(Precip_Type.lower())
    except:
        loc_index2 = -1

    x = np.zeros(len(__data_columns))
    x[0] = Humidity
    x[1] = Wind_Speed
    x[2] = Wind_Bearing
    x[3] = Visibility
    x[4] = Pressure
    x[5] = hour
    x[6] = month
    if loc_index1>=0:
        x[loc_index1] = 1
    if loc_index2>=0:
        x[loc_index2] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __Summary 
    global __Precip_Type 

    with open("./Server/Artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __Summary = __data_columns[7:20] 
        __Precip_Type = __data_columns[20:] 

    global __model
    if __model is None:
        with open('./Server/Artifacts/weather_prediction.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_Summary():
    return __Summary

def get_Precip_Type():
    return __Precip_Type

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    # print(get_Summary())
    # print(get_Precip_Type())
    print(get_estimated_temperature(0.89, 3.9284, 204.0, 14.9569, 1015.94, 2, 4, "Summary_Mostly Cloudy","Precip Type_rain"))