import cv2
import RPi.GPIO as GPIO
import socket
import RPi
import math
import time
import struct
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm1=GPIO.PWM(11,50)
pwm1.start(7.5)
GPIO.setup(8,GPIO.OUT)
pwm2=GPIO.PWM(8,50)
pwm2.start(7.5)
UDP_IP = "192.168.43.216"
UDP_PORT = 5050
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
video_capture = cv2.VideoCapture(0)
sock.bind((UDP_IP,UDP_PORT))
while   True:
    data,addr=sock.recvfrom(1024)
    data1 = data.decode("utf-8")
    data2 = str(data1)
    a = data2.index(',')
    data2 = data2+"*"
    b = data2.rfind(',')
    c = data2.index('*')
    azu = abs(float(data2[0:a])-200)
    roll = abs(float(data2[b+1:c]))
    duty1=float(azu)/10+2.5 
    pwm1.ChangeDutyCycle(duty1)
    time.sleep(0.00000000002)
    duty2=float(roll)/10+2.5
    pwm2.ChangeDutyCycle(duty2)
    time.sleep(0.00000000002)
    print(azu, "                  ",roll)
    _,frame = video_capture.read()
    cv2.imshow('video',frame)
    if cv2.waitKey(1):
        continue
    video_capture.release()
    cv2.destroyAllWindows()

