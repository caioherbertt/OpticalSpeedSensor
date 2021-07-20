import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)
pin_to_circuit = 7
 
while True:
    count = 0
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(pin_to_circuit, GPIO.IN)
    currentTime = time.time()
    diff = 0

    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        diff = time.time() - currentTime

    tensao = diff * 5 / 65536
    print(tensao) 
    time.sleep(1)
