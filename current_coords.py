import serial
import pynmea2

def getCoords():

    port = "/dev/ttyAMA0"
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)
    dataout = pynmea2.NMEAStreamReader()
    newdata = ser.readline()

    if newdata == "$GPGLL":
        newmsg = pynmea2.parse(newdata)
        lat = str(newmsg.latitude)
        lng = str(newmsg.longitude)

    return [lat, lng]