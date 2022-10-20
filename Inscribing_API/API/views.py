from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
import json
import ctypes
import glob

def inscribingFunction(inscribingInput):
    radius = inscribingInput['radius']
    length = inscribingInput['length']
    width = inscribingInput['width']
    libfile = glob.glob('/home/100071/118.Geocoordinates.Dowell/Inscribing_API/API//build/*/algorithm*.so')[0]
    mylib = ctypes.CDLL(libfile)
    mylib.inscribe.restype = ctypes.c_int
    mylib.inscribe.argtypes = [ctypes.c_float, ctypes.c_int, ctypes.c_int]
    numberOfCircles = mylib.inscribe(radius, length, width)
    inscribingOutput = {
        'numberOfCircles':numberOfCircles,
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
