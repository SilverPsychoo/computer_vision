"""
5.1 Problem 1: Sum of integers in a range
the program prompts the user to input a positive integer n and then calculates the sum of all 
integers from 1 to n, as well as the sum of only the even integers in that range.
"""
import numbers


try:
    n_txt = input("Enter a positive integer n: ")
    n = int(n_txt)
    if n < 1:
        raise ValueError("n must be greater than or equal to 1.")
except ValueError:
    print("Error: invalid input. Please enter a positive integer.")
    exit(1)
total_sum = 0
even_sum = 0
for i in range(1, n + 1):
    total_sum += i
    if i % 2 == 0:
        even_sum += i
print(f"Sum 1..n: {total_sum}")
print(f"Even sum 1..n: {even_sum}")




""""
5.2 Problem 2: Multiplication table with for
the program prompts the user to input a base number and a limit m, then prints the 
multiplication table for that base from 1 to m.
"""
try:
    base_txt = int(input("Enter the base number: "))
    m_txt = int(input("Enter the limit m for the multiplication table: "))
    if m_txt < 1:
        raise ValueError("m must be greater than or equal to 1.")
except ValueError:
    print("Error: invalid input. Please enter valid integers.")
    exit(1)
for i in range(1, m_txt + 1):
    result = base_txt * i
    print(f"{base_txt} x {i} = {result}")
    
"""
5.3 Problem 3: Average of numbers with while and sentinel
the program prompts the user to input numbers one by one until they enter a sentinel value (e.g., -1) 
to indicate they are finished. The program then calculates and displays the average of the entered 
numbers, excluding the sentinel value. If no valid numbers were entered, it should display an error message.
"""
sentinel_value = -1
count = 0
total_sum = 0.0
while True:
    try:
        number_txt = input("Enter a number (or -1 to finish): ")
        number = float(number_txt)
        if number < 0 and number != sentinel_value:
            print("Error: invalid input. Please enter a non-negative number or -1 to finish.")
            continue
    except ValueError:
        print("Error: invalid input. Please enter a valid number.")
        continue
    if number == sentinel_value:
        break
    total_sum += number
    count += 1
if count > 0:
    average_value = total_sum / count
    print(f"Count: {count}")
    print(f"Average: {average_value}")
else:
    print("Error: no data")
""""
5.4 Problem 4: Password attempts with while
the program defines a correct password and allows the user to attempt to enter it up to a 
maximum number of attempts (e.g., 3).
"""
MAX_ATTEMPTS = 3
correct_password = "holasoylacontraseñacorrecta"
attempts = 0
while attempts < MAX_ATTEMPTS:
    user_password = input("Enter the password: ")
    if user_password == correct_password:
        print("Login success")
        break
    else:
        print("Incorrect password. Try again.")
        attempts += 1
if attempts == MAX_ATTEMPTS:
    print("Account locked")
""""
5.5 Problem 5: Simple menu with while
the program implements a simple text-based menu that repeatedly prompts the user to select an option
until they choose to exit.
"""
counter = 0
option = -1
while option != 0:
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")
    option_input = input("Select an option: ")
    try:
        option = int(option_input)
    except ValueError:
        print("Error: invalid option")
        continue
    if option == 1:
        print("Hello!")
    elif option == 2:
        print(f"Counter: {counter}")
    elif option == 3:
        counter += 1
        print("Counter incremented")
    elif option == 0:
        print("Bye!")
    else:
        print("Error: invalid option")
""""
5.6 Problem 6: Pattern printing with nested loops
the program prompts the user to input a positive integer n and then prints a right-angled triangle
pattern of asterisks (*) with n rows.
"""
try:    
    n = int(input("Enter the number of rows for the pattern: "))
    if n < 1:
        raise ValueError("n must be greater than or equal to 1.")
except ValueError:
    print("Error: invalid input. Please enter a positive integer.")
    exit(1)
for i in range(1, n + 1):
    line = ""
    for j in range(i):
        line += "*"
    print(line)
