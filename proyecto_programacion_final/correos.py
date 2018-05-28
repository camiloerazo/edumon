import smtplib


def enviarMail(destinatario,contrasenaDestinatario):

	f = open("user_contrasena.txt","r")

	texto = []

	for linea in f:
		linea = linea.replace("\n"," ")
		texto.append(linea.split(","))

	print(texto[0][0])
	email = texto[0][0]
	contrasena = texto[0][1]

	f.close()


	contenido = "Felicidades por registrarte en EDUMON tu usuario es\n"+str(destinatario)+"\ny tu contrasena es\n"+str(contrasenaDestinatario)

	mail = smtplib.SMTP("smtp.gmail.com",587)

	mail.ehlo()

	mail.starttls()
	mail.login(email,contrasena)

	mail.sendmail(email,destinatario,contenido)
	mail.close()
	print(contenido)
