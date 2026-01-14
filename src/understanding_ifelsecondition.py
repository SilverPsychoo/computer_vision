user_age = int(input("Ingresa tu edad: "))

if user_age < 0:
    print("Edad inválida.")
elif user_age < 18:
    print("Eres menor de edad.")
elif user_age < 60 and user_age >= 18:
    print("Eres adulto.")
elif 60 <= user_age < 100:
    print("Eres adulto mayor.")
else:
    print("Descansa en paz.")
    
