#!/usr/bin/env python3

import signal
import sys
import RPi.GPIO as GPIO

pulsadorGPIO = 16

def callbackSalir (senial, cuadro): # señal y estado cuando se produjo la interrup.
    GPIO.cleanup () # limpieza de los recursos GPIO antes de salir
    sys.exit(0)

def callbackBotonPulsado (canal):
    print("El boton se ha pulsado")

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsadorGPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(pulsadorGPIO, GPIO.FALLING,
      callback=callbackBotonPulsado, bouncetime=500) # expresado en ms.

    signal.signal(signal.SIGINT, callbackSalir) # callback para CTRL+C que limpia todos los hilos anteriores
    signal.pause() # esperamos por hilo/callback CTRL+C antes de acabar para que no se acabe solo el principal
