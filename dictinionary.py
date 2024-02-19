# Phonebook stored in a dictionary

phonebook = {}

# Add contacts to the phonebook

def add_contact(name, phone_number):
    phonebook[name] = phone_number

# Search for a contact in the phonebook
def search_contact(name):
    if name in phonebook:
        return phonebook[name]
    else:
        return "Contact not found in the phonebook."
    

# Update a contact in the phonebook
    
def update_contact(name, new_phone_number):
    if name in phonebook:
        phonebook[name] = new_phone_number
    else:
        print("Contact not found in the phonebook.")

# Example usage
        

add_contact("Ghanwa", "0306027691")
add_contact("ahmed", "9876543210")
print(search_contact("Ghanwa"))
update_contact("Ghanwa", "9999999999")

print(phonebook)



sentence = input("Urdu sentence likho: ")
words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)


# Grading scale stored in a dictionary

grading_scale = {"A+": 90, "A": 80, "B": 70, "C": 60, "D": 50, "F": 0}

# User input for scores in different subjects

subject_scores = {}
for subject in range(1, 4):
    score = int(input(f"Subject {subject} ka score dalo: "))
    subject_scores[f"Subject {subject}"] = score

# Calculate overall grade
    
total_score = sum(subject_scores.values())
average_score = total_score / len(subject_scores)

# Determine overall grade based on grading scale

for grade, min_score in grading_scale.items():
    if average_score >= min_score:
        overall_grade = grade
        break

print(f"Overall Grade:overall_grades")
# Shopping list stored in a dictionary

shopping_list = {}

# Add items to the shopping list

def add_item(item):
    shopping_list[item] = "Pending"

# Remove items from the shopping list
    
def remove_item(item):
    if item in shopping_list:
        del shopping_list[item]
    else:
        print("Item not found in the shopping list.")

# Check off items on the shopping list
        
def check_off_item(item):
    if item in shopping_list:
        shopping_list[item] = "Done"
    else:
        print("Item not found in the shopping list.")

# Example usage
        
add_item("Milk")
add_item("Bread")
check_off_item("Bread")
remove_item("Milk")

print(shopping_list)

# Shopping list stored in a dictionary

shopping_list = {}

# Add items to the shopping list
def add_item(item):
    shopping_list[item] = "Pending"

# Remove items from the shopping list
def remove_item(item):
    if item in shopping_list:
        del shopping_list[item]
    else:
        print("Item not found in the shopping list.")

# Check off items on the shopping list
def check_off_item(item):
    if item in shopping_list:
        shopping_list[item] = "Done"
    else:
        print("Item not found in the shopping list.")

# Example usage
add_item("Milk")
add_item("Bread")
check_off_item("Bread")
remove_item("Milk")

print(shopping_list)




# Temperature conversion factors stored in a dictionary
conversion_factors = {"Celsius to Fahrenheit": lambda c: c * 9/5 + 32,
                      "Fahrenheit to Celsius": lambda f: (f - 32) * 5/9}

# Example usage to convert Celsius to Fahrenheit
celsius_temp = 30
fahrenheit_temp = conversion_factors["Celsius to Fahrenheit"](celsius_temp)
print(f"{celsius_temp} degrees Celsius is equal to {fahrenheit_temp} degrees Fahrenheit.")




# Temperature conversion factors stored in a dictionary
conversion_factors = {"Celsius to Fahrenheit": lambda c: c * 9/5 + 32,
                      "Fahrenheit to Celsius": lambda f: (f - 32) * 5/9}

# Example usage to convert Celsius to Fahrenheit
celsius_temp = 30
fahrenheit_temp = conversion_factors["Celsius to Fahrenheit"](celsius_temp)
print(f"{celsius_temp} degrees Celsius is equal to {fahrenheit_temp} degrees Fahrenheit.")



menu = {}

def read_menu(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            item, price, category = line.strip().split(',')
            menu[item] = {'price': float(price), 'category': category}

def browse_menu(category=None):
    print("Menu:")
    for item, details in menu.items():
        if category is None or details['category'] == category:
            print(f"{item}: ${details['price']} ({details['category']})")

file_path = input("Enter path to menu file: ")
read_menu(file_path)

while True:
    print("\nOptions:")
    print("1. Browse menu")
    print("2. Search for item")
    print("3. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        category = input("Enter category to browse (leave blank to browse all): ")
        browse_menu(category)
    elif choice == 2:
        item = input("Enter item to search for: ")
        if item in menu:
            print(f"{item}: ${menu[item]['price']} ({menu[item]['category']})")
        else:
            print("Item not found in the menu.")
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")



        
expenses = {}

def add_expense(category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

def display_expenses():
    print("Travel Expenses:")
    for category, amount in expenses.items():
        print(f"{category}: ${amount:.2f}")

while True:
    print("\nOptions:")
    print("1. Add an expense")
    print("2. Display expenses")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        add_expense(category, amount)
        print("Expense added successfully.")
    elif choice == '1':
        display_expenses()
    elif choice == '2':
        break
    else:
        print("Invalid choice. Please try again.")


import random
import string

password_constraints = {'length': 8, 'uppercase': True, 'lowercase': True, 'numbers': True, 'symbols': False}

def generate_password(constraints):
    characters = ''
    if constraints['uppercase']:
        characters += string.ascii_uppercase
    if constraints['lowercase']:
        characters += string.ascii_lowercase
    if constraints['numbers']:
        characters += string.digits
    if constraints['symbols']:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(constraints['length']))

print("Generated password:", generate_password(password_constraints))
