from django.shortcuts import render

# Create your views here.
def find_shape_centre(coordinates):

    coordinates = sorted(coordinates, key=lambda x: x[1])

    x_coordinates = list()
    y_coordinates = list()

    for coordinate in coordinates:
        x_coordinates.append(coordinate[0])
        y_coordinates.append(coordinate[1])

    shape_area = 0

    i = 0
    while i < len(coordinates):
        
        if i == 0:
            area = y_coordinates[i+1] * x_coordinates[i]
            shape_area+=area

        elif i > 0 and i < len(coordinates) - 1:
            area = y_coordinates[i+1] - y_coordinates[i-1]
            area = area * x_coordinates[i]
            shape_area+=area

        elif i == len(coordinates) - 1:
            area = 0 - y_coordinates[i-1]
            area = area * x_coordinates[i]
            shape_area+=area

        i+=1

    shape_area = shape_area/2

    centroid_x_coordinate = 0
    centroid_y_coordinate = 0

    i = i - i
    while i < len(coordinates) - 1:
        centroid_x = (
            x_coordinates[i] + x_coordinates[i+1]) * ((x_coordinates[i] * y_coordinates[i+1]) - (x_coordinates[i+1] * y_coordinates[i])
            )
        
        centroid_x_coordinate+=centroid_x
        i+=1

    i = i - i
    while i < len(coordinates) - 1:
        centroid_y = (y_coordinates[i] + y_coordinates[i+1]) * ((x_coordinates[i] * y_coordinates[i+1]) - (x_coordinates[i+1] * y_coordinates[i]))

        centroid_y_coordinate+=centroid_y
        i+=1

    centroid_x_coordinate = centroid_x_coordinate * 1/(6 * shape_area)
    centroid_y_coordinate = centroid_y_coordinate * 1/(6 * shape_area)

    centroid_x_coordinate = round(centroid_x_coordinate, 2)
    centroid_y_coordinate = round(centroid_y_coordinate, 2)

    centre_coordinates = (centroid_x_coordinate, centroid_y_coordinate)

    return print(centre_coordinates)

find_shape_centre(
    coordinates=[(2.66, 4.71), (5, 3.5), (3.63, 2.52), 
                    (4, 1.6), (1.9, 1), (0.72, 2.28)]
                    )
