# P3-Interrupciones

## (CC-BY-NC-SA) Adrián Cobo Merino

El objetivo de este esta práctica es tener la primera toma de contacto con las intorrupciones y con los botones.

###Ejercicio1

En el ejercicio 1,he correjido el problema de,rebote añadiendo una condicion boliana y para resolver el problema de finalizar el programa con control+c no he podido hacerlo de ninguna otra forma
que no fuese sustituir el while true por un hilo,lo que haria de mi programa una copia del codigo ofrecido como ejemplo en interruptionEvent.py.

Igualmente he usado en mi ejercicio los metodos signal.signal() y signal.pause() ya que me di cuenta que si haces control+c y pulsas el boton, el programa se detiene,y añadiendo esas funciones,
lo hace de una forma mas correcta y te puede hacer un apaño

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

###Ejercicio2

Para el programa sinInterrupcionesMejorado.py, hemos modificado el programa sinInterrupciones.py para que al pulsarse un boton cambie 
la salida de un pin que va a estar conectado a un led. Una vez conseguido eso,tan solo hay que duplicar el codigo para que podamos 
controlar otro led usando otro boton, y crear las condiciones booleanas que nos van a permitir que los leeds se puedan controlar de forma
independiente.

*Importante*:antes de usar este programa ejecuta el programa GPIOCLEANUP.py para limpiar los GPIOS

Para cualquier duda: <a.cobo.2020@alumos.urjc.es>
