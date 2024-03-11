import paho.mqtt.client as paho
import time
import ssl

ret_val=''

def on_connect(client, userdata, flags, rc):
    print('Broker Hivemq Connected')
    client.subscribe([("sensors/t1",2),("sensors/t2",1),("sensors/t5",0)])
    

def on_subscribe(client, userdata, mid, granted_qos):
   print("Subscribed: "+str(mid)+" "+str(granted_qos))
    

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    
    global ret_val
    ret_val=str(msg.qos) + " "+str(msg.payload)
    #client.disconnect()

client_id = "spt-client-02"
client = paho.Client(client_id=client_id, clean_session=True)
client.username_pw_set('cosminB', 'ze03b05rA')
client.tls_set(certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED)

client.on_connect=on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect('cc015d965352455a97e2a60fe921c2c3.s1.eu.hivemq.cloud', 8883,keepalive=60,)

client.loop_forever()

#client.disconnect()