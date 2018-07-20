import paho.mqtt.client as mqtt
import ssl

rootca = r'C:\\Users\\Prasad\\Desktop\\aws_iot_tutorial\\AmazonRootCA1.pem.txt'
certificate = r'C:\\Users\\Prasad\\Desktop\\aws_iot_tutorial\\260492f7cc-certificate.pem.crt'
key_file = r'C:\\Users\\Prasad\\Desktop\\aws_iot_tutorial\\260492f7cc-private.pem.key'


c = mqtt.Client()
c.tls_set(rootca, certfile=certificate, keyfile=key_file, cert_reqs=ssl.CERT_REQUIRED,
          tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

broker_address = 'a5mphxmdxvg88.iot.ap-south-1.amazonaws.com'
c.connect(broker_address, 8883)
# 1883 port is for mqtt
# 8883 port is for mqtt with ssl (mqtts)


def onc(c, user_data, flags, rc):
    print('Successfully connected to AWS with RC', rc)
    c.subscribe("mytopic/iot")


def onm(c, user_data, msg):
    my_msg = msg.payload.decode()
    print('Message from AWS:', my_msg)  # Message published by AWS IoT
    if my_msg == 'hello':
        c.publish('mytopic/iot', 'Hey AWS, This is Python!')
        # Python is publishing message which will be received by AWS

c.on_connect = onc
c.on_message = onm
c.loop_forever()
