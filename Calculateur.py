def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Division par zéro"

# Menu
print("Sélectionnez une opération:")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")

# Demander à l'utilisateur de choisir une opération
choix = input("Entrez le numéro de l'opération (1/2/3/4): ")

# Demander à l'utilisateur d'entrer les nombres
nombre1 = float(input("Entrez le premier nombre: "))
nombre2 = float(input("Entrez le deuxième nombre: "))

# Effectuer l'opération sélectionnée
if choix == '1':
    print(nombre1, "+", nombre2, "=", addition(nombre1, nombre2))
elif choix == '2':
    print(nombre1, "-", nombre2, "=", soustraction(nombre1, nombre2))
elif choix == '3':
    print(nombre1, "*", nombre2, "=", multiplication(nombre1, nombre2))
elif choix == '4':
    print(nombre1, "/", nombre2, "=", division(nombre1, nombre2))
else:
    print("Opération non valide")
