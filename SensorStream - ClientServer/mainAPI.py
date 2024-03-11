
import paho.mqtt.client as paho
import time
import ssl
from flask import Flask
app = Flask(__name__)

ret_val=''
data_count=0
expected_count=0
client_id = "spt-client-02"


def on_connect(client, userdata, flags, rc):
    print('Broker Hivemq Connected')
   
    

def on_subscribe(client, userdata, mid, granted_qos):
   print("Subscribed: "+str(mid)+" "+str(granted_qos))
    

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    
    global ret_val
    global data_count
    
    #Append data to ret_val
    ret_val=ret_val+str(msg.topic) + " "+str(msg.payload)+" | "
    data_count=data_count+1
    if data_count>=expected_count:
        client.disconnect()


@app.route('/api/test/', methods=['GET', 'POST'])
def welcome():
    return "Ready for command!"


@app.route('/api/sensors/<string:sensors>/', methods=['GET'])
def sensors(sensors):
    
    global ret_val
    global data_count
    global expected_count
    data_count=0
    expected_count=0
    ret_val=''
    print("Reading sensors ["+sensors+"]...")
    
    topics=sensors.split(",");
    
    topics_arr=[]
    #Build the subscrube list
    j=0
    for x in topics:
       tpl=("sensors/"+x,j)
       topics_arr.append(tpl)
       j=j+1
       expected_count=j  
    print(topics_arr)
    
   
    #call broker client
    client_id = "spt-client-02"
    client = paho.Client(client_id=client_id, clean_session=True)
    client.username_pw_set('cosminB', 'ze03b05rA')
    client.tls_set(certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED)

    client.on_connect=on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    client.connect('cc015d965352455a97e2a60fe921c2c3.s1.eu.hivemq.cloud', 8883,keepalive=60)
    client.subscribe(topics_arr, qos=1)
    client.loop_forever()
    while data_count<j   :
        time.sleep(1)
    return ret_val    
        
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)