"""
5.1 Problem 1: Rectangle area and perimeter (basic functions)
the program defines two functions to calculate the area and perimeter of a rectangle given its width and height.
The program prompts the user to input the width and height, calls the functions, and displays the
"""
def calculate_area(width, height):
    return width * height
def calculate_perimeter(width, height):
    return 2 * (width + height)

try:
    width_txt = input("Enter the width of the rectangle: ")
    height_txt = input("Enter the height of the rectangle: ")
    width = float(width_txt)
    height = float(height_txt)
    if width <= 0 or height <= 0:
        print("Error: invalid input")
    else:
        area = calculate_area(width, height)
        perimeter = calculate_perimeter(width, height)
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
except ValueError:
    print("Error: invalid input")
    exit(1)

"""
5.2 Problem 2: Grade classifier (function with return string)
the program defines a function to classify a numeric grade into letter categories (A, B, C, D, F).
The program prompts the user to input a grade score, calls the function, and displays the score and
its category.
"""

try:
    score_txt = input("Enter the grade score (0-100): ")
    score = float(score_txt)
except ValueError:
    print("Error: invalid input")
    exit(1)
def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
if score < 0 or score > 100:
    print("Error: invalid input")
else:
    category = classify_grade(score)
    print(f"Score: {score}")
    print(f"Category: {category}")
    
"""
5.3 Problem 3: List statistics function (min, max, average)
the program defines a function to calculate and return the minimum, maximum, and average of a list of numbers.
The program prompts the user to input a list of numbers (comma-separated), calls the function, and displays the results.
"""

numbers_text = input("Enter a list of numbers separated by commas: ").strip()
if not numbers_text:
    print("Error: invalid input")
    exit(1)
try:
    numbers_list = [float(num.strip()) for num in numbers_text.split(",")]
    if not numbers_list:
        print("Error: invalid input")
        exit(1)
except ValueError:
    print("Error: invalid input")
    exit(1)
def summarize_numbers(numbers_list):
    min_value = min(numbers_list)
    max_value = max(numbers_list)
    average_value = sum(numbers_list) / len(numbers_list)
    return {
        "min": min_value,
        "max": max_value,
        "average": average_value
    }
summary = summarize_numbers(numbers_list)
print(f"Min: {summary['min']}")
print(f"Max: {summary['max']}")
print(f"Average: {summary['average']}")

"""
5.4 Problem 4: Apply discount list (pure function = no modificar la entrada, sin efectos secundarios)
the program defines a function to apply a discount rate to a list of prices and return a new list with the discounted prices.
"""
prices_text = input("Enter a list of prices separated by commas: ").strip()
discount_rate_text = input("Enter the discount rate (e.g., 0.10 for 10%): ").strip()
if not prices_text:
    print("Error: invalid input")
    exit(1)
try:
    prices_list = [float(price.strip()) for price in prices_text.split(",")]
    discount_rate = float(discount_rate_text)
    if not prices_list or any(price <= 0 for price in prices_list):
        print("Error: invalid input")
        exit(1)
    if discount_rate < 0 or discount_rate > 1:
        print("Error: invalid input")
        exit(1)
except ValueError:
    print("Error: invalid input")
    exit(1)
def apply_discount(prices_list, discount_rate):
    discounted_list = []
    for price in prices_list:
        discounted_price = price * (1 - discount_rate)
        discounted_list.append(discounted_price)
    return discounted_list
discounted_prices = apply_discount(prices_list, discount_rate)
print(f"Original prices: {prices_list}")
print(f"Discounted prices: {discounted_prices}")

"""
5.5 Problem 5: Greeting function with default parameters
the program defines a function to generate a greeting message. The function takes a name and an optional title (default is an empty string).
The program prompts the user to input a name and an optional title, calls the function, and displays the greeting message.
"""
def greet(name, title=""):
    name = name.strip()
    title = title.strip()
    if not name:
        return "Error: invalid input"
    full_name = f"{title} {name}" if title else name
    return f"Hello, {full_name}!"
try:
    name_input = input("Enter the name: ")
    title_input = input("Enter the title (optional): ")
    if not name_input.strip():
        raise ValueError("Name cannot be empty.")
    greeting_message = greet(name_input, title_input)
    print(f"Greeting: {greeting_message}")
except ValueError:
    print("Error: invalid input")
    exit(1)
    
"""
5.6 Problem 6: Factorial function (iterative or recursive)
the program defines a function to calculate the factorial of a non-negative integer n.
The program prompts the user to input n, calls the function, and displays the factorial value.
"""
def factorial(n):
    # iterative implementation to avoid recursion limit issues for larger n
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
try:
    n_txt = input("Enter a non-negative integer n (max 20): ")
    n = int(n_txt)
    if n < 0 or n > 20:
        print("Error: invalid input")
        exit(1)
except ValueError:
    print("Error: invalid input")
    exit(1)
fact_value = factorial(n)
print(f"Factorial of {n} is {fact_value}")
