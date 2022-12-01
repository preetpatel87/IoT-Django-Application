import json
# from urllib import request
from django.shortcuts import render
from django.template import RequestContext
from dashboard.models import Mode, State
from rest_framework import viewsets,request
from dashboard.serializers import ModeSerializer, StateSerializer
from mqtt_test.mqtt import client as mqtt_client

# Create your views here.
from django.http import HttpResponse


def on_connect(mqtt_client, userdata, flags, rc):
   if rc == 0:
       print('Connected successfully')
       mqtt_client.subscribe('django/mqtt')
   else:
       print('Bad connection. Code:', rc)

def on_message(mqtt_client, userdata, msg):
   print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)

def index(request):
    return render(request,"index.html")

def lights(request):
    print(request.POST)
    return render(request,'lights.html',{'currentmode':'auto', 'currentstate':'on'})

def publish(request):
    modeObject = Mode.objects.all()
    print(modeObject)
    # rc, mid = mqtt_client.publish(request_data['topic'], request_data['msg'])
    # return JsonResponse({'code': rc})

class ModeViewSet(viewsets.ModelViewSet):
    queryset = Mode.objects.all()
    serializer_class = ModeSerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

def home(request):
    out=""
    if 'on' in request.POST:
        values = {"name": "on"}
        r=request.put('https://ventilation-system-dashboard-ndrgz.ondigitalocean.app/state/1/', data=values)
        result=r.text
        output = json.loads(result)
        out=output['name']
    if 'off' in request.POST:
        values = {"name": "off"}
        r=request.put('https://ventilation-system-dashboard-ndrgz.ondigitalocean.app/state/1/', data=values)
        result=r.text
        output = json.loads(result)
        out=output['name']
    if 'auto' in request.POST:
        values = {"name": "auto"}
        r=request.put('https://ventilation-system-dashboard-ndrgz.ondigitalocean.app/mode/1/', data=values)
        result=r.text
        output = json.loads(result)
        out=output['name']
    if 'manual' in request.POST:
        values = {"name": "manual"}
        r=request.put('https://ventilation-system-dashboard-ndrgz.ondigitalocean.app/mode/1/', data=values)
        result=r.text
        output = json.loads(result)
        out=output['name']
    r=request.GET.get('https://ventilation-system-dashboard-ndrgz.ondigitalocean.app/mode/1/')
    print(r)
    result=r.text
    output = json.loads(result)
    currentmode=output['name']
    r=request.GET.get('https://ventilation-system-dashboard-ndrgz.ondigitalocean.app/state/1/')
    print(r)
    result=r.name
    output = json.loads(result)
    currentstate=output['name']
    return render(request, 'lights.html',{'r':out, 'currentmode':currentmode, 'currentstate':currentstate}, context_instance=RequestContext(request))