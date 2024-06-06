import pandas as pd 
import numpy as np

def evaluate_lower_possibility(alternative_data:pd.Series, possibility_function_definitions:dict) -> np.array:

    possibility_values = np.zeros((alternative_data.size, 1))

    for index, criteria in enumerate(alternative_data.index.values):
        criteria_val = alternative_data[criteria]

        # If the value is smaller than the lower turning point, it is automatically one
        #since it is in the const part of the possibility function
        if criteria_val <= possibility_function_definitions['x3'][criteria]:
            possibility_values[index] = 1
            continue

        # Otherwise it is necessary to calculate the y value from the x = criteria_val in the 
        #line that represents the possibility function of the form y = ax + b
        a = 1 / (possibility_function_definitions['x4'][criteria] - possibility_function_definitions['x3'][criteria])
        b = -1 * possibility_function_definitions['x4'][criteria] * criteria_val
        possibility_values[index] = a*criteria_val + b

    return possibility_values