from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

import pandas as pd

# Create your views here.
def index(request):
    template = "unevenshape/index.html"
    return render(request, template)

def find_shape_area(area):
    shape_area = area/2
    return shape_area

def split_coordinates(coordinates):
    # split the coordinates into x and y
    x_coordinates = list()
    y_coordinates = list()

    for coordinate in coordinates:
        x_coordinates.append(coordinate[0])
        y_coordinates.append(coordinate[1])

    return x_coordinates, y_coordinates

def find_shape_centre(request):
    # access the file temporarily stored
    coordinates_file = request.FILES['filename']

    # uploading file with pandas mainatins constant time complexity
    coordinates_file = pd.read_csv(coordinates_file, header=None)

    # create a tuple of the coordinates from separate columns
    coordinates = [(x,y) for x,y in zip(coordinates_file[0], coordinates_file[1])]

    # sort the coordinates according to the y axis
    coordinates = sorted(coordinates, key=lambda x: x[1])

    x_coordinates = split_coordinates(coordinates)[0]
    y_coordinates = split_coordinates(coordinates)[1]

    # loop through coordinates to calculate area of the boundary
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

    shape_area = find_shape_area(shape_area)

    # loop through to find centroid values
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

    # round off to the nearest 2 dp
    centroid_x_coordinate = round(centroid_x_coordinate, 2)
    centroid_y_coordinate = round(centroid_y_coordinate, 2)

    centre_coordinates = (centroid_x_coordinate, centroid_y_coordinate)

    return HttpResponse(centre_coordinates)