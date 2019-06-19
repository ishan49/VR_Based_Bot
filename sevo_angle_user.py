import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
pwm=GPIO.PWM(8,50)
pwm.start(7.5)
y=180
duty1=y/18+2
print(duty1)
try:
    GPIO.output(8,True)
    pwm.ChangeDutyCycle(duty1)
    time.sleep(1)
    GPIO.output(8,False)
    pwm.ChangeDutyCycle(0)
    pwm.stop()
except KeyboardInterrupt:
    GPIO.cleanup()