from gpiozero import PWMLED, MCP3008
from time import sleep

ldr = MCP3008(0)

while True:
    print(ldr.value)
