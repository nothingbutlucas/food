from os import system, name
import sys
import requests
from draws import *


#####----- CONSTANTES -----#####

EXIT = ["exit", "quit", "salir", "q", "e"]
MENU = ["menu", "menu principal", "'menu'"]
DIBUJO = ["draw", "dibujo", "ver dibujo"]
#LINK_API = "https://plant-base-food-api.herokuapp.com"
LINK_API = "http://localhost:8000"

#####---- DEFINIR FUNCIONES ----#####


def clima():
	new_line()
	# printbarra()
	try:
		r = requests.get('http://es.wttr.in/BuenosAires?0')
		x = r.text
		print(x)
		if "Soleado" in x or "Despejado" in x:
			print("Lindo día para cocinar! | Great day for cooking!")
		else:
			print("El sol esta sobrevalorado! | The sun is overrated!")
	except:
		print("Hi :) | Hola :)\n")


def capture_foods():
	foods = requests.get(f"{LINK_API}/foods")
	foods = foods.json()
	return (foods)


def capture_recipes():
	recipes = requests.get(f"{LINK_API}/foods/recipes")
	recipes = recipes.json()
	all_recipes = list()
	for recipe in recipes:
		recipe = recipe.replace("-", " ")
		all_recipes.append(recipe)
	return all_recipes


def capture_food_id(user_input):
	food = requests.get(f"{LINK_API}/foods/id/{user_input}")
	food = food.json()
	return (food)


def namestr(obj, namespace):
	return [name for name in namespace if namespace[name] is obj]


def clear():
	# pa windows
	if name == 'nt':
		_ = system('cls')
	# pa linux o mac
	else:
		_ = system('clear')


def bienvenida():
	clima()
	# printbarra()
	print("Vamos a cocinar algo! | Let's cook something!")
	new_line()
	print("creado por devycoso | created by devycoso  <- 2021 - CopyPaste")
	# printbarra()


def cocinar():
	printflorcitas()
	print("COCINAR | COOK")
	new_line()
	print(f"Recorda ingresar los ingredientes en singular y separados por una coma :) | Remember to enter the ingredients in the singular and separated by a comma :)")
	new_line()
	print("creado por devycoso | created by devycoso  <- 2021 - CopyPaste")
	printflorcitas()
	new_line()
	ingredientes = input("Escribi los ingredientes que vayas a usar ó 'menu' para volver al menu | Write the ingredients you are going to use or 'menu' to return to the menu: ")

	if ingredientes.strip() in MENU:
		menu_principal()
	posibilidad = ingredientes.split(",")
	posibility = list()
	for ingredient in posibilidad:
		ingredient = ingredient.strip()
		posibility.append(ingredient)
	# clear()

	foods = capture_foods()
	can_cook = list()

	# print(foods)
	# print(foods.get('0'))
	# print(foods.get('0').get("name"))

	for x, food in enumerate(foods):
		food = foods[str(x)]["name"] + " " + str(foods[str(x)]["main-ingredients"]) + " " + str(foods[str(x)]["secondary-ingredients"])
		main_ingredients = foods[str(x)]["main-ingredients"]
		have_ingredient = list()
		for ingredient in main_ingredients:
			if ingredient in posibility:
				have_ingredient.append(ingredient)
			if len(have_ingredient) == len(main_ingredients):
				can_cook.append("[ + ] Puedes cocinar | U can cook:")
				can_cook.append("  |  ")
				can_cook.append("  --" + str(food).replace("-", " "))
				can_cook.append("\n")
	new_line()
	for x in can_cook:
		print(x)

	if len(can_cook) <= 0:
		print(f"No puedes cocinar nada de lo que tengo disponible con {str(posibility)} :(")
		new_line()
		print(f"You can't cook anything I have available with {str(posibility)} :(")
	new_line()
	cocinar()


def recetas():
	# clear()
	# printbarra()
	new_line()
	recipes = capture_recipes()
	for n, recipe in enumerate(recipes):
		recipe = f"[ {n} ] - {recipe}"
		print(recipe)
	new_line()
	print("[ 999 ]" + " " + "Volver al menu principal")
	new_line()

	input_user = input("Elegi | Choose: ")
	new_line()
	print("[ N ] -> Nombre | Name")
	print("[ M/P ] -> Main ingredient | Ingrediente principal")
	print("[  S  ] -> Secondary ingredient | Ingrediente secundario")

	if input_user.strip() == "999":
		return menu_principal()
	else:
		try:
			food = capture_food_id(int(input_user.strip()))
			name = (food["name"]).replace("-", " ")
			new_line()
			print("[  N  ] -> " + name)
			for ingredient in food["main-ingredients"]:
				print(f"[ M/P ] --> {ingredient}")
			for ingredient in food["secondary-ingredients"]:
				print(f"[  S  ] --> {ingredient}")
		except KeyError:
			error = capture_food_id(int(input_user.strip()))
			error = error["detail"][0]["msg"]
			new_line()
			print("Error: " + error)
		except Exception:
			print("Ups, no se que, pero algo salío mal :( | Ups, i don't know what, but something when wrong :(")
		return menu_principal()


def menu_principal():
	new_line()
	print("[ 1 ] Ver todos los ingredientes | See all the ingredients")
	new_line()
	print("[ 2 ] Ver las comidas | See all the meals")
	new_line()
	print("[ 3 ] Ver que podes cocinar | See what u can cook")
	new_line()
	print("[ 4 ] Para salir | Exit")
	new_line()
	eleccion = input("Elegi | Choose 1, 2, 3 o 4: ")
	new_line()
	eleccion = eleccion.strip()
	if eleccion == "1":
		ver_ingredientes()
	elif eleccion == "2":
		recetas()
	elif eleccion == "3":
		cocinar()
	elif eleccion == "4":
		chau()
	else:
		print("Elegiste cualquier cosa, usa los numeros")
		menu_principal()


def ver_ingredientes():
	ingredientes_menu = []
	foods = capture_foods()
	for x, food in enumerate(foods):
		ingredients = foods[str(x)]["main-ingredients"] + foods[str(x)]["secondary-ingredients"]
		for ingredient in ingredients:
			if ingredient not in ingredientes_menu:
				ingredientes_menu.append(ingredient)

	for ingredient in ingredientes_menu:
		print("[ + ]" + " " + str(ingredient))

	menu_principal()


def chau():
	new_line()
	rat()
	new_line()
	sys.exit()


#####---- Inicio del programa ----#####

bienvenida()
menu_principal()