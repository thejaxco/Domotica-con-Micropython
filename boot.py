# Complete project details at https://RandomNerdTutorials.com

try:
  import usocket as socket
except:
  import socket

import network
from machine import Pin
import dht

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Cisco03222'
password = ''

station = network.WLAN(network.STA_IF)
station.ifconfig(('10.199.160.229', '255.255.255.0', '10.199.160.254', '212.0.97.81'))
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Estas conectado en:')
print(station.ifconfig())

#sensor = dht.DHT22(Pin(14))
sensor = dht.DHT11(Pin(13))