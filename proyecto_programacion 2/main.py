from flask import Flask, render_template, redirect, request
from registrarUsuario import *

app = Flask(__name__)

@app.route('/') #root
def index():
	return render_template('login.html')

@app.route('/login', methods = ['POST', 'GET'])
def game():
	if request.method == 'POST':
		usuario = request.form['usuario']
		contrasena = request.form['contrasena']
		print("\n",usuario,"<-- USUARIO INGRESADO")
		print("\n",contrasena,"<-- CONTRASEÑA INGRESADA")
		registro = True

		if validarUsuario(usuario,contrasena)==True:
			if validarAdmin(usuario)==True:
				return render_template('admin.html')
			else:
				datos = listaDeDatos(usuario)
				return render_template('edumon.html',correo=usuario, datos=datos)
		else:
			return render_template('login.html',registro=False,usuario=usuario)
	else:
		return render_template('login.html',registro=True)

	return render_template('login.html',registro=True)

@app.route('/admin', methods = ['POST','GET'])
def admin():
	if request.method == 'POST':
		resultado = request.form
		correo_registro = request.form['correo']
		contrasena_registro = request.form['contrasena_admin']
		user_id = request.form['user_id']
		grado = request.form['grado']
		rol = request.form['rol']
		print("EL ADMINITRADOR QUIERE REGISTRAR = ","\n",correo_registro,"\n",
			correo_registro,"\n",user_id,grado,"\n",rol)
		registrar(user_id,correo_registro,contrasena_registro,grado,rol)
		
		return render_template('admin.html')
	else:
		return 'Llena el formulario para que comienze la diversion!'


if __name__ == "__main__":
	app.run(debug = True)