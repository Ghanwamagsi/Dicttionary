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
