# 118.Geocoordinates.Dowell

## Calling Inscribing API

import json

import requests

url = 'http://100071.pythonanywhere.com/api/'

data={

  'radius': 0.5,      # Radius should be a float value
  
  'length': 1000,     # Length should be a natural number 
  
  'width': 1000,      # Width should be a natural number 

}

headers = {'content-type': 'application/json'}

response = requests.post(url, json =data,headers=headers)

output_data=json.loads(response.text)

print(output_data)
