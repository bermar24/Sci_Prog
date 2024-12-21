# Ubuntu/Linux Mint:
# sudo apt-get update && sudo apt-get install python3 python3-pip

# TODO: whit this i can resalt a coment ( Implement a function...)

# Arithmetic operations
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333333333333335
print(a // b)  # Output: 3
print(a ** b)  # Output: 1000
print(a % b)  # Output: 1 (remainder of 10 / 3)

# type conversor
a = 10
b = float(a)  # Convert integer to float
c = int(3.14)  # Convert float to integer
d = str(a)  # Convert to string

# Indexing
name = "Oleg"
print(name[0])  # Output: O
print(name[2])  # Output: e

# Logical operations
# and (Logical AND): Returns True if both expressions are true (True and False -> False).
# or (Logical OR): Returns True if at least one of the expressions is true (True or False -> True).
# not (Logical NOT): Returns the inverse value of the expression (not True -> False).

# Comparison operators
# ==: Returns; True if the two values are equal.
# !=: Returns; True if the two values are not equal.
# >: Returns; True if the left value is greater than the right value.
# <: Returns; True if the left value is less than the right value.
# >=: Returns; True if the left value is greater than or equal to the right value.
# <=: Returns; True if the left value is less than or equal to the right value.

# increas int value - or + a value
index = 0
index -= 1
index += 1

#TODO Creating lists
friends = ["Tim", "Oleg", "Emely", "Niklas"]
numb = [1, 2, 3.32, 4, 5.0]
mixed_list = ["Apple", 3.14159, True, "D"]
empty_list = []

animals = ["Rabbit", "Horse", "Dog"]
print(animals[1])  # Output: Horse
print(animals[-1])  # Output: Dog

favorite_foods = ['Cake']
favorite_foods.append('Apples')
favorite_foods.insert(0, 'Frosted Donut')
print(favorite_foods)  # Output: ['Frosted Donut', 'Cake', 'Apples']

favorite_foods.remove("Apples")
favorite_foods.pop(0)  # Removes the first element
print(favorite_foods)  # Output: ['Cake']

fruits = ['Apple', 'Potato', 'Banana']
fruits[2] = 'Pineapple'
print(fruits)  # Output: ['Apple', 'Pineapple', 'Banana']

#TODO Slicing
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[2:4])  # Output: [3, 4]
print(numbers[2:5:2])  # Output: [3, 5]
print(numbers[:4:2])   # Output: [1, 3]
print(numbers[1::3])   # Output: [2, 5]
print(numbers[3:])     # Output: [4, 5, 6]
print(numbers[:4])     # Output: [1, 2, 3, 4]
print(numbers[::2])    # Output: [1, 3, 5]
print(numbers[::-1])   # Output: [6, 5, 4, 3, 2, 1]
print(numbers[::])     # Output: [1, 2, 3, 4, 5, 6]

#TODO Matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\

#TODO for Loops

# for Loops with range()
# The range() function is often used in for loops to perform a specific number of iterations. It can be used in different ways:
# range(n) generates a sequence from 0 to n-1.
# range(start, stop) generates a sequence from start to stop-1.
# range(start, stop, step) adds a step value.

# "break" statement is used within the loop to terminate it prematurely
# "continue" it skips the rest of the current iteration and jumps to the next iteration immediately.

# TODO Functions
def greet_people(name1, name2):
    print("Hello " + name1 + " and " + name2 + "!")
greet_people("Kelly", "Oleg")  # Output: Hello Kelly and Oleg!

# Functions can return values using the return # statement.


# TODO Recursion
def fac(n):
    if n <= 1:
        return 1
    return n * fac(n - 1)

# TODO: Dictionaries
band = {"name": "Sixelle", "genre": "Rock", "city": "Munich", "members": 7}
print(band["name"])  # Output: Sixelle
print(band["city"])  # Output: Munich

# add
fruit = {"type": "Apple", "color": "Red"}
fruit["variety"] = "Pink Lady"
print(fruit)  # Output: {'type': 'Apple', 'color': 'Red', 'variety': 'Pink Lady'}
# mod
fruit["color"] = "Green"
print(fruit)  # Output: {'type': 'Apple', 'color': 'Green', 'variety': 'Pink Lady'}
# del
del fruit["variety"]
print(fruit)  # Output: {'type': 'Apple', 'color': 'Green'}

# Methods
band = {"name": "Sixelle", "genre": "Rock"}
print(band.keys())  # Output: dict_keys(['name', 'genre'])
print(band.values())  # Output: dict_values(['Sixelle', 'Rock'])
print(band.items())  # Output: dict_items([('name', 'Sixelle'), ('genre', 'Rock')])

def vorkommen(liste):
    # Initialisiere ein leeres Dictionary
    vorkommen_dict = {}

    # Iteriere über jedes Element in der Liste
    for zahl in liste:
        # Wenn die Zahl bereits als Schlüssel im Dictionary existiert, erhöhe den Wert
        if zahl in vorkommen_dict:
            vorkommen_dict[zahl] += 1
        else:
            # Andernfalls füge die Zahl mit dem Wert 1 hinzu
            vorkommen_dict[zahl] = 1

    return vorkommen_dict

def schranke(keys, vals, schwelle):
    # Erstelle ein leeres Dictionary
    result = {}

    # Durchlaufe beide Listen mit zip, um Schlüssel-Wert-Paare zu kombinieren
    for key, val in zip(keys, vals):
        # Füge das Paar zum Dictionary hinzu, wenn der Wert größer als die Schwelle ist
        if val > schwelle:
            result[key] = val

    return result

# TODO: Modules

# import x
# from x import y, z
# The "math" module for mathematical functions.
# The "os" module for interacting with the operating system.
# The "sys" module for accessing functions closely tied to the Python interpreter.

# TODO: Object-Oriented Programming (OOP)
# The principle of object-oriented programming (OOP) is a programming paradigm based on the concept of "objects," which contain data and methods. Objects are instances of classes that act as templates, defining the attributes (properties) and behavior (methods) of the objects.
# OOP focuses on dividing software into reusable and modular components, making the code more structured and easier to maintain.

# TODO: Classes
class Person:
    def __init__(self, name, age, height): #A common mistake is forgetting to include self as the first parameter in a method, which leads to errors. So don’t forget it!
        self.name = name
        self.age = age
        self.height = height
# Creating Objects
wil = Person("Will", 19, 189)

# TODO: Methods
# Methods are functions defined within a class and determine the behavior of objects.
# They can access and modify the data (attributes) belonging to an object.
class Person:
    def __init__(self, name, age, height): #Most methods have self as the first parameter. When calling such a method, you do not pass an argument for this parameter—it is handled automatically.
        self.name = name
        self.age = age
        self.height = height

    def birthday(self):
        self.age += 1
        print("Happy Birthday, Will! You are now " + str(self.age) + " years old.")

will = Person("Will", 19, 189)
will.birthday()
# One year later...
will.birthday()

class Inbox:
    def __init__(self, address):
        self.address = address
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(self.address + ": New contact " + contact.address)

    def send_message(self, recipient, message):
        if recipient not in self.contacts:
            print(recipient.address + " is not in your contacts!")
            return
        print(self.address + ': Message "' + message + '" sent to ' + recipient.address)
        recipient.__receive_message(self, message)

    def __receive_message(self, sender, message): #When a method name starts with two underscores (__)
        print(self.address + ': New message from ' + sender.address + ': "' + message + '"')

andrea = Inbox("andrea@web.de")
harry = Inbox("harry@gmx.de")
andrea.send_message(harry, 'Hello!')
andrea.add_contact(harry)
andrea.send_message(harry, 'Hello!')

#TODO: Inheritance – Reusing Classes
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def introduction(self):
        return f"Hi, I’m {self.name}, and I’m {self.age} years old."

class Student(Person):
    def __init__(self, name, age, height, student_number, program):
        super().__init__(name, age, height) #super() Function
        self.student_number = student_number
        self.program = program

    def introduction(self):
        return f"{super().introduction()} I study {self.program}, and my student number is {self.student_number}."
        # super() Function  is used to call the introduction() method of the Person class and extend its functionality.
#Multiplw Inheritance
class Athlete:
    def __init__(self, sport):
        self.sport = sport

    def train(self):
        return f"I train for {self.sport}."

class StudentAthlete(Student, Athlete):
    def __init__(self, name, age, height, student_number, program, sport):
        Student.__init__(self, name, age, height, student_number, program)
        Athlete.__init__(self, sport)

    def introduction(self):
        return f"{Student.introduction(self)} {Athlete.train(self)}"

#Base Class
class Medium:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} was successfully borrowed.")
        else:
            print(f"{self.title} is currently unavailable.")

    def return_medium(self):
        if not self.available:
            self.available = True
            print(f"{self.title} was successfully returned.")
        else:
            print(f"{self.title} is already in stock.")

    def display(self):
        status = "available" if self.available else "borrowed"
        print(f"'{self.title}' by {self.author} ({self.year}) - Status: {status}")
#Subclasses
class Book(Medium):
    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def display(self):
        super().display()
        print(f"ISBN: {self.isbn}")

class Magazine(Medium):
    def __init__(self, title, author, year, issue):
        super().__init__(title, author, year)
        self.issue = issue

    def display(self):
        super().display()
        print(f"Issue: {self.issue}")

class DVD(Medium):
    def __init__(self, title, director, year, duration):
        super().__init__(title, director, year)
        self.duration = duration

    def display(self):
        super().display()
        print(f"Duration: {self.duration} minutes")


# TODO: Catch and handle errors
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Teilen durch 0 nicht definiert!")
# Assign keyword to a variable:
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(f"Teilen durch 0 nicht definiert! Fehler: {e}")
# Catch multiple errors
try:
    print(10 / "a")
except ZeroDivisionError:
    print("Teilen durch 0 nicht definiert!")
except TypeError:
    print("Keine gültige Zahl!")
# Else block
else:
    print(f"Das Ergebnis ist {ergebnis}")

# The finally block: Sometimes there is code that needs to be executed regardless of whether an exception has occurred or not.
def safe_div(n, d):
    try:
        print(n/d)
    except ZeroDivisionError:
        print("Teilen durch 0 nicht definiert!")
    finally:
        print("Operation abgeschlossen.")

safe_div(10, 0)

#Exception:
class UngueltigeEingabeError(Exception):
    def __init__(self, ex):
        super().__init__(ex)

def eingabe_pruefen(zahl):
    if zahl < 0:
        raise UngueltigeEingabeError("Negative Zahlen sind nicht erlaubt!")

try:
    eingabe_pruefen(-10)
except UngueltigeEingabeError as e:
    print(f"Fehler: {e}")

#raise: This keyword is used to throw an exception in Python.
raise Exception("Something went wrong!")

#error example calculator
class UndefinedOperationError(Exception):
    def __init__(self, operation):
        super().__init__(f"Ungültige Operation: {operation}")

def addiere(a, b):
    return a + b

def subtrahiere(a, b):
    return a - b

def multipliziere(a, b):
    return a * b

def dividiere(a, b):
    if b == 0:
        raise ZeroDivisionError("Division durch null ist nicht möglich!")
    return a / b

def taschenrechner(a, b, operation):
    try:
        if operation == "+":
            ergebnis = addiere(a, b)
        elif operation == "-":
            ergebnis = subtrahiere(a, b)
        elif operation == "*":
            ergebnis = multipliziere(a, b)
        elif operation == "/":
            ergebnis = dividiere(a, b)
        else:
            raise UndefinedOperationError(operation)
            return

        print(f"Das Ergebnis ist: {ergebnis}")
    except TypeError:
        print("Fehler: Ungültige Eingabe, bitte gib eine Zahl ein!")
    except Exception as e:
        print(f"Fehler: {e}")

taschenrechner(5, 4, "+")
taschenrechner(10, 0, "/")
taschenrechner(11, "4", "-")
taschenrechner(7, 4, "#")