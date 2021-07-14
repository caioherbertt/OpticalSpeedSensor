import random
import pyrebase
random.seed(2)

config = {
  "apiKey": "AIzaSyAW4RY8ttu7Sqyv2ZfpPD6NoTn1s1Cd2h4",
  "authDomain": "opticalspeedsensor.firebaseapp.com",
  "databaseURL": "https://opticalspeedsensor-default-rtdb.firebaseio.com/",
  "storageBucket": "opticalspeedsensor.appspot.com"
}
firebase = pyrebase.initialize_app(config)
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)
pin_to_circuit = 7
 
def rc_time (pin_to_circuit):
    count = 0
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(pin_to_circuit, GPIO.IN)
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1
 
    return count
 
#Catch when script is interupted, cleanup correctly
try:
    # Main loop
    while True:
        a = (rc_time(pin_to_circuit)*5/65536)
        print(a)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
db = firebase.database()
dado1 = "432432"
dado = random.random()
db.child("Sensor2").child("Medida").push(a)
