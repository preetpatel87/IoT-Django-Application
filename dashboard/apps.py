from django.apps import AppConfig
# import paho.mqtt.client as mqtt

# def on_connect(mqtt_client, userdata, flags, rc):
#    if rc == 0:
#        print('Connected successfully')
#        mqtt_client.subscribe('/temperature')
#        mqtt_client.publish('/humidity')
#    else:
#        print('Bad connection. Code:', rc)

# def on_message(mqtt_client, userdata, msg):
#    print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')

# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message
# client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
# client.connect(
#     host=settings.MQTT_SERVER,
#     port=settings.MQTT_PORT,
#     keepalive=settings.MQTT_KEEPALIVE
# )

class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'
