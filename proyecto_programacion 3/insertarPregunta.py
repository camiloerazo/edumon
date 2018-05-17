def insertar_pregunta(pregunta,lista_respuestas,indice_correcta,materia):
    f = open("preguntas.txt","r")

    texto = []

    for linea in f:
        linea = linea.replace("\n"," ")
        texto.append(linea.split(","))

    print(texto,"\n")

    if len(texto)!=0:
        id_pregunta = len(texto)-1
    else:
        id_pregunta = 0

    texto = []

    print(id_pregunta)
     
    f.close()

    x = open("preguntas.txt","a")

    x.write("\n"+ str(id_pregunta)+","+ materia +","+"TRA"+","+ pregunta)
    
    x.close()

    f = open("respuestas.txt","r")

    for linea in f:
        linea = linea.replace("\n"," ")
        texto.append(linea.split(","))

    print(texto)

    f.close()

    x = open("respuestas.txt","a")

    id_respuesta = len(texto)-1

    correcta = lista_respuestas[indice_correcta]
    print(lista_respuestas[indice_correcta])

    id_respuesta_cor = 0

    for i in range(len(lista_respuestas)):
        if lista_respuestas[i]==correcta:
            x.write("\n"+str(id_respuesta +i)+","+str(id_pregunta)+","+lista_respuestas[i])
            id_respuesta_cor = id_respuesta+i
        else:
            x.write("\n"+str(id_respuesta +i)+","+str(id_pregunta)+","+lista_respuestas[i])

    print(id_respuesta_cor,"Correcta")

    x.close()


    f = open("respuestas_correctas.txt","a")

    f.write("\n"+ str(id_respuesta_cor)+","+ str(id_pregunta))

    f.close()