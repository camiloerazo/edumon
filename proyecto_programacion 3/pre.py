import json

def modificarJson(grado,materia,id,pregunta,respuestas,indice_correcta):
	grado = str(grado)
	materia = str(materia)
	id = str(id)

	with open('preguntas_json.json') as f:
		data = json.load(f)
		#data[grado][materia][0] = {"id": id, "pregunta": pregunta, "respuestas":respuestas,
		 #"correcta":indice_correcta}
		data[grado] = {}
		data[grado][materia] = []
		data[grado][materia] = {"id":id,"pregunta":pregunta,"respuestas": respuestas,
		 "correcta":indice_correcta}

	x = open("preguntas_json.json","w")
	json.dump(data,x, indent=2)

	x.close()
modificarJson(2,"matematicas",3,"Cuanto es 500-250", [230,250,580,235],1)