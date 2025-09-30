import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Print old and new shape, slice list and return new list"""

    # Input validation
    if not isinstance(family, list):
        raise TypeError("Parameter 'family' must be list")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("Parameter 'family' must be 2D array")
    row_size_list = [len(row) for row in family]
    if not all(i == row_size_list[0] for i in row_size_list):
        raise ValueError("All rows in 'family' must be same size")

    # Print and slice part
    family_array = np.array(family)
    print("My shape is :", family_array.shape)
    slice_family_array = family_array[start:end]  # ':' to slice
    print("My new shape is :", slice_family_array.shape)

    return slice_family_array.tolist()  # Return list
