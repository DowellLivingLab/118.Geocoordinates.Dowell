import os

import pandas as pd

def unevenCartesian(uneven_centre, cartesian_centre):
    """
    Align the cartesian plane centre to the uneven shape centre
    """
    # find the coordinates to shift the origin
    shift_point = tuple(map(lambda i, j: i - j, uneven_centre, cartesian_centre))

    coordinates = pd.read_excel(os.path.abspath("DATA.xlsx"))
    coordinates = [(x,y) for x, y in zip(coordinates["Lat"], coordinates["Long"])]

    print("{}\n".format(coordinates[:10]))

    print("{}\n".format("-" * 80))

    # shift the coordinates within cartesian plane
    new_coordinates = list()

    for coordinate in coordinates:
        new_coordinate = tuple(map(lambda i, j: i + j, shift_point, coordinate))
        new_coordinates.append(new_coordinate)

    print("{}\n".format(new_coordinates[:10]))

    new_centre = uneven_centre

    return new_centre

print(unevenCartesian(uneven_centre=(2.5, 2.7), cartesian_centre=(1, -1)))