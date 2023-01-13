from machine import Pin, ADC # analog bemenete 0 tol 4095 ig intervallumba van
import time

tarolo = Pin(21,Pin.OUT)   # világitunk ezzel a koddal az első szám a lábnak az idexét mondja

pipi = ADC(Pin(34,Pin.IN))

while True:
    #print(pipi.read())
    time.sleep(0.5)
    print(pipi.read())
    if pipi.read() >= 2000:
        tarolo.value(1)
    else:
        tarolo.value(0)
