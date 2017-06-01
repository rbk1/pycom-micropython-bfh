# _boot.py -- always run on boot-up, even during safe boot
import os
from machine import UART
from network import WLAN
from time import sleep_ms
#UART(1, 115200)
#UART(2, 115200)
os.dupterm(UART(0, 115200))
wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid='WiFi-T204', auth=(WLAN.WPA2, '112233445566778899AABBCCDD'))
while not wlan.isconnected():
    sleep_ms(50)
print(wlan.ifconfig())
