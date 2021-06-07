#!/usr/bin/python
import bme680
import time
import sys
import serial
import urllib.request
from picamera import PiCamera
camera = PiCamera()

def getCPM(ser):
    ser.write(b'<GETCPM>>')
    rec = ser.read(2)
    return rec
ser = serial.Serial('/dev/ttyUSB0', 115200)

while True:
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
    sensor.set_humidity_oversample(bme680.OS_2X)
    sensor.set_pressure_oversample(bme680.OS_4X)
    sensor.set_temperature_oversample(bme680.OS_8X)
    sensor.set_filter(bme680.FILTER_SIZE_3)
    sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
    sensor.set_gas_heater_temperature(320)
    sensor.set_gas_heater_duration(150)
    sensor.select_gas_heater_profile
    sensor.get_sensor_data()

    f = open('/var/tmp/datafile', 'w')

    temp = ((sensor.data.temperature/5)*9)+32
    temp = round(temp, 1)

    hum = round(sensor.data.humidity, 1)

    pres = 0.02953 * sensor.data.pressure
    pres = round(pres, 3)

    cpm = getCPM(ser)
    cpm2 = int.from_bytes(cpm, byteorder='big')
    cpm3 = cpm2*0.0065
    cpm4 = round(cpm3, 2)

    f.write ('outTemp=')
    s = str(temp)
    f.write (s)
    f.write('\n')
    f.write ('outHumidity=')
    s = str(hum)
    f.write (s)
    f.write ('\n')
    f.write ('pressure=')
    s = str(pres)
    f.write (s)
    f.write ('\n')
    f.write ('usv=')
    s = str(cpm4)
    f.write (s)
    f.close()

    print("Sensor Data Logged")
    time.sleep(10)
    camera.capture('/home/pi/Desktop/wx.jpg')
    print('Snap')