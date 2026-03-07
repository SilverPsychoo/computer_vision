#Este programa pide al usuario ingresar una cantidad en pesos mexicanos,
#también pide el porcentaje de IVA y el porcentaje de propina.
#El programa debe calcular el monto total a pagar por el usuario

subtotal = input("Subtotal(MXN): ")
iva_txt = input("IVA (%): ej. 16: ")
propina_txt = input("Propina (%): ej. 10: ")

try:
    #Metodo built-in float(1 argument)- Convierte a un dato del tipo flotante
    subtotal = float(subtotal)
    iva = float(iva_txt)/100
    propina = float(propina_txt)/100
except ValueError:
    print("Entrada invalida. Utiliza números:")
    exit(1)
    
monto_iva = subtotal * iva
monto_propina = subtotal * propina
total = subtotal + monto_iva + monto_propina

print(f"Subtotal: {subtotal}")
print(f"IVA: {monto_iva}")
print(f"Propina: {monto_propina}")
print(f"Total: {total}")

