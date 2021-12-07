#Tenemos un diccionario que hace de agenda con 3 valores llamados contactos
telefonos = {
	"Marian": 123,
	"Papá": 345,
	"Mamá": 567}
consultando = True
#menu de la agenda
while consultando:
	print()
	print("Consultar contactos: 1")
	print("Añadir contactos: 2")
	print("Modificar contactos: 3")
	print("Borrar contactos: 4")
	print("Salir: 5")
#se le pide al usuario que elija una opción por comando
	opcion= " "
	while opcion not in ("1","2","3","4","5"):
		opcion= input("- ")
	if opcion=="1":
		nombre=input("Nombre: ")
		if nombre not in telefonos:
			print("El nombre que esta buscando no se encuentra en la agenda")
		else:
			telef=telefonos[nombre]
			print(nombre,":",telef)
#Se muestra la clave y el valor relacionado a esa clave
	elif opcion=="2":
		nombre= input("Nombre: ")
		if nombre in telefonos:
			print("Ese nombre ya se encuentra en la agenda")
		else:
			telef=int(input("agregar numero de telefono: "))
			telefonos[nombre]=telef
			print("el telefono de contacto se guardo correctamente")
	elif opcion == "3":
		nombre =input("Nombre: ")
		if nombre not in telefonos:
			print("Ese nombre no está en la agenda de telefonos")
		else:
			telef= int(input("telefono: "))
			telefonos[nombre]= telef
#se modifica el telefono de la misma manera en que se agrega, es una opción más sencilla
			print("El telefono del contacto se modifico correctamente")
#se modifica por el nuevo telefono que introduce el usuario
	elif opcion== "4":
		nombre= input("Nombre: ")
		if nombre not in telefonos:
			print("ESe nomnre no está en la agenda telefonica")
		else:
			del telefonos[nombre]
			print("el telefono se borro correctamente")
	elif opcion=="5":
		consultando= False
#de esta menera se sale del programa