#JOSE ORTEGA GUIDO - A01770426

import re
import dominate
from dominate.tags import *

variables = ""
operadores = ""
enteros =""
flotante = ""
strings = ""
comentarios = ""
comentariosMult = ""
palabrasReservadas = ""
lexico = [variables,operadores,enteros,flotante,strings,comentarios,comentariosMult,palabrasReservadas]

with open("test.txt","r") as archivo:
    expresiones = archivo.readlines()
    i = 0
    for expresion in expresiones:
        lexico[i] = expresion.rstrip()
        i += 1
archivo.close()
doc = dominate.document(title='Resaltador de sintaxis de Python')

with doc.head:
    link(rel='stylesheet', href='estilo.css')
    meta(charset = "UTF-8")
    meta(name = "viewport", content = "width= device-width, initial-scale= 1")

with doc:
    body(cls = "estilo")
    with open("input2.txt","r",encoding = "utf8") as input:
        lineas = input.readlines()
        i=0
        for linea in lineas:
            with div():
                attr(cls='estilo')
                k = 0
                while(linea[k] == " "):
                    print(lineas[k])
                    span("_", cls = "tabulador")
                    k += 1
                lineas[i] = linea.rstrip()
                palabras = lineas[i].rsplit()
                j = 0 
                if lineas[i].startswith('"""') or lineas[i].startswith("'''") or lineas[i].startswith("#"):
                    if (re.match(lexico[5],lineas[i])):
                        span(lineas[i],cls = "comentarios")
                    elif (re.match(lexico[6],lineas[i])):
                        span(lineas[i],cls = "comentariosMult")                    
                elif lineas[i].startswith("'") or lineas[i].startswith('"'):
                    if (re.match(lexico[4],lineas[i])):
                        span(lineas[i],cls = "strings")
                else
                    for palabra in palabras:
                        if (re.match(lexico[1],palabra)):
                            span(palabra,cls = "operadores")
                        elif (re.match(lexico[2],palabra)):
                            span(palabra,cls = "enteros")
                        elif (re.match(lexico[3],palabra)):
                            span(palabra,cls = "flotante")
                        elif(re.match(lexico[7],palabra)):
                            span(palabra, cls = "palabrasReservadas")
                        elif(re.match(lexico[4],palabra)):
                            span(palabra,cls = "strings")
                        else:
                            try:
                                if (re.match(lexico[0],palabra) and re.match(lexico[1],palabras[j+1])):
                                    span(palabra,cls = "variables")
                                elif(re.match(lexico[0],palabra) and re.match(lexico[7],palabras[j-1])):
                                    span(palabra,cls = "variables")
                                else:
                                    span(palabra)
                            except Exception as e:
                                try:
                                    if (re.match(lexico[0],palabra) and re.match(lexico[1],palabras[j-1])):
                                        span(palabra,cls = "variables")
                                    else:
                                        span(palabra)    
                                except Exception as e:
                                    span(palabra)
                        j += 1
            i += 1
    input.close()
html = open("resaltadorSintaxis.html","w",encoding = "utf8")
html.write(str(doc))
html.close()
