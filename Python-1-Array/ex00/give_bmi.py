import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Use array to use numpy, calcul bmi and return result into list"""

    # Input validation
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Parameters must be lists")
    if not all(isinstance(v, (int, float)) for v in height):
        raise TypeError("The values in 'height' must be int or float")
    if not all(isinstance(v, (int, float)) for v in weight):
        raise TypeError("The value in 'weight' must be int or float")
    if len(height) != len(weight):
        raise TypeError("Parameters must have same size")

    # Give bmi
    np_height = np.array(height)
    np_weight = np.array(weight)
    bmi = np_weight / (np_height ** 2)  # '**' for power

    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Use array to use numpy, check if bmi > limit and return bool list"""

    # Input validation
    if not isinstance(bmi, list) or not isinstance(limit, int):
        raise TypeError("Parameters must be one list and one int")
    if not all(isinstance(v, (int, float)) for v in bmi):
        raise TypeError("The values in bmi must be int or float")

    # Apply limit
    np_bmi = np.array(bmi)
    result = np_bmi > limit  # Compare bmi with limit and return bool array

    return result.tolist()
