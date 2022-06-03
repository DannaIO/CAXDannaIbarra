'''hola

#print (mensaje): permite mandar informacion a la pantalla

print('hola')
print('saludines')
print(5)
print(5+5)

#constantes son datos que no CAMBIAN

dia=4
print('dia')

pi=3.24
print('pi')

#variables son datos que PUEDEN o NO ccambiar

calificacion=6
calificacion=calificacion+2

print(calificacion)

#print mas bonito

print('tu calificacion es:', calificacion)
print('hoy es', dia, 'de enero')
print(pi, 'es el valor de pi que usaremos')

#operadores matematicos # + suma, - restar, * multiplicar, / division

a=2
b=3

print(a+b)
print(a-b)
print(a*b)
print(b/a)
print(a+b*b)

#jerarquia de operaciones (parentesis), potencias, multiplicaciones, sumas

#loop: se refiere a cualquier codigo que se pueda calca o repetir n numero de veces

#while: mientras una condicion ocurra (o no) se ejecuta todo el codigo dentro de la misma

tomate=2 

#operadores logicos
#a>b a es mayor que b
#a<b a es menor que b
#a==b a es identico a b

while(tomate>0):
  print('hay tomate')
  tomate=tomate-1

#identacion y estas nos dice que lineas perteneces a un ciclo o condicion, puede ser un simple espacio o un tab

#while true es una condicion que pregunta si se puede ejecutar, si respondes que si el codigo funciona

while True:
  print('hola')'''

#input(): nos permite ingresar informacion al codigo desde la consola, se debe presionar enter una vez que termines

#nombre es una variable por que puede cambiar si se ejecuta de nuevo 

nombre=input()
print('saludos', nombre)

apellido=input('apellido:')
print('saludos mr.', apellido)