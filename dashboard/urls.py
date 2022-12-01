from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('lights/', views.lights, name='light')
    path('mqttRequest/',views.publish, name='publish')
]