print("Este programa captura importes")
info = """
                    CALCULA TU SUMA
    Este programa lleva el conteo de cuantos importes ha
    introducido un usuario.
    
    Va acumulando todos los importes que el usuario ingresa.
    
    Si el usuari desea terminar el programa puede escribir
    en cualquier momento la palabra exit, quit, terminar.
    
                                    Elaborado por Jonathan
"""
print(info)
conteo = 0
suma = 0.0
minimo = None
maximo = None

while True:
    user_message = """
    Ingresa tu importe (MXN)
    Si quieres dejar de capturar importes
    puedes ingresar en cualquier momento
    'exit', 'quit' o 'terminar':
    """
    
    line = input(user_message).lower()
    if line == "exit" or line == "quit" or line == "terminar":
        break
    try:
        value = float(line)
    except ValueError:
        print("El valor ingresado no es un número válido. Intenta de nuevo. ej.125.5")
        continue
        
    conteo += 1
    suma += value
    
    if minimo is None or value < minimo:
        minimo = value
    if maximo is None or value > maximo:
        maximo = value
        
if conteo == 0:
    print("No se capturaron importes.")
else:
    print("="*32)
    print("La cantidad de numeros ingresados es: ", f"{conteo}")
    print("La suma de los importes es: ", f"{suma}")
    print("El importe mínimo es: ", f"{minimo}")
    print("El importe máximo es: ", f"{maximo}")
print("Programa finalizado")