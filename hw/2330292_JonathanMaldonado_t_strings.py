"""
5.1 Problem 1: Full name formatter (name + initials)
 program that prompts the user to input their full name (first name, middle name(s), and last name).
 then formats the name in a standardized way (e.g., capitalizing the first letter of each name and ensuring proper spacing) and also extracts the initials of the name. Finally, it should display both the formatted full name and the initials to the user.
"""


#the user is prompted to input their full name
try:
    full_name = input("Enter your full name: ")
    if not full_name.strip():
        raise ValueError("The name cannot be empty or only spaces.")
except ValueError:
    print("Invalid input. Please enter a valid full name.")
    exit(1)

# Normalizing spaces
normalized_name = " ".join(full_name.strip().split())
# Capitalizing each word
formatted_name = normalized_name.title()
# Extracting initials
initials = ''.join([word[0].upper() + '.' for word in normalized_name.split()])
# Displaying results
print(f"Formatted name: {formatted_name}")
print(f"Initials: {initials}")

"""
5.2 Problem 2: Simple email validator (structure + domain)
Write a program that prompts the user to input an email address and then validates 
whether the email address is in a correct format. The program should check for the presence of an "@"
symbol, ensure that there are no spaces, and verify that there is a valid domain structure (e.g., something like "example.com"). 
If the email address is valid, the program should print "Valid email: True" and display the domain part of the email. If the email address is invalid, it should print "Valid email: False".
"""

try:
    email_text = input("Enter an email address: ")
    if not email_text.strip():
        raise ValueError("The email address cannot be empty or only spaces.")
except ValueError:
    print("Invalid input. Please enter a valid email address.")
    exit(1)
# Validating email structure
if email_text.count('@') == 1 and ' ' not in email_text:
    local_part, domain_part = email_text.split('@')
    if '.' in domain_part:
        print("Valid email: True")
        print(f"Domain: {domain_part}")
    else:
        print("Valid email: False")
else:
    print("Valid email: False")

"""
5.3 Problem 3: Palindrome checker (ignoring spaces and case)
Program that prompts the user to input a phrase and then checks if the phrase is a palindrome, ignoring spaces and case sensitivity. 
The program should normalize the input by removing spaces and converting all characters to the same case (either upper or lower)
before performing the palindrome check. Finally, it should display whether the input phrase is a palindrome or not.
"""

try:
    phrase = input("Enter a phrase to check if it is a palindrome: ")
    if not phrase.strip():
        raise ValueError("The phrase cannot be empty or only spaces.")
except ValueError:
    print("Invalid input. Please enter a valid phrase.")
    exit(1)
# Normalizing the phrase
normalized_phrase = phrase.replace(" ", "").lower()
# Checking if the normalized phrase is a palindrome
is_palindrome = normalized_phrase == normalized_phrase[::-1]
print(f"Is palindrome: {is_palindrome}")

"""
5.4 Problem 4: Sentence word statistics (lengths and first/last word)
the program prompts the user to input a sentence and then analyzes the sentence to provide various statistics about the words it contains.
The program should count the total number of words in the sentence, identify the first and last word, and determine the shortest and longest word based on their lengths.
"""

try:
    sentence = input("Enter a sentence to analyze: ")
    if not sentence.strip():
        raise ValueError("The sentence cannot be empty or only spaces.")
except ValueError:
    print("Invalid input. Please enter a valid sentence.")
    exit(1)
# Normalizing spaces
normalized_sentence = sentence.strip()
# Splitting into words
words = normalized_sentence.split()
if not words:
    print("No valid words found in the sentence.")
    exit(1)
# Word count
word_count = len(words)
# First and last word
first_word = words[0]
last_word = words[-1]
# Finding shortest and longest word
shortest_word = min(words, key=len)
longest_word = max(words, key=len)
# Displaying results
print(f"Word count: {word_count}")
print(f"First word: {first_word}")
print(f"Last word: {last_word}")
print(f"Shortest word: {shortest_word}")
print(f"Longest word: {longest_word}")

"""
5.5 Problem 5: Password strength classifier
The program prompts the user to input a password and then evaluates the strength of the password based on certain criteria.
The program should check for the presence of uppercase letters, lowercase letters, digits, and special characters
"""

try:
    password_input = input("Enter a password to evaluate its strength: ")
    if not password_input.strip():
        raise ValueError("The password cannot be empty or only spaces.")
except ValueError:
    print("Invalid input. Please enter a valid password.")
    exit(1)
# Evaluating password strength
has_upper = any(char.isupper() for char in password_input)
has_lower = any(char.islower() for char in password_input)
has_digit = any(char.isdigit() for char in password_input)
has_symbol = any(not char.isalnum() for char in password_input)
length = len(password_input)
if length < 8 or (password_input.islower() and not has_digit and not has_symbol):
    strength = "weak"
elif length >= 8 and ((has_upper and has_lower) or (has_digit and (has_upper or has_lower))):
    strength = "medium"
elif length >= 8 and has_upper and has_lower and has_digit and has_symbol:
    strength = "strong"
else:
    strength = "weak"
print(f"Password strength: {strength}")

"""
5.6 Problem 6: Product label formatter (fixed-width text)
the program prompts the user to input a product name and its price, then formats this information into a fixed-width label suitable for display.
The label should include the product name and price, formatted in a way that ensures the total length of the label does not exceed 30 characters.
"""
try:
    product_name = input("Enter the product name: ").strip()
    if not product_name.strip():
        raise ValueError("The product name cannot be empty or only spaces.")

    price_input = input("Enter the product price: ")
    price_value = float(price_input)
    if price_value <= 0:
        raise ValueError

except ValueError:
    print("Entrada inválida. Por favor, ingrese un nombre de producto válido y un precio positivo.")
    exit(1)

label = f"Product: {product_name} | Price: ${price_value}"

if len(label) > 30:
    label = label[:30]
else:
    label = label.ljust(30)

print(f"Label: '{label}'")


