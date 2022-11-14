#We import...
from datetime import *
from plyer import notification
import time

#We ingest data...
Titulo= int(input('Recordar: '))
detalles= int(input('Detalles de la actividad: '))
time= int(input(print('Cuando quieres que te lo Notifique?: ')))
X ='60'
time=time * X
time.split(time)
#This function checks if the time and match, in case YES popup notification is shown.
#When the date and time coincide, the notification will be sent.

def main():
  if time==time:
    notification.notify(print(Titulo), print(detalles))

print(main())