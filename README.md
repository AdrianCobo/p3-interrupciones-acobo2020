# P3-Interrupciones

## (CC-BY-NC-SA) Adrián Cobo Merino

El objetivo de este esta práctica es tener la primera toma de contacto con las intorrupciones y con los botones.

### Ejercicio1

En el ejercicio 1,he correjido el problema del rebote añadiendo una condición booliana como flag y para resolver el problema de finalizar 
el programa con control+c no he podido hacerlo de ninguna otra forma que no fuese sustituir el while true por un hilo,lo que haria de mi 
programa una copia del código ofrecido como ejemplo en interruptionEvent.py. Igualmente he usado en mi ejercicio los metodos signal.signal()
y signal.pause() ofrecidos en el programa interrupcionEvent.py ya que me di cuenta que si haces control+c y pulsas el botón, el programa se
detiene,y añadiendo esas funciones,lo hace de una forma mas correcta y te puede hacer un apaño

```python
def callbackSalir (senial, cuadro): # señal y estado cuando se produjo la interrup.
    GPIO.cleanup () # limpieza de los recursos GPIO antes de salir
    sys.exit(0)
#.
#.
#.

signal.signal(signal.SIGINT, callbackSalir) # callback para CTRL+C que limpia todos los hilos anteriores
signal.pause()
```

### Ejercicio2

El esquema de los gpios utilizados es el mismo para los 3 programas y se intuye en: 

```python
GPIO.setmode(GPIO.BCM)
pulsadorGPIO1 = 16
pulsadorGPIO2 = 21
ledGPIO1=20
ledGPIO2=12
```

Para el programa sinInterrupcionesMejorado.py, hemos modificado el programa sinInterrupciones.py para que al pulsarse un boton cambie 
la salida de un pin que va a estar conectado a un led. Una vez conseguido esto,tan solo hay que duplicar el código para que podamos 
controlar otro led usando otro botón, y crear las condiciones booleanas que nos van a permitir que los leds se puedan controlar de forma
independiente.Además el programa es capaz de dejar encendido los leds solo mientras se estna pulsando los botones.

Para el programa InterrupcionesMejorado.py nos damos cuenta de que al solo tener un hilo, el procesador solo va a estar pediente del 
pulsador que le corresponda con el metodo GPIO.wait_for_edge, y hasta que no haya hecho algo ese botón, lo que haga el otro le va a dar 
igual y no va a avanzar más en el programa hasta que no reciba una señal del pulsador del que está pendiente.

Finalmente para el programa interrupcionEventMejorado.py, utilizamos eventos que encenderan o apagaran el led en funcion del valor de unas 
variables globales. Me he visto obligado a utilizar este método ya que solo podemos tener un evento por GPIO y no pueden retornar valores.

como curiosidad, descubrí como pasar parámetros a los eventos:

```python
def evento(parametro):


GPIO.add_event_detect(pulsadorGPIO1, GPIO.FALLING,callback=lambda x:evento(parametro), bouncetime=500)
```

**Importante: antes de usar estos programa ejecuta el programa GPIOCLEANUP.py para limpiar los GPIOS**

Si quieres ver un video de demostracion del programa sinInterrupcionesMejorado.py, 
pulsa [aqui](https://drive.google.com/file/d/1aWFSqJxfIakVRPgp6kce8qWLPtNMSFMa/view?usp=sharing).
Se hace dificil grabar y pulsar botones a la vez:=)

Si quieres ver un video de demostracion del programa interrupcionEventMejorado.py.py, 
pulsa [aqui](https://drive.google.com/file/d/13j78xTz0Fby131z2q_GzcOzyOOIfTptj/view?usp=sharing).

Para cualquier duda: <a.cobo.2020@alumos.urjc.es>
