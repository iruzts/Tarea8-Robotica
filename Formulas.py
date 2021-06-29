formula = {
    "Area del triángulo": "(base * altura) / 2",
    "Area del cuadrado": "lado * lado",
    "Area del circulo": "(3.1416) * (radio * radio)",
    "Area del rectangulo": "Area=base*altura",
    "Area del rombo": "area=diagonale mayor* diagonale menor/2",

}

try:
    print ("Formulas Matematicas")
    Formula2 = input("Ingresar Nombre de Formula a Buscar: ")
    print("La Formula para resolver {} es: {} .".format(Formula2, format(formula[Formula2],)))
except KeyError:
    print("El Pais no existe")