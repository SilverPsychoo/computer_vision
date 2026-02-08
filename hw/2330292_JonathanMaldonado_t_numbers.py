""""
5.1 Problem 1: Temperature converter and range flag
The program prompts the user to input a temperature in Celsius and then converts it to Fahrenheit and Kelvin. 
Additionally, it checks if the temperature is considered "high" (30 degrees Celsius or above) and displays a boolean flag indicating this.
"""
try:
    temp_c_input = float(input("Enter a temperature in Celsius: "))
except ValueError:
    print("Error: invalid input. Please enter a numeric value.")
    exit(1)

temp_f = temp_c_input * 9 / 5 + 32
temp_k = temp_c_input + 273.15
is_high_temperature = (temp_c_input >= 30.0)
print(f"Fahrenheit: {temp_f}")
print(f"Kelvin: {temp_k}")
print(f"High temperature: {is_high_temperature}")

"""
5.2 Problem 2: Work hours and overtime payment
the program prompts the user to input the number of hours worked in a week and the hourly rate.
The program calculates the total pay for the week, taking into account that any hours worked beyond 40 hours are considered overtime and are paid at 1.5 times the regular hourly rate.
"""
try:
    hours_worked = int(input("Enter hours worked in the week: "))
    hourly_rate = float(input("Enter hourly rate: "))
except ValueError:
    print("Error: invalid input. Please enter numeric values.")
    exit(1)
    
if hours_worked < 0 or hourly_rate <= 0:
    print("Error: invalid input.")
else:
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(0, hours_worked - 40)
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay
    has_overtime = (hours_worked > 40)
    print(f"Regular pay: {regular_pay}")
    print(f"Overtime pay: {overtime_pay}")
    print(f"Total pay: {total_pay}")
    print(f"Has overtime: {has_overtime}")

"""
5.3 Problem 3: Discount eligibility with booleans
the program prompts the user to input the total purchase amount and whether the customer is a student or a senior citizen.
The program then determines if the customer is eligible for a discount based on the following criteria:
"""

try:
    purchase_total = float(input("Enter the total purchase amount: "))
except ValueError:
    print("Error: invalid input. Please enter a numeric value.")
    exit(1)
is_student_text = input("Is the customer a student? (YES/NO): ").strip().upper()
is_senior_text = input("Is the customer a senior? (YES/NO): ").strip().upper()
if purchase_total < 0.0:
    print("Error: invalid input.")
    exit(1)
if is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
    print("Error: invalid input.")
    exit(1)
is_student = (is_student_text == "YES")
is_senior = (is_senior_text == "YES")
discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
final_total = purchase_total * 0.9 if discount_eligible else purchase_total
print(f"Discount eligible: {discount_eligible}")
print(f"Final total: {final_total}")


""""
5.4 Problem 4: Basic statistics of three integers
The program prompts the user to input three integers and then calculates and displays the 
sum, average, maximum, minimum, and a boolean flag indicating whether all three integers are even.
"""
try:
    n1 = int(input("Enter the first integer: "))
    n2 = int(input("Enter the second integer: "))  
    n3 = int(input("Enter the third integer: "))
except ValueError:
    print("Error: invalid input. Please enter integer values.")
    exit(1)
sum_value = n1 + n2 + n3
average_value = sum_value / 3
max_value = max(n1, n2, n3)
min_value = min(n1, n2, n3)
all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
print(f"Sum: {sum_value}")
print(f"Average: {average_value}")
print(f"Max: {max_value}")
print(f"Min: {min_value}")
print(f"All even: {all_even}")

"""
5.5 Problem 5: Loan eligibility (income and debt ratio)
the program prompts the user to input their monthly income, monthly debt, and credit score.
The program then calculates the debt-to-income ratio and determines if the user is eligible for a loan
"""
try:
    monthly_income = float(input("Enter monthly income: "))
    monthly_debt = float(input("Enter monthly debt: "))
    credit_score = int(input("Enter credit score: "))
except ValueError:
    print("Error: invalid input. Please enter numeric values.")
    exit(1)
if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
    print("Error: invalid input.")
else:
    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)
    print(f"Debt ratio: {debt_ratio}")
    print(f"Eligible: {eligible}")

"""
the program prompts the user to input their weight in kilograms and height in meters, 
then calculates the Body Mass Index (BMI) and determines if the person is underweight, 
normal weight, or overweight based on standard BMI categories.
"""

try:
    weight_kg = float(input("Peso (kg): "))
    height_m = float(input("Altura (m): "))
except ValueError:
    print("Error: invalid input. Please enter numeric values.")
    exit(1)
if weight_kg <= 0.0 or height_m <= 0.0:
    print("Error: invalid input.")
else:
    bmi = weight_kg / (height_m * height_m)
    bmi_rounded = round(bmi, 2)
    is_underweight = (bmi < 18.5)
    is_normal = (18.5 <= bmi < 25.0)
    is_overweight = (bmi >= 25.0)
    print(f"BMI: {bmi_rounded}")
    print(f"Underweight: {is_underweight}")
    print(f"Normal: {is_normal}")
    print(f"Overweight: {is_overweight}")