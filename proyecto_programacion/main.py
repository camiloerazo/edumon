from flask import Flask, render_template, redirect, request
from registrarUsuario import *



app = Flask(__name__)

@app.route('/') #root
def index():
	return render_template('login.html')

@app.route('/game', methods = ['POST', 'GET'])
def game():
	if request.method == 'POST':
		result = request.form
		print(result)
		usuario = request.form['usuario']
		contrasena = request.form['contrasena']
		#correo_registro = request.form['correo']
		#print(correo_registro,"sadasdsaasdsadasdasdasdsadasdasdasdasd")
		print(usuario,"<-- USUARIO INGRESADO")
		print(contrasena,"<-- CONTRASEÑA INGRESADA")
		print(type(usuario))

		if validarUsuario(usuario,contrasena)==True:
			if validarAdmin(usuario)==True:
				return render_template('admin.html')
			else:
				return render_template('edumon.html')


	return render_template('login.html')

@app.route('/admin', methods = ['POST','GET'])
def admin():
	if request.method == 'POST':
		resultado = request.form
		correo_registro = request.form['correo']
		contrasena_registro = request.form['contrasena_admin']
		user_id = request.form['user_id']
		grado = request.form['grado']
		rol = request.form['rol']
		print(correo_registro,correo_registro,user_id,grado,rol)
		print(resultado)
		registrar(user_id,correo_registro,contrasena_registro,grado,rol)
		return render_template('admin.html')


if __name__ == "__main__":
	print(app.url_map)
	app.run(debug = True)
    
