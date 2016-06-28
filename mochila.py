from visual import * # must import visual or vis first
from visual.graph import *	# import graphing features 
from random import *


def generar_poblacion(valor,peso):
	crom = [0,0,0,0,0,0,0,0,0,0]
	peso_crom = 0
	while(1):
		rand = randrange(0, 10)
		if(crom[rand] == 0):
			crom[rand] = 1
			peso_crom+=valor[rand]
			if(peso_crom>peso):
				crom[rand] = 0
				peso_crom -= valor[rand]
				print peso_crom, crom
				return crom

def obtener_valor(valor,individuo):
	val = 0
	for pos in range(len(individuo)):
		if(individuo[pos]==1):
			val+=valor[pos]
	return val

def obtener_peso(peso,individuo):	
	pes = 0
	for pos in range(len(individuo)):
		if(individuo[pos]==1):
			pes+=peso[pos]
	return pes


def mejor_individuo(valor,peso, poblacion):
	mejor_valor = -1
	pes = 0
	peso_final = 0
	mejor_indi 	= []
	for indi in range(len(poblacion)):
		suma_valor = valor[indi] 
		pes = obtener_peso(peso, poblacion[indi])
		if (suma_valor > mejor_valor):
			mejor_valor = suma_valor
			mejor_indi 	= indi
			peso_final = pes
	return (mejor_valor,peso_final,poblacion[mejor_indi],mejor_indi)

def obtener_valores(techo, peso, valor, lista_poblacion):
	valores = []
	for ind in lista_poblacion:
		val = 0
		we = 0
		for crom in range(len(ind)):
			if(ind[crom] == 1):
				val += valor[crom]
				we += peso[crom]
		if (we>techo):
			val = 0
		valores.append(val)
		print ind, val
	return valores

def mutacion_individuo(mejor, valor, peso ,lista_poblacion):
	pos = randrange(0, len(lista_poblacion))
	while(pos==mejor):
		pos = randrange(0, len(lista_poblacion))
	individuo = lista_poblacion[pos]
	pos_mutacion = randrange(0, len(individuo))
	if(individuo[pos_mutacion]==0):
		individuo[pos_mutacion] = 1
	else:
		individuo[pos_mutacion] = 0
	lista_poblacion[pos] = individuo


def mutacion_poblacion(mejor, valor, peso ,lista_poblacion):
	for individuo in range(len(lista_poblacion)):
		if(individuo != mejor):
			pos_mutacion = randrange(0, len(lista_poblacion[individuo]))
			if(lista_poblacion[individuo][pos_mutacion]==0):
				lista_poblacion[individuo][pos_mutacion]= 1
			else:
				lista_poblacion[individuo][pos_mutacion] = 0

def media(lista):
	suma = 0
	for elem in lista:
		suma += elem
	return suma / len(lista)

#Variables(objetos, valor y pesos)
#Valor  	= [12,15,10,8,4,14,7,6,2,9]
#Peso 	= [10,13,20,16,12,7,6,10,2,5]
Valor = [67,15,33,75,81,44,17,72,91,16]
Peso = [47,43,44,35,33,36,24,49,41,29]
grafica = []
Valores = []
suma = 0
for a in Valor:
	suma += a
print "Suma: ",suma
Peso_mochila 	= 80
N_objetos 		= len(Valor)
Poblacion_inicial = 6
lista_poblacion = []
cont = 0
# Generando la poblacion
while(cont < Poblacion_inicial):
	string = generar_poblacion(Peso, Peso_mochila)
	crom = []
	for i in string:
		crom.append(i)
	lista_poblacion.append(crom)
	cont+=1
med = 0
i = 0
mejor_genenraciones = (-10,0,[])
while(i<5000):
	valores = obtener_valores(Peso_mochila, Peso, Valor,lista_poblacion)
	print valores
	med = media(valores)
	tupla = mejor_individuo(valores,Peso, lista_poblacion)
	if (mejor_genenraciones[0]<tupla[0]):
		mejor_genenraciones = tupla
	mutacion_individuo(tupla[3],Valor, Peso ,lista_poblacion)
	i+=1	
	grafica.append((med, tupla[0]))
	print "--------------------------------"

print "El mejor invididuo  en todas la generaciones fue : ", mejor_genenraciones[2], " con un peso de : ", mejor_genenraciones[1], " y con un valor de:",mejor_genenraciones[0]

f1 = gcurve(color=color.cyan)# a graphics curve 
f2 = gcurve(color=color.red)
tiempo = 0 
#for x in arange(0, 8.05, 0.1):	# x goes from 0 to 8
while(tiempo < len(grafica)):
	f1.plot(pos=(tiempo,grafica[tiempo][0]))
	f2.plot(pos=(tiempo,grafica[tiempo][1]))
	tiempo += 1
