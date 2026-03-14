import numpy as np

def calculate_wind_speed(u, v):

    wind_speed = np.sqrt(u**2 + v**2)

    return wind_speed.fillna(0)