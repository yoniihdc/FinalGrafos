#Importacion de libreías
import networkx as nx				#Librería para la creación de gráfos, en el programa se utilizará como "nx"
import matplotlib.pyplot as plt		#Librería para desplegar el diagrama de Hasse

#Funcion que recibe la matriz orignial y la ultima multiplicacion A^x
#y las multiplica entre sí devolviendo A^x+1
#Multiplicacion de las matrices
#Se hace la multiplicacion lógica (AND) de cada elemento k de la fila i
#con el mismo elemento k de la columna j y se hace la suma lógica (OR) de todos
#los resultados de las multiplicaciones.
def binaryProduct(mat, mat2, tam):
	res = []
	aux = 0

	#Simulacion de una matriz creando listas de listas unitarias dentro de una lista auxiliar
	for i in range(tam):
		res.append([int(0)]*tam)

	for i  in range(0,tam):
		for j in range(0,tam):
			aux = 0
			for k in range(0,tam):
				aux = aux | (mat[i][k]&mat2[k][j])
			res[i][j] = aux
	return res

#Funcion que evalua la diagonal de la matriz original para checar si es reflexiva
#Recorremos la diagonal de la matriz y evaluamos si algun elemento de la diagonal 
#Es cero en caso de ser así la matriz ya no es reflexiva y se actualiza la variable
#Que indica si la relacion tiene dicha propiedad y sale del ciclo al actualizar dicha variable
def check_Reflex(mat, tam):
	val = True
	for i in range(0,tam):
		if mat[i][i] == 0:
			val = False
			break
	return val

#Funcion que valua la simetría de la relacion evaluando que la matriz en (i,j)
#sea igual a la matriz (j,i)
#Se recorre la matriz y se evalua que la matriz tenga el mismo valor en (i,j)
#Y en (j,i) en caso de que no se cambia el valor de la vairable a falso y sale del recorrido
def check_Sim(mat, tam):
	val = True
	for i in range(0,tam):
		for j in range(0,tam):
			if mat[i][j] != mat[j][i]:
				val = False
				break
		if not val:
			break
	return val

#Funcion que recorre la matriz y evalua la antisimetria en base a la definicion
#				Si iRj y jRi -> i = j
#Por lo cual si encontramos el par (i,j) que este relacionado
#Y que (j,i) igual lo esté verificamos que i = j en caso de que esto sea falso
#La relacion no es antisimetrica
def check_Antisim(mat, tam):
	val = True
	for i  in range(0,tam):
		for j in range(0,tam):
			if mat[i][j] == 1 and mat[i][j] == mat[j][i]: 
				if i != j:
					val = False
					break
		if not val:
			break
	return val

#Funcion que evalua la transitividad de la relacion utilizando la cerradura
#Multiplicamos la matriz^x por la matriz original donde x va de 1 a n-1 
#Donde n es la cardinalidad del conjunto sobre el cual esta definida la relacion
#Y evaluamos que los unos la matriz resultante esten dentro de la matriz original
def check_Tran(mat,tam,prod,grafo):
	val = True
	for k in range(2,tam):
		prod = binaryProduct(mat,prod,tam)
		for i in range(0,tam):
			for j in range(0,tam):
				if prod[i][j] == 1:
					if mat[i][j] == 0:
						val = False
			if not val:
				break
		if not val:
			break
	return val


def main():
	nodos=int(input("Ingrese la cantidad de elementos del conjunto\n"))
	matriz=[]
	aux = []
	G = nx.Graph()
	#Creacion de la matriz donde recibir la matriz de adyacencia, una matriz auxiliar y los nodos del grafo.
	for i in range(nodos):
		matriz.append([int(0)]*nodos)
		aux.append([int(0)]*nodos)
		G.add_node(i+1)

	for i in range(0,nodos):
		for j in range(0,nodos):
			print("El elemento ", i+1, " esta relacionado con el elemento ", j+1,"?")
			print("1 Si\n0 No")
			a=int(input())
			matriz[i][j] = a
			aux[i][j] = a

	#LLamadas a las funciones para identificar las propiedades.
	reflexiva = check_Reflex(matriz, nodos)
	simetrica = check_Sim(matriz,nodos)
	antisimetria = check_Antisim(matriz, nodos)
	transitividad = check_Tran(matriz,nodos,aux,G)

	#Identificacion del tipo de relacion en base a sus propiedades
	if reflexiva and simetrica and transitividad:
		print("La relacion es de Equivalencia")
	elif reflexiva and antisimetria and transitividad:
		print("La relacion es de Orden Parcial")
		#Aqui la relacion es de orden parcial y se elabora el diagrama de Hasse
		for i in range(0,nodos):
			matriz[i][i] = 0
		for i in range(0,nodos-1):
			for j in range(0,nodos):
				if matriz[i][j] == 1:
					for k in range(0,nodos):
						if matriz[k][i] == 1:
							matriz[k][j] = 0
		for i in range(0,nodos):
			for j in range(0,nodos):
				if matriz[i][j] == 1:
					G.add_edge(i+1,j+1)
		plt.show(nx.draw(G))
	elif not reflexiva and simetrica:
		print("La relacion es un Grafo")
	else:
		print("Tipo de relacion desconocido, la relacion es:")
		if reflexiva:
			print("Reflexiva")
		if simetrica:
			print("Simetrica")
		if antisimetria:
			print("Antisimetrica")
		if transitividad:
			print("Transitiva")
	
	
main()