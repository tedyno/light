
import  RPi.GPIO as GPIO
import time
buttonPin=26 #set pin of button GPIO
lightPin=17 #set pin of light GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(lightPin,GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN,pull_up_down=GPIO.PUD_UP)
status=1 

while True:
    inputValue = GPIO.input(buttonPin)
    if (inputValue == False): 
        if(status == 1):
                status=0
                GPIO.output(lightPin,GPIO.HIGH)
        else:
                status=1
                GPIO.output(lightPin,GPIO.LOW)
    time.sleep(0.3) #this waits for button to press and then sets the light on or off



