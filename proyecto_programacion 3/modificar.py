def cambiarGrado(usuario,grado):
	grado = str(grado)
	f = open('datos_estudiante.txt',"r")

	texto = []

	for linea in f:
		linea = linea.replace("\n"," ")
		texto.append(linea.split(','))

	

	lineaCambiar = []
	indice = 0
	indice1 = 0

	for lista in texto:
		indice += 1
		for elemento in lista:
			if elemento == usuario:
				lineaCambiar = lista
				indice1 = indice-1

	print(lineaCambiar,"<--  DATOS PARA CAMBIAR GRADO")
	print(indice1,"<-- INDICE DONDE SE VA A CAMBIAR EL GRADO")

	texto[indice1][3] = grado
	print(texto)
	f.close()

	f = open('datos_estudiante.txt',"w")
	for i in range(len(texto)):
		f.write(texto[i][0]+","+texto[i][1]+","+texto[i][2]+","+texto[i][3]+","+texto[i][4]+"\n")
	f.close()
