
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

'''
foods = {
    1: {
        "name": "Sopa-de-arvejas",
        "ingredients" : {
            1: "cebolla",
            2: "arveja",
            3: "papa"
        }
    },
    2: {
        "name": "Guiso-de-lentejas",
        "ingredients": {
            1: "lenteja",
            2: "cebolla",
            3: "zanahoria",
            4: "papa",
            5: "pimiento",
            6: "botella de tomate"
        }
    }
}
'''

for recetas in lista_comidas:
    for receta in recetas:
