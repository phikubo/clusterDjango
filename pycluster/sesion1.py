import time
print('Sesion 1')
print('--------')
print('')

cad="curso django"
edad=22
decim=28.9
estado=True
lista=[1,3,5,'cuatro'] #lista
tupla=(1,3,5,'cuatro') #tupla

#Diferencias en la funcionalidad. La tupla se crea y es innmutable.
#Esto es, no se puede modificar la tupla

'''como python es dinamico puedo re asignar el tipo de dato
solo cambiado el valor de la variable'''

cad=10 #cambio el dato.
print("Variable re definida", type(cad))


#Diccionario.

dic={'clave': 'valor', 'clave2':'valor2', edad:'Variable edad existe'}
print(dic)


#programa para entrar a discoteca.

edad1=17
edad2=18
'''if edad1 >17:
    print("Acceda")
else:
    if edad2==18:
        print("Feliz cumpleaños edad2")
    print("Sáquese soquete")'''


#CONDICION
if edad1 >17:
    print("Acceda")
elif edad2==18:
    print("Feliz cumpleaños edad2")
print("Sáquese soquete")

#WHILE
condicion=0
while condicion!=5:
    #condicion+=1
    print("hola cluster por "+str(condicion)+ " vez, desde el while")
    condicion+=1
    time.sleep(1)
    #break
    #continue

#FOR
for i in range(5,10,1):#empieza en 5 hasta 10, de incrementos de a 1
    print("hola cluster por "+str(i)+ " vez, desde el for")
    time.sleep(1)


'''La diferencia entre el recorrido es que el while lo hace desde 1
y el for inicio desde el 0, si se coloca el aumento desde el inicio del while.'''


for elemento in lista:
    print("Elementos: ", elemento)










print("Fin del programa")