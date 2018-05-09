def registrar(user_id, email, password, grado, rol):

	user_id = str(user_id) # Se transforma los datos en string
	email = str(email)
	password = str(password)
	grado = str(grado)
	rol = str(rol)

	if rol != 'admin':
		rol = 'user'
	
	leer_login = open('login.txt','r')
	agregar_datos = open("datos_estudiante.txt",'r')

	texto = []
	texto2 = []
	diccionario = {} # Se crea el diccionario

	for linea in leer_login:
		linea = linea.replace("\n"," ")
		texto.append(linea.split(','))

	for linea in agregar_datos:
		linea = linea.replace("\n"," ")
		texto2.append(linea.split(','))
	correos = []
	id_s = []

	for i in range(len(texto)):
		correos.append(texto[i][0])

	for i in range(len(texto2)):
		id_s.append(texto2[i][0])
	

	diccionario["user_id"] = id_s
	diccionario["correos"] = correos # Se llena la key 'correos' con todos los correos

	leer_login.close()
	agregar_datos.close()

	if email in diccionario["correos"] or user_id in diccionario["user_id"]:
		print("El email de {} o su user_id ya se encuentra en la base de datos y no puedes agregarlo"
			.format(email))
		return False

	else:
		agregar_login = open('login.txt','a')
		agregar_login.write("\n"+ email +","+ password)
		agregar_login.close()

		print('\nEl email de {} se ha agregado'.format(email))

		agregar_datos = open("datos_estudiante.txt",'a')
		agregar_datos.write('\n'+ user_id +',' + email +',' + password +',' + grado 
			+ ','+ rol)
		agregar_datos.close()
		if rol == 'admin':
			agregar_admin = open('admin.txt','a')
			agregar_admin.write('\n'+ email)
			agregar_admin.close()
			print("\nEl email de {} se registro como admin".format(email))
		else:
			print("\nEl email de {} se registro como usuario".format(email))


def validarUsuario(email,contraseña): #preguntar sobre esta funcion

	email = str(email)
	contraseña = str(contraseña)

	validar = open('login.txt','r')
	texto = []
	correos = []
	contraseñas = []

	for linea in validar:
		linea = linea.replace("\n"," ")
		linea = linea.replace(' ','')
		texto.append(linea.split(","))

	for i in range(len(texto)):
		correos.append(texto[i][0])
		contraseñas.append(texto[i][1])
	texto2 = []
	flag = False

	for i in range(len(texto)):
		for j in range(len(texto[i])):
			if texto[i][j]==email:
				print('\nSE ENCONTRO EL EMAIL EN LA BASE DE DATOS \n')
				texto2=(texto[i])
				flag = True

	if flag==False:
		print('\n NO SE ENCUENTRA EL EMAIL EN LA BASE DE DATOS')
	else:
		print("DATOS DEL USUARIO = ",texto2)

	if flag == True and email==texto2[0] and contraseña==texto2[1]:
		print("\n EL USUARIO Y LA CONTRASEÑA ESTAN CORRECTAS INGRESANDO...")
		return True

	else:
		print("\nLA CONTRASEÑA QUE INGRESO ES INVALIDA")
		return False
		
	validar.close()

def validarAdmin(email):

	email = str(email)
	texto = []
	correos = []

	f = open('admin.txt','r')

	for linea in f:
		linea = linea.replace('\n'," ")
		linea = linea.replace(" ","")
		texto.append(linea.split(","))

	for i in range(len(texto)):
		correos.append(texto[i][0])

	if email in correos:
		print(" \nEl email {} si esta en la base de los admins \n INGRESANDO".format(email))
		return True
	else:
		print("\nEl email {} no esta en la base de los admins".format(email))
		return False

	f.close()

def listaDeDatos(email):
	f = open('datos_estudiante.txt')

	texto = []

	for linea in f:
		linea = linea.replace('\n','')
		texto.append(linea.split(','))

	datos = []
	for i in range(len(texto)):
		for j in range(len(texto[i])):
			if texto[i][j]==email:
				print("\nSe encontro el correo electronico")
				datos.append(texto[i])
	datos2 = []

	for i in range(len(datos[0])):
		datos2.append(datos[0][i])
	print("\nEstos son los datos del usuario ingresado = ",datos2)
	f.close()
	return datos2