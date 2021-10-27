#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import signal
import sys

pulsadorGPIO1 = 16
pulsadorGPIO2 = 21
ledGPIO1=20
ledGPIO2=12

def callbackSalir (senial, cuadro): # señal y estado cuando se produjo la interrup.
    GPIO.cleanup () # limpieza de los recursos GPIO antes de salir
    sys.exit(0)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsadorGPIO1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(pulsadorGPIO2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.setup (ledGPIO1, GPIO.OUT)
    pwm = GPIO.PWM(ledGPIO1,100)
    pwm.start (0)

    GPIO.setup (ledGPIO2, GPIO.OUT)
    pwm2 = GPIO.PWM(ledGPIO2,100)
    pwm2.start (0)
    time.sleep(0.1)

    pulsado1 = False #variable antirrebote
    pulsado2 = False
    while True:

        GPIO.wait_for_edge(pulsadorGPIO1, GPIO.BOTH)
        if not pulsado1:
            time.sleep(0.1)
            pwm.ChangeDutyCycle(100)
            pulsado1 = True
            time.sleep(0.1)
        else:
            pulsado1 = False
            pwm.ChangeDutyCycle(0)
            time.sleep(0.1)

        GPIO.wait_for_edge(pulsadorGPIO2, GPIO.BOTH)
        if not pulsado2:
            time.sleep(0.1)
            pwm2.ChangeDutyCycle(100)
            pulsado2 = True
            time.sleep(0.1)
        else:
            pulsado2 = False
            pwm2.ChangeDutyCycle(0)
            time.sleep(0.1)

        signal.signal(signal.SIGINT, callbackSalir)
        time.sleep(0.1)#liberamos el procesador