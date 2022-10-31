from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
import json
import sys
sys.path.insert(0, '/home/100071/Inscribing_API/build')
import geocoordinates

def inscribingFunction(inscribingInput):
    radius = inscribingInput['radius']
    length = inscribingInput['length']
    width = inscribingInput['width']
    points = geocoordinates.inscribe(radius, length, width)
    coordinates = []
    for point in points:
        coordinates.append([point.x, point.y])
    numberOfCircles = len(coordinates)
    inscribingOutput = {
        'numberOfCircles':numberOfCircles,
        'coordinates':coordinates,
    }
    return inscribingOutput

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def functionInputs(request):
    if request.method == 'POST':
        radius=float(request.POST['radius'])
        length=int(request.POST['length'])
        width=int(request.POST['width'])
        inscribingInput = {
            'radius':radius,
            'length':length,
            'width':width,
        }
        inscribingOutput = inscribingFunction(inscribingInput)
        return JsonResponse(inscribingOutput)
    else:
        return HttpResponse("Method Not Allowed")

@csrf_exempt
def inscribingAPI(request):
    if (request.method=="POST"):
        inscribingInput=json.loads(request.body)
        inscribingOutput=inscribingFunction(inscribingInput)
        return JsonResponse (inscribingOutput)
    else:
        return HttpResponse("Method Not Allowed")
