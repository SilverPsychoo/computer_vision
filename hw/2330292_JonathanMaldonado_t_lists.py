"""
5.1 Problem 1: Shopping list basics (list operations)
the program prompts the user to input a list of items (as a comma-separated string),
then allows the user to add a new item to the list and search for an item within the list.o
"""
try:
    initial_items_text = input("Enter initial items (format: item:quantity, e.g., apple:2,banana:5): ")
    new_item = input("Enter a new item to add (format: item:quantity): ")
    search_item = input("Enter an item to search for: ")
    
    if not initial_items_text.strip():
        raise ValueError("Initial items cannot be empty.")
    if not new_item.strip():
        raise ValueError("New item cannot be empty.")
    if not search_item.strip():
        raise ValueError("Search item cannot be empty.")
    
    # Process initial items
    items_list = []
    for item in initial_items_text.split(','):
        item = item.strip()
        if item:
            items_list.append(item.lower())
    
    # Add new item
    items_list.append(new_item.strip().lower())
    
    # Check if search item is in the list
    is_in_list = search_item.strip().lower() in items_list
    
    # Output results
    print(f"Items list: {items_list}")
    print(f"Total items: {len(items_list)}")
    print(f"Found item: {is_in_list}")
except ValueError:
    print("Invalid input. Please follow the specified formats.")

"""
5.2 Problem 2: Points and distances with tuples
the program prompts the user to input the coordinates of two points in a 2D space (as tuples),
then calculates and displays the distance between the points and the midpoint.
"""
try:
    x1 = float(input("Enter x1 coordinate of Point A: "))
    y1 = float(input("Enter y1 coordinate of Point A: "))
    x2 = float(input("Enter x2 coordinate of Point B: "))
    y2 = float(input("Enter y2 coordinate of Point B: "))
    point_a = (x1, y1)
    point_b = (x2, y2) 
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    midpoint = ((x1 + x2)/2, (y1 + y2)/2)
    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {distance}")
    print(f"Midpoint: {midpoint}")
except ValueError:
    print("Invalid input. Please enter numeric values for coordinates.")

"""
5.3 Problem 3: Product catalog with dictionary
the program defines a product catalog using a dictionary where the keys are product names and the values are their prices.
The user is prompted to input a product name and a quantity to buy.
"""
product_prices = {
    "apple": 10.0,
    "banana": 5.0,
    "orange": 8.0,
    "chicken": 50.0,
    "bread": 20.0,
    "beef": 100.0
}
print("Available products:", product_prices)
try:
    product_name = input("Enter the product name: ").strip().lower()
    quantity_txt = input("Enter the quantity to buy: ")
    if not product_name:
        raise ValueError("Product name cannot be empty.")
    quantity = int(quantity_txt)
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    if product_name in product_prices:
        unit_price = product_prices[product_name]
        total_price = unit_price * quantity
        print(f"Unit price: {unit_price}")
        print(f"Quantity: {quantity}")
        print(f"Total: {total_price}")
    else:
        print("Error: product not found")
except ValueError:
    print("Invalid input. Please enter a valid product name and a positive integer quantity.")  
     
"""
5.4 Problem 4: Student grades with dict and list
the program defines a dictionary where the keys are student names and the values are lists of their grades.
The user is prompted to input a student's name, and the program calculates and displays the student's average
"""
grades = {
    "Isabella": [95.0, 90.0, 100.0],
    "Gladis": [92.0, 88.0, 95.0],
    "Erick": [70.0, 65.0, 80.0],
    "Brandon": [50.0, 60.0, 55.0],
}
print("Available students:", grades)
try:
    student_name = input("Enter the student's name: ").strip()
    if not student_name:
        raise ValueError("Student name cannot be empty.")
    if student_name in grades:
        student_grades = grades[student_name]
        if not student_grades:
            raise ValueError("No grades available for this student.")
        average = sum(student_grades) / len(student_grades)
        is_passed = average >= 70.0
        print(f"Grades: {student_grades}")
        print(f"Average: {average}")
        print(f"Passed: {is_passed}")
    else:
        print("Error: student not found")   
except ValueError:
    print("Invalid input. Please enter a valid student name.")

"""
5.5 Problem 5: Word frequency counter (list + dict)
the program prompts the user to input a sentence, then counts the frequency of each word in the sentence using a dictionary.
The program also identifies and displays the most common word.
"""

try:
    sentence = input("Enter a sentence: ")
    if not sentence.strip():
        raise ValueError("The sentence cannot be empty or only spaces.")
except ValueError:
    print("Invalid input. Please enter a valid sentence.")
    exit(1)
# Normalizing the sentence: converting to lowercase and removing basic punctuation
normalized_sentence = sentence.lower()
for char in ".,!?;:":
    normalized_sentence = normalized_sentence.replace(char, "")
# Splitting into words
words_list = normalized_sentence.split()
if not words_list:
    print("No valid words found in the sentence.")
    exit(1)
# Building frequency dictionary
freq_dict = {}
for word in words_list:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1
# Finding the most common word
most_common_word = max(freq_dict, key=freq_dict.get)
# Displaying results
print(f"Words list: {words_list}")
print(f"Frequencies: {freq_dict}")
print(f"Most common word: {most_common_word}")

"""
5.6 Problem 6: Simple address book (dictionary CRUD)
the program implements a simple address book using a dictionary where the keys are contact names and the values are their phone numbers.
The user is prompted to input an action (ADD, SEARCH, DELETE) and a contact name.
"""
contacts = {
    "Isabella": "8345678901",
    "Erick": "8341310904",
    "Charly": "5545333530"
}
action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()
if action_text not in ("ADD", "SEARCH", "DELETE"):
    print("Error: invalid action.")
    exit(1)
name = input("Enter contact name: ").strip().title()
if not name:
    print("Error: name cannot be empty.")
    exit(1)
if action_text == "ADD":
    phone = input("Enter contact phone: ").strip()
    if not phone:
        print("Error: phone cannot be empty.")
        exit(1)
    contacts[name] = phone
    print(f"Contact saved: {name} {phone}") 
elif action_text == "SEARCH":
    if name in contacts:
        print(f"Phone: {contacts[name]}")
    else:
        print("Error: contact not found")
elif action_text == "DELETE":
    if name in contacts:
        contacts.pop(name)
        print(f"Contact deleted: {name}")
    else:
        print("Error: contact not found")
