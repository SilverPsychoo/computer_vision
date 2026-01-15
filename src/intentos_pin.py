"""
    1)Este programa va a pedir el usuario su PIN de acceso.
    Si el pin es correcto, entonces el programa debe decirle
    autenticación exitosa, acceso concedido.
    
    2)Si el pin es incorrecto, el programa debe decirle
    pin incorrecto, y el numero de intentos que le quedan.
    
    3)Si el usuario supera el numero de intentos permitidos
    entonces el programa le va a decir numero de intentos 
    superados y cuenta bloqueada.
"""
PIN_CORRECTO = "1234"
INTENTOS_MAX = 3
intentos = 0

while intentos < INTENTOS_MAX:
    entrada = input("Ingresa tu pin (4 dígitos): ")
    if entrada == PIN_CORRECTO:
        print("Autenticación exitosa")
        print("Acceso concedido.")
        break
    else:
        intentos += 1
        restantes = INTENTOS_MAX - intentos
        if restantes > 0:
            print(f"Pin incorrecto. Te quedan {restantes} intentos.")
        else:
            print("Pin incorrecto. CUENTA BLOQUEADA. Número de intentos superados.")