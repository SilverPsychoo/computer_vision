names = []
print(names)

#Método append para agregar elementos al final de la lista
names.append("Jonathan")
names.append("Isabella")
names.append("Gladis")
names.append("Yadira")
names.append("Yeimi")

print(names)
print(type(names))
print(len(names))

#Método insert para agregar elementos en una posición específica
names.insert(0, "Erick") 
print(names)

#Método pop() para eliminar el último elemento de la lista
names.pop()
print(names)

#Método pop() con índice para eliminar un elemento en una posición específica
names.pop(3)
print(names)

#Método remove() para eliminar un elemento por su valor
names.remove("Yadira")
names.remove("Erick")
print(names)