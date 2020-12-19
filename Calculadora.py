# Metodo principal de la calculadora
def calculator():
    finish = False
    while (not finish):
        print("\n")
        num1 = input("First number:")
        num2 = input("Second number:")
        operator = input("Operation:")

        print(calculate(num1, num2, operator))

        print("")
        exit = input("Exit (y/n):")
        if (exit == "y"):
            finish = True


# Metodo que encuentra el resultado de la operacion
# Params:
#   num1: primer número de la operación
#   num2: segundo número de la operación
#   operator: operador mátematico
# Return: El resultado de la operación
def calculate(num1, num2, operator):
    if(operator == "+"):
        return sum(num1, num2)
    elif(operator == "-"):
        return subtract(num1, num2)
    elif(operator == "*"):
        return multiply(num1, num2)
    elif(operator == "/"):
        return divide(num1, num2)
    else:
        return "Not a valid operator"

# Metodo encargado de las sumas
# Params:
#   num1: primer número de la operación
#   num2: segundo número de la operación
# Return: El resultado de la suma
def sum(num1, num2):
    return int(num1)+int(num2)

# Método encargado de las restas
# Params:
#   num1: primer número de la operación
#   num2: segundo número de la operación
# Return: El resultado de la resta
def subtract(num1, num2):
    return int(num1)-int(num2)

# Método encargado de las multiplicaciones
# Params:
#   num1: primer número de la operación
#   num2: segundo número de la operación
# Return: El resultado de la multiplicación
def multiply(num1, num2):
    return int(num1)*int(num2)

# Método encargado de las divisiones
# Params:
#   num1: primer número de la operación
#   num2: segundo número de la operación
# Return: El resultado de la división
def divide(num1, num2):
    return int(num1)/int(num2)

#Corre el programa
calculator()

