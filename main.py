# Create list of names
import random

file = open("super_villains.txt")

name_list = []
for line in file:
    line = line.strip()
    name_list.append(line)

key = "Morgiana the Shrew"

i = 0
while i < len(name_list) and name_list[i] != key:
    i += 1

if i < len(name_list):
    print("The name is at position", i)
else:
    print("The name was not found.")

# Create Alien class
class Alien:
    """ Define alien attributes"""
    def __init__(self, color, weight):
        """Constructor: set name and color"""
        self.color = color
        self.weight = weight

# Function to check if item has a property
def has_property(my_alien):
    if my_alien.color.lower() == "green":
        return True
    else:
        return False

def while_check(my_list):
    i = 0
    while i < len(my_list) and not has_property(my_list[i]):
        i += 1
    if i < len(my_list):
        return True
    else:
        return False

def for_check(my_list):
    for i in my_list:
        if has_property(i):
            return True
    return False

def binary_check(my_list, search_item):
    key = search_item
    lower_bound = 0
    upper_bound = len(my_list) - 1
    found = False

    while lower_bound < upper_bound and not found:
        middle_pos = (lower_bound + upper_bound) // 2

        if my_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif my_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True
    if found:
        print("YES !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return middle_pos
    else:
        return False

random_list = []
for i in range(1000):
    for p in range(1000):
        random_list.append(random.randrange(100000000))
    print(binary_check(random_list, 500))
    random_list.clear()



file.close()