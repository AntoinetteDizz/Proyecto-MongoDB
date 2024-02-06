from pymongo import MongoClient

import json

# FUNCION PARA SALIR DEL PROGRAMA

def exitMenu():
   exit()

#FUNCION PARA MOSTRAR EN PANTALLA EL MENU DEL PROGRAMA
   
def showMenu():
   print("\t\t\t______________MENU______________\n")
   print("1- MOSTRAR LAS HERRAMIENTAS MENAJADAS DE CADA PERSONA")
   print("0- Salir")
   option = int(input("INGRESA LA OPCION DE ACUERDO AL MENU "))
   return option

#FUNCION QUE MUESTRA EN PANTALLA LAS HERRAMIENTAS UTILIZADAS POR CADA INDIVIDUO

def showSkills(results):
   for ob in results:
      name = ob["basics"]
      nombre = name["name"]

      skills = ob["skills"]

      message = "NOMBRE DE LA PERSONA {}".format(nombre)
      print(message)

      message = "NUMERO DE HERRAMIENTAS MANEJADAS -> {} \n".format(len(skills))
      print(message)
      for herramienta in skills:
         variable = herramienta["name"]
         message = "Nombre: {}".format(variable)
         print(message)
         variable = herramienta["level"]
         message = "Nivel: {}".format(variable)
         print(message)
      print("--------------------------------------------------------------")

#with open('resume.json', 'r') as archivo:
#    cvData = json.load(archivo)

MONGO_URI = 'mongodb://localhost:27017/'

client = MongoClient(MONGO_URI)

db = client['cv']
collection = db['data']
results = collection.find()

#query = {"basics.name":"Alvaro Aguinagalde Freites"}

#query4 = {"basics.name":"Alvaro Aguinagalde Freites","languages.language":"Ingles"}

#proyeccion = {"languages.$": 1}

while True:
   option = showMenu()
   if option == 1:
      showSkills(results)
   if option == 0:
      exitMenu()


