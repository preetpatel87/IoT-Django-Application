import json
# from urllib import request
from django.shortcuts import render
from django.template import RequestContext
from dashboard.models import Mode, State
from rest_framework import viewsets,request
from dashboard.serializers import ModeSerializer, StateSerializer

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def lights(request):
    return render(request,"lights.html")

class ModeViewSet(viewsets.ModelViewSet):
    queryset = Mode.objects.all()
    serializer_class = ModeSerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

def home(request):
    print(dir(request))
    print(request.POST)
    print(request.body)
    if 'on' in request.POST:
        values = {"name": "on"}
        r=request.put('http://127.0.0.1:8000/state/1/', data=values, auth=('username', 'password'))
        result=r.text
        output = json.loads(result)
        out=output['name']
    if 'off' in request.POST:
        values = {"name": "off"}
        r=request.Request.put('http://127.0.0.1:8000/state/1/', data=values, auth=('username', 'password'))
        result=r.text
        output = json.loads(result)
        out=output['name']
    if 'auto' in request.POST:
        values = {"name": "auto"}
        r=request.Request.put('http://127.0.0.1:8000/mode/1/', data=values, auth=('username', 'password'))
        result=r.text
        output = json.loads(result)
        out=output['name']
    if 'manual' in request.POST:
        values = {"name": "manual"}
        r=request.Request.put('http://127.0.0.1:8000/mode/1/', data=values, auth=('username', 'password'))
        result=r.text
        output = json.loads(result)
        out=output['name']
    
    r=request.Request.get('http://127.0.0.1:8000/mode/1/', auth=('username', 'password'))
    result=r.text
    output = json.loads(result)
    currentmode=output['name']
    r=request.Request.get('http://127.0.0.1:8000/state/1/', auth=('username', 'password'))
    result=r.text
    output = json.loads(result)
    currentstate=output['name']

    return render('lights.html',{'r':out, 'currentmode':currentmode, 'currentstate':currentstate}, context_instance=RequestContext(request))
