import datetime

dia= datetime.date.today()

print(dia)

w=dia.weekday()+1

if (w==0):
  print('feliz domingo')

elif (w==2):
  print('ehh es martes')

else:
  print('yay es sabado')

if(w==0):
  print('feliz lunes')

elif (w==3):
  print('eee es jueves')

else:
  print('wuuu ya casi es miercoles')

if (w==0):
  print('se aproxima el viernes')