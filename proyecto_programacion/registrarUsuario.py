
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
	print("Correos Actuales {}".format(diccionario["correos"]))

	leer_login.close()
	agregar_datos.close()


	if email in diccionario["correos"] or user_id in diccionario["user_id"]:
		print("El email de {} o su user_id ya se encuentra en la base de datos y no puedes agregarlo"
			.format(email))

	else:
		agregar_login = open('login.txt','a')
		agregar_login.write("\n"+ email +", "+ password)
		agregar_login.close()

		print('El email de {} se ha agregado'.format(email))

		agregar_datos = open("datos_estudiante.txt",'a')
		agregar_datos.write('\n'+ user_id +', ' + email +', ' + password +', ' + grado 
			+ ', '+ rol)
		agregar_datos.close()
		if rol == 'admin':
			agregar_admin = open('admin.txt','a')
			agregar_admin.write('\n'+ email)
			agregar_admin.close()
			print("El email de {} se registro como admin".format(email))
		else:
			print("El email de {} se registro como usuario".format(email))

#registrar(1004217473,"anita@gmail.com",1234,3,"admin")
#registrar(122112,"juancamiloerazo82@gmail.com","camiloerazo1",11,"admin")


	

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

	print("print texto",texto)

	for i in range(len(texto)):
		correos.append(texto[i][0])
		contraseñas.append(texto[i][1])

	print(correos, "estos son los correos", contraseñas, "estas son las contraseñas")

	if email in correos and contraseña in contraseñas:

		print("Accediendo a la sesion de {}".format(email))
		return True

	else:
		print("No esta registrado en la base de datos")
		return False
		
	validar.close()

def validarAdmin(email):

	email = str(email)
	print(email)
	texto = []
	correos = []

	f = open('admin.txt','r')

	for linea in f:
		linea = linea.replace('\n'," ")
		linea = linea.replace(" ","")
		texto.append(linea.split(","))

	print(texto)

	for i in range(len(texto)):
		correos.append(texto[i][0])

	print(correos)

	if email in correos:
		print(" El email {} si esta en la base de los admins \n INGRESANDO".format(email))
		return True
	else:
		print("El email {} no esta en la base de los admins".format(email))
		return False

	f.close()

#validarAdmin("juan")