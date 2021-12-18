from picamera import PiCamera
from time import sleep

def photo(param1, param2):
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture(f'/photos/{param1}{param2}.jpg')
    camera.stop_preview()
    return None