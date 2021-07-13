from os import system, name
from time import sleep
import sys
import requests

'''lista = open('lista.txt', 'r')
lista_comidas = []

for i in lista:
	lista_comidas.append(i)
	
print(lista_comidas)'''

#####----- COMIDAS -----#####

sopa_de_arvejas = ["cebolla", "arveja", "papa"]
guiso_de_lentejas = ["lenteja", "cebolla", "zanahoria", "papa", "pimiento", "botella de tomate"]
caldo = ["calabaza", "choclo", "zanahoria"]
salsa_para_pasta = ["botella de tomate", "cebolla", "pimiento"]
zapallitos_rellenos = ["zapallito", "cebolla", "pimiento", "soja texturizada"]
bombas_de_calabaza = ["queso", "calabaza", "pan rallado"]
milanesas_de_berenjena = ["berenjena", "pan rallado"]
gaspacho = ["pepino", "tomate", "pimiento", "cebolla", "ajo"]
empanadas_fatai = ["soja texturizada", "tapa de empanada"]
empanadas_de_papa = ["tapa de empanada", "cebolla", "papa", "aceituna","queso"]
tarta_de_zapallito = ["zapallito", "cebolla"]
tarta_de_calabaza_y_tofu = ["tofu", "calabaza", "tapa de tarta", "queso", "cebolla"]
milanesa_de_soja = ["poroto de soja", "harina integral", "pan rallado"]
babaganush = ["berenjena", "especias"]
croquetas_de_arroz = ["arroz", "zapallito", "cebolla", "curry"]
bombas_de_papa = ["papa", "pan rallado", "queso"]
salsa_de_hongos = ["hongo", "cebolla morada", "leche", "maicena", "agua"]
sorrentinos_rellenos = ["masa", "hongo", "cebolla morada", "nuez"]
empanadas_de_batata = ["batata", "cebolla", "queso", "aceituna negra"]
croquetas_de_porotos_negros = ["harina de arroz", "poroto negro", "tomate", "cebolla", "morron rojo"]
milanesas_de_pencas = ["penca", "harina de garbanzo", "pan rallado"]

#####----- LISTADO -----#####

lista_comidas = [
sopa_de_arvejas,
guiso_de_lentejas,
caldo,
salsa_para_pasta,
zapallitos_rellenos,
bombas_de_calabaza,
milanesas_de_berenjena,
gaspacho,
empanadas_fatai,
empanadas_de_papa,
tarta_de_zapallito,
tarta_de_calabaza_y_tofu,
milanesa_de_soja,
babaganush,
bombas_de_papa,
salsa_de_hongos

]

#####---- DEFINIR FUNCIONES ----#####


def clima():
	new_line()
	printbarra()
	r = requests.get('http://es.wttr.in/BuenosAires?0')
	x = r.text
	print(x)
	if "Soleado" in x or "Despejado" in x:
		print("Lindo día para cocinar!")
	else:
		print("El sol esta sobrevalorado!")


def namestr(obj, namespace):
	return [name for name in namespace if namespace[name] is obj]


def new_line():
	print("\n")


def clear():
	# pa windows
	if name == 'nt':
		_ = system('cls')
	# pa linux o mac
	else:
		_ = system('clear')


def drawing():
	drawing='''
                            _          _ 
                           (c)___c____(c) 
                            \ ........../ 
                             |.........| 
                              |.......| 
      vamo a cocinar master   |.......| 
   algo vegano, obvio \       |=======| 
                       \      |=======| 
                        \    __o)""""::? 
                         \  C__    c)::; 
                          \___ >--   ::     /\ 
                               (____/      /__\ 
                               } /""|      |##| 
                    __/       (|V ^ )\     |##| 
                    o | _____/ |#/ / |     |##| 
           @        o_|}|_____/|/ /  |     |##| 
                          _____/ /   |     ~!!~ 
              ======ooo}{|______)#   |     /`'\ 
          ~~~~ ;    ;          ###---|8     "" 
        ____;_____;____        ###====     /:|\ 
       (///0///@///@///)       ###@@@@| 
       |~~~~~~~~~~~~~~~|       ###@@@@| 
        \             /        ###@@@@|               + 
         \___________/         ###xxxxx      /\      // 
           H H   H  H          ###|| |      /  \    // 
           H H   H  H           | || |     /____\  /~_^_ 
           H H   H  H           C |C |     _|@@|_ /__|#|_ 
           H H   H  H            || ||    /_|@@|_/___|#|/| 
 v    \/   H(o) (o) H            || ::   |:::::::::::::|#| 
 ~    ~~  (o)      (o)        Ccc__)__)  |::::::::::::#| 
  \|/      ~   @* & ~                    |:::::::::::::|/  \|/ 
   ~           \|/        !!        \ !/  ~~~~~~~~~~~~~    ~~~ 
               ~~~        ~~         ~~           ~~ 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
	new_line()
	print(drawing)
	new_line()


def rat():
	print("  ,,==.                      (bai)")
	print(" //    `                      /")
	print("||      ,--~~~~-._ _(\--,_   /")
	print(" \\._,-~   \      '    *  `o ")
	print("  `---~\( _/,___( /_/`---~~")
	print("        ``==-    `==-,")


def printbarra():
	print("="*50)


def printequis():
	print("Xx"*25)


def printflorcitas():
	print("*"*50)


def bienvenida():
	clima()
	printbarra()
	print("Vamos a comer algo!")
	new_line()
	print("creado por lucasuait          2021-CopyLeft")
	printbarra()


def cocinar():
	clear()
	#print(lista_comidas)
	drawing()
	sleep(3)
	clear()
	printflorcitas()
	new_line()
	print(f"Recorda ingresar los ingredientes en singular\nseparados por una coma y sin espacio")
	new_line()
	print("creado por lucasuait          2021")
	printflorcitas()
	new_line()
	ingredientes = []
	ingredientes = input("Escribi los ingredientes que vayas a usar: ")
	if ingredientes == "exit":
		clear()
		menu_principal()
	elif ingredientes == "dibujo":
		drawing()
		sleep(10)
		menu_principal()

	posibilidad = ingredientes.split(",")

	clear()
	for comida in lista_comidas:
		#print(comida)
		var = 0
		noprint = 0
		nonoprint = 0
		for ingrediente in comida:
			#print(ingrediente)
			if ingrediente in posibilidad:
				#print(ingrediente)
				var += 1
				if len(comida) >= 3:
					cantidad = len(comida) - 1
				else:
					cantidad = 2
				if var >= cantidad:
					if noprint == 1:
						pass
					else:
						nombre = namestr(comida, globals())
						nombre = nombre[0]
						nombre = nombre.replace("_", " ")
						printbarra()
						new_line()
						print(f"[+] Podes hacer" + " " + str(nombre) + " " +"con estos ingredientes:" + " " + str(comida))
						new_line()
						printbarra()
						noprint += 1
				elif var < cantidad:
					if nonoprint == 1:
						pass
					else:
						nombre = namestr(comida, globals())
						nombre = nombre[0]
						nombre = nombre.replace("_", " ")
						print(f"[-] Aun NO podes hacer" + " " + str(nombre) + " " +"porque faltan algunos de estos:" + " " + str(comida))
						nonoprint += 1
	menu_principal()


def recetas():
	clear()
	printbarra()
	new_line()
	for comida in lista_comidas:
		nombre = namestr(comida, globals())
		nombre = nombre[0]
		nombre = nombre.replace("_", " ")
		print("[+]"+ " " + str(nombre))
	new_line()
	printbarra()
	new_line()
	menu_principal()


def menu_principal():
	new_line()
	print("Presiona 1 para ver todos los ingredientes")
	new_line()
	print("Presiona 2 para ver las recetas")
	new_line()
	print("Presiona 3 para ver que podes cocinar")
	new_line()
	print("Presiona 4 para salir")
	new_line()
	eleccion = input("Elegi 1, 2, 3 o 4: ")
	if eleccion == "1":
		ver_ingredientes()
	elif eleccion == "2":
		recetas()
	elif eleccion == "3":
		cocinar()
	elif eleccion == "4":
		chau()
	else:
		print("Elegiste cualquier cosa")
		sleep(3)
		clear()
		menu_principal()


def ver_ingredientes():
	clear()
	printbarra()
	new_line()
	ingredientes_menu = []
	for comida in lista_comidas:
		for ingrediente in comida:
			if ingrediente in ingredientes_menu:
				pass
			else:
				ingredientes_menu.append(ingrediente)
	for i in ingredientes_menu:
		print("[+]" + " " + i)
	new_line()
	printbarra()
	menu_principal()


def chau():
	clear()
	#printbarra()
	new_line()
	rat()
	new_line()
	#printbarra()
	sleep(2)
	clear()
	sys.exit()

#####---- Inicio del programa ----#####

clear()
bienvenida()
menu_principal()
