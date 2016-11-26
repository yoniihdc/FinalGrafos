import networkx as nx
import matplotlib.pyplot as plt

def binaryProduct(mat, mat2, tam):
	res = []
	aux = 0
	for i in range(tam):
		res.append([int(0)]*tam)
	for i  in range(0,tam):
		for j in range(0,tam):
			aux = 0
			for k in range(0,tam):
				aux = aux | (mat[i][k]&mat2[k][j])
			res[i][j] = aux
	print(res)
	return res

def check_Reflex(mat, tam):
	val = True
	for i in range(0,tam):
		if mat[i][i] == 0:
			val = False
			break
	return val

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

def check_Antisim(mat, tam):
	val = True
	for i  in range(0,tam):
		for j in range(0,tam):
			if i != j and mat[i][j] == 1: 
				if mat[i][j] == mat[j][i]:
					val = False
					break
	return val

def check_Tran(mat,tam,prod,grafo):
	val = True
	for i in range(2,tam):
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
	nodos=int(input("Ingrese la cantidad de elementos del conjunto"))
	matriz=[]
	aux = []
	G = nx.Graph()
	for i in range(nodos):
		matriz.append([int(0)]*nodos)
		aux.append([int(0)]*nodos)
		G.add_node(i+1)

	for i in range(0,nodos):
		for j in range(0,nodos):
			print("El elemento ", i+1, " esta relacionado con el elemento ", j+1,"?")
			print("1 Si\n0 No")
			a=int(input())
			if a == 1 and i != j:
				G.add_edge(i+1,j+1)
			matriz[i][j] = a
			aux[i][j] = a
	reflexiva = check_Reflex(matriz, nodos)
	simetrica = check_Sim(matriz,nodos)
	antisimetria = check_Antisim(matriz, nodos)
	transitividad = check_Tran(matriz,nodos,aux,G)

	if reflexiva and simetrica and transitividad:
		print("La relacion es de Equivalencia")
	elif reflexiva and antisimetria and transitividad:
		print("La relacion es de Orden Parcial")
		for i in range(1,nodos-1):
			for j in range(i+1,nodos):
				if i != j:
					if matriz[i][j] == 1:
						for k in range(0,i):
							if matriz[k][i] == 1:
								if G.has_edge(k+1,j+1):
									G.remove_edge(k+1,j+1)
		plt.show(nx.draw(G))
	elif simetrica and transitividad:
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