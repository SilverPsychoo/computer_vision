"""
Problema:1 palindrome checker
"""
try:
    phrase = input("Escribe tu frase: ").strip()
except ValueError:
    print("Error al procesar la entrada.")
else:
    if not phrase:
        print("La frase está vacía.")
    else:
        cleaned = ''.join(c.lower() for c in phrase if c.isalnum()) [-1]
        is_palindrome = cleaned == cleaned[::-1]
        if is_palindrome:
            print("Es un palíndromo")
        else:        
            print("No es un palíndromo")
    
"""
Problema 2: Calificacion de estudiantes con  lista y diccionarios
"""

students_list = [
    {"nombre": "Isabella", "calif": [100, 95, 90]},
    {"nombre": "Erick", "calif": [70, 75, 70]},
    {"nombre": "Gladis", "calif": [90, 85, 80]},
    {"nombre": "Charly", "calif": [65, 50, 60] },]

try:
    search_name = input("Ingrese el nombre del estudiante: ").strip()
except ValueError:
    print("Error al procesar la entrada.")

if search_name:
    found_student = None
    for student in students_list:
        if student["nombre"] == search_name:
            found_student = student
            break

    if found_student:
        average = sum(found_student["calif"]) / len(found_student["calif"])
        grades = found_student["calif"]
        passed = average >= 70
        print(f"El promedio de {found_student['nombre']} es: {average}")
        print(f"Calificaciones: {grades}")
        if passed:
            print("El estudiante ha aprobado.")
        else:
            print("El estudiante no ha aprobado.")
    else:
        print("Estudiante no encontrado.")
else:
    print("Nombre vacío.")

"""
Oportunidades de contraseña (3 intentos) con while
"""
correct_password = "pasemeprofesor"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    try:
        user_input = input("Ingrese la contraseña: ").strip()
    except ValueError:
        print("Error al procesar la entrada.")
        continue

    if user_input == correct_password:
        print("Contraseña correcta. Acceso concedido.")
        break
    else:
        attempts += 1
        print(f"Contraseña incorrecta. Intento {attempts} de {max_attempts}.")
        
"""
Pregunta (10 puntos): ¿Qué ventajas tiene usar funciones en un programa? Menciona al menos tres 
beneficios (por ejemplo, en legibilidad, reutilización y pruebas)
Cuando tienes un comando largo, que resuelve una cosa en común, para facilitarte el mundo, en vez de
escribir comando por comando, cada vez que necesites realizar lo que vayas a hacer, mejor usas una
funcion a la que le escibes esos comandos una sola vez, y listo, solamente cuando necesites llamarlo, 
llamas solo a la función y ya, lo que haces es ahorrarte trabajo, tener un codigo mas corto y mejor 
factorizado y que la gente pueda entender que rollo lo que esta sucediendo
"""