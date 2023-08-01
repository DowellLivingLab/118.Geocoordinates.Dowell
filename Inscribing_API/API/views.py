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

@csrf_exempt
def publicAPI(request):
    if (request.method=="POST"):
        inscribingInput=json.loads(request.body)
        if "api_key" in inscribingInput:
            api_key = inscribingInput.get('api_key')
            data = processApikey(api_key)
            api_resp = json.loads(data)
            if api_resp['success'] is True:
                credit_count = api_resp['total_credits']
                if credit_count>=0:
                    inscribingOutput=inscribingFunction(inscribingInput)
                    return JsonResponse(inscribingOutput)
                else:
                    JsonResponse({"success":api_resp['success'], "message":api_resp['message'], "total credits":api_resp['total_credits']},status=status.HTTP_400_BAD_REQUEST)
            elif api_resp['success'] is False:
                return JsonResponse({"sucesss":False, "message":api_resp['message'], "total credits":api_resp['total_credits']},status=status.HTTP_200_OK)

        else:
            return JsonResponse({"success":False, "msg":"Provide a valid API key"},status=status.HTTP_403_FORBIDDEN)

    else:
        return HttpResponse("Method Not Allowed")
