import serial
import time
arduino = serial.Serial('COM3', 9600, timeout=.1)
time.sleep(5)

while True:
    SERIALDATA= arduino.readline() #Read line of text from Arduino
    SERIALDATA2= SERIALDATA.decode()
    pyVALUE1= SERIALDATA2.split(';')[0] #Splits the line of text into array of strings composed of each individual sensor data
    pyVALUE2= SERIALDATA2.split(';')[1]
    pyVALUE3= SERIALDATA2.split(';')[2]
    if SERIALDATA:
        f = open('C:\sample.txt', 'w')
        f.write ('outHumidity=')
        s = pyVALUE1
        f.write (s)
        f.write('\n')
        f.write ('outTemp=')
        s = pyVALUE2
        f.write (s)
        f.write('\n')
        f.write ('heatIndex=')
        s = pyVALUE3
        f.write (s)
        f.close()
    time.sleep(2)
