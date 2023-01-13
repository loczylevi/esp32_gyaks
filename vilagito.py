from machine import Pin
import time

tarolo = Pin(21,Pin.OUT)   # világitunk ezzel a koddal az első szám a lábnak az idexét mondja
lab = Pin(34,Pin.IN, Pin.PULL_UP) # PULL_UP az aktivál beépitet felhuzo ellenálást

while True:
    #time.sleep(0.5)
    #tarolo.value(not tarolo.value()) #beállitunk
    if lab.value() == False: #vizsgálunk
        tarolo.value(1)
    else:
        tarolo.value(0)
    
     
