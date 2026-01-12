name = "Hola Mundo"
print(name)

# Built-in method input(argument)-Se utiliza para que el usuario ingrese información
user_name = input("¿Como te llamas?: ")
edad_txt = input("¿Cuál es tu edad?: ")

#Built-in method type(argument)-Nos dice el tipo de variable
print(user_name)
print(type(user_name))
print(edad_txt)
print(type(edad_txt))

#Método built-in int(1 argument)-Convierte un String a un número entero
try:
    edad = int(edad_txt)
    print(edad)
    print(type(edad))
except ValueError:
    print("Error: la conversión no se pudo realizar.")
    print("Debes ingresar un número entero")

print("Fin del programa")