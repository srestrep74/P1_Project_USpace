#Importar librerias
import RPi.GPIO as IO   
import time

#Etiquetado de pines
LED = 10
SW1 = 5


#Constantes
TIME = 0.5

#Configuracion
IO.setmode(IO.BOARD)    
IO.setup(LED,IO.OUT)
IO.setup(SW1,IO.IN)

#RunTime
while True:
    print(IO.input(SW1))
    if IO.input(SW1):
        IO.output(LED,True)#(led, 1)    
        time.sleep(TIME)
    else:
        IO.output(LED,False)
