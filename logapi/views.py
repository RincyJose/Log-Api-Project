import imp
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LogSerializer
from .models import log
import requests
import json

# Create your views here.
@api_view(['GET'])
def ShowAll(request):
    messages = log.objects.all()
    serializer = LogSerializer(messages, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def CreateLog(request):
    serializer = LogSerializer(data=request.data)
    data = request.data
    title = data['title']
    message=data['message']
    
    if serializer.is_valid():
        serializer.save()
        
    url = "https://fcm.googleapis.com/fcm/send"

    payload = json.dumps({
    "notification": {
    "title": title,
    "body": message,
    "vibration": 1,
    "sound": 1
    },
    "to": "/topics/Alerts"
    })
    headers = {
  'Authorization': 'key=AAAAWCVwZOk:APA91bFHbtDc1gNKhDwJdQfeEgvtXErqn16kcX7aAFSCiIr2haNZQGHOobVUPEAPKDFugY6MRSlI7I6pmk5xtvhc_F-KZB80eDEJYRHAIxB0aV1RyltYaYAM4nhBUNHUfD9xYnh-klBj',
  'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    
    return Response(serializer.data)