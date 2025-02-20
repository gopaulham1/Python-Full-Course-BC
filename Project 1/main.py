# Lesson 1
# 
# 
#  This is how you can make a comment

# print("I like Pizza");

# x = 5

# # Lesson 2

# first_name = "bro"
# print(f"Hello {first_name}")

# # Strings 
# food = "pizza"
# number = 5

# print(f"You have {number} {food}s")

# #Floats

# gpa = 3.2 
# distance = 10.99
# print(f"Your gpa is {gpa}")

# # Boolean
# is_student = False
# print(f"Are you a student?  {is_student}")

# # if else statements

# if is_student:
#    print("You are a student")
# else:
#    print("You are not a student")

# # Lesson 3 - Typecasting

# name = "Bro code"
# age = 25
# gpa = 3.2
# is_student = True

# gpa = int(gpa)
# print(gpa) #truncated

# age = float(age)
# print(age)

# age = str(age)
# print(age)

# print(type(age)) # <class 'str'>

# name = bool(name)
# print(name) # true

# x = 5
# x = bool(x)
# print(x)


# ##########################################

# #        LESSON 4 - inputs

# ##########################################


# name = input("What is your name? ")
# age = input("How old are you? ")

# age = int(age) + 1


# print(f"Hello {name}!")
# print(f"You are {age} years old!")


# # User creates a rectangle - project

# length = int(input("What is the length of the rectangel? "))
# height = int(input("What is the height of the rectangle? "))

# area = length * height

# print(f"The area of the rectangle is {area}cm²")

##########################################

#        LESSON 5 - Arithmetic

##########################################

# friends = 5

# friends += 5
# friends *= 5 
# friends -= 5
# friends /= 5 
# friends **= 5
# friends %= 5

# print(friends) # 4

# # Built in functions

# x = 3.14
# y = 4
# z = 5

# result = round(x)
# result = abs(y)
# result = pow(y,3)

# print(result)

# import math

# print(math.pi)
# print(math.e)
# print(math.sqrt(144))
# print(math.ceil(3.4444))
# print(math.floor(3.4444))

# # Calculating the circumference of a circle

# radius = int(input("Enter the radius of the circle "))

# cir = radius * math.pi * 2

# print(f"The circumference of the circle is {math.ceil(cir)}cm")


# # Calculating the area of a circle

# radius = pow(int(input("Enter the radius of the circle ")), 2)

# area = radius * math.pi

# print(f"The area of the circle is {math.ceil(area)}cm²")


# print(f"The area of the circle is {round(pow(int(input("Enter the radius of the circle ")), 2) * math.pi)}cm²")


##########################################

#        LESSON 6 - If else elif statements

##########################################

# age = int(input("How old are you? "))

# if age > 100:
#    print("You are too old")
# elif age > 50:
#    print("You are kinda ok....")
# else:
#    print("You are the right age")

# response = input("Are you hungry? (Y/N) ")

# if response == "Y":
#    print("You can eat some food then")  
# else:
#    print("No food for you sir!")


##########################################

##      LESSON 7 - logical operators

##########################################

# temp = 20
# is_raining = False

# if temp>35 or temp<0 or is_raining:
#    print("This outdoor event is cancelled")
# else:
#    print("This outdoor event is still on!")


# if temp>20 and is_raining:
#    print("Hot rain man")
# else:
#    print("It's ite fam")

# if not is_raining:
#    print("It is not raining")

##########################################

##     LESSON 8 - conditional expressions

##########################################

# num = 12434

# print("Positive" if num > 0 else "Negative")
# print("Odd" if num % 2 else "Even")

# a = 6
# b = 12

# max_num = a if a>b else b
# min_num = a if a<b else b
# print(max_num)
# print(min_num)

##########################################

##     LESSON 9 - String methods

##########################################

# name = input("Enter your full name ")

# result = len(name)
# print(result)

# result = name.find("a")
# print(result)

# result = name.rfind("a")
# print(result)

# result = name.capitalize()
# print(result)

# result = name.lower()
# print(result)

# result = name.upper()
# print(result)

# result = name.isdigit()
# print(result)

# result = name.isalpha()
# print(result)

# result = name.replace("a", "o")
# print(result)

# help(str)


##########################################

##     LESSON 10 - String indexing

##########################################

# credit_number = "1234-5678-9012-3456"

# print(credit_number[0])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-3])
# print(credit_number[::2])

# last4digits = credit_number[-4:]
# print(last4digits)


##########################################

##     LESSON 11 - Format specifiers

##########################################

# price1 = 3000.14159
# price2 = -9827.65
# price3 = 1200.34

# print(f"Price 1 is £{price1:.2f}")
# print(f"Price 1 is £{price2:.2f}")
# print(f"Price 1 is £{price3:.2f}")
# print("-------------------------")
# print(f"Price 1 is £{price1:10}")
# print(f"Price 1 is £{price2:10}")
# print(f"Price 1 is £{price3:10}")
# print("-------------------------")
# print(f"Price 1 is £{price1:010}")
# print(f"Price 1 is £{price2:010}")
# print(f"Price 1 is £{price3:010}")
# print("-------------------------")
# print(f"Price 1 is £{price1:<10}")
# print(f"Price 1 is £{price2:<10}")
# print(f"Price 1 is £{price3:<10}")
# print("-------------------------")
# print(f"Price 1 is £{price1:+}")
# print(f"Price 1 is £{price2:+}")
# print(f"Price 1 is £{price3:+}")
# print("-------------------------")
# print(f"Price 1 is £{price1: }")
# print(f"Price 1 is £{price2: }")
# print(f"Price 1 is £{price3: }")
# print("-------------------------")
# print(f"Price 1 is £{price1: ,.2f}")
# print(f"Price 1 is £{price2: ,.2f}")
# print(f"Price 1 is £{price3: ,.2f}")
# print("-------------------------")

##########################################

##     LESSON 12 - While Loop

##########################################

# name = input("What the Huck is your name! ")

# while name == "":
#     print("You did not enter your name!")
#     name = input("What the Huck is your name! ")

# food = input("Enter a food you like! (q to quit): ")

# while not food == "q":
#     print(f"YEAHH  i bet you do like {food} from the looks of it!")
#     food = input("Enter another food you like! (q ro quit): ")

# print("Bye Fatty!")


##########################################

##     LESSON 13 - For loop

##########################################

# for x in range(1,11):
#     print(x)
# print("Happy New Year!!")

# for x in range(1,11,2):
#     print(x)
# print("Happy New Year!!")

# credit_card = "1234-5678-4321-2341"

# for x in credit_card: 
#     print(x)

# for x in range(1,21):
#     if x == 13:
#         continue
#     else:
#         print(x)
        
# for x in range(1,21):
#     if x == 13:
#         break
#     else:
#         print(x)

##########################################

##     LESSON 19 - Countdown timer program

##########################################

# import time

# time.sleep(3)
# print("Time's up!")

# sleep_time = int(input("How long would you like to sleep for? "))

# for sleepy in range(sleep_time,0,-1):
#     print(sleepy)
#     time.sleep(1)

# print("Time is up!")


# sleep_time = int(input("How long would you like to sleep for? "))

# for x in range(sleep_time,0,-1):
#     seconds = x % 60
#     minutes = int((x / 60))
#     hours = int(x / 3600) 
#     print(f"{hours:02}:{minutes:02}:{seconds:02}") # You want to add 2 digits then 0 pad those digits
#     time.sleep(1)

# print("Time is up!")


##########################################

##     LESSON 20 - Nested Loop

##########################################

# for x in range(1,10):
#     print(x)

# for x in range(1,10):
#     print(x,end="")

# for x in range(1,10):
#     print(x,end="-")

# for x in range(1,10):
#     print(x,end=" Idiot ")


# rows = int(input("Enter the number of rows you want "))
# cols = int(input("Enter the number of rows you want ")) 
# symb = input("Enter the symbol you want ")

# for x in range(rows):
#     for y in range(cols):
#         print(symb,end="")
#     print("")

##########################################

##     LESSON 21 - Lists, Sets and Tuples

##########################################

# Collection = single "variable" used to store multiple values

# List = [] ordered and changeable. Duplicates allowed
# Set = {} unordered and immutation, but add, remove ok. no duplicates
# Tuple = () ordered and unchangeable. duplicates ok. faster.

# fruits = ["apple","orange","banana","coconut"]

# print(fruits[0])
# print(fruits[:3])
# print(fruits[::2])
# print(fruits[::-1])

# print(len(fruits))
# print("apple" in fruits)

# fruits[0] = "pineapple"
# fruits.append("pear")
# fruits.remove("pear")
# fruits.insert(0,pear)
# fruits.sort()
# fruits.reverse()
# fruits.clear
# fruits.index("pineapple")
# fruits.count("banana")

## Sets

# fruits = {"apple","orange","banana","coconut"}

# print(fruits)

# fruits.add("pear")
# fruits.pop()
# print(help(fruits))

## Tuple

# fruits = ("apple","orange","banana","coconut","coconut")

# print(len(fruits))
# print("pineapple" in fruits)
# print(fruits.count("coconut"))

##########################################

##     LESSON 22 - 2D Arrays

##########################################

# fruits = ["apple","pears","strawberries"]
# vegetables = ["potatoes","tomatoes"]
# meat = ["fish", "chicken thighs", "chicken legs","bone marrow"]

# groceries = [fruits, vegetables, meat]

# print(groceries[0][0])

# for category in groceries:
#     for item in category:
#         print(item, end=" ----- ")
#     print("")
        
## Can also do 2d tuples, sets, or lists


##########################################

##     LESSON 22 - Dictionay

##########################################

## dictionary = a collection of {key:value} pairs ordered and changeable. No duplicates

# capitals = {"USA":"Washington D.C.",
#             "India":"New Delhi",
#             "China":"Beijing",
#             "Russia":"Moscow"}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("India"))

# if capitals.get("Japan"):
#     print("That capital exists")
# else: {
#     print("That capital doesn't exist")
# }

# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Detroit"})
# capitals.pop("China")

# print(capitals)

# keys = capitals.keys()

# for key in capitals.keys():
#     print(key)

# items = capitals.items()
# print(items)

# for key,value in capitals.items():
#     print(f"{key} => {value}")
    

##########################################

##     LESSON 23 - Random

##########################################

# import random

# low = 1
# high = 100
# cards = ["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]


# options = ("rock", "paper","scissors")
# option = random.choice(options)
# random.shuffle(cards)

# print(random.randint(low, high))
# print(option)
# print(cards)

## Random number guessing game
# import random

# answer = random.randint(1,1000)
# guess_no = 0
# guess = 0

# while True:
#     guess = int(input("Guess the number i am thinking of between 1 and 1000..... "))
#     guess_no+=1
#     if guess == answer:
#        print(f"CORRECT! the answer is {guess}")
#        print(f"Guess attemps = {guess_no}")
       
#        break
#     elif guess>answer:
#         print("NOPE! GO LOWER ")
#     else:
#         print("NOPE! GO HIGHER")
       

## Rock paper scissors game 

# import random
# import time

# options = ("rock","paper","scissors")

# while True: 
#     choice = input("Choose rock(r), paper(p) or scissors(s)!  ")
#     comp = random.choice(options)
#     for x in range(3,0,-1):
#         print(f"{x}!!")
#         time.sleep(1)
#     if choice==comp[0]:
#         print(f"IT'S A DRAW! {comp} is a {comp}!")
#     else:
#         if choice=="r":
#             if comp=="paper":
#                 print("PAPER WRAPS ROCKS -> YOU LOSE")
#             else:
#                 print("ROCK SMASHES SCISSORS -> YOU WIN")
#                 break
#         elif choice=="s":
#             if comp=="paper":
#                 print("SCISSORS CUTS PAPER -> YOU WIN")
#                 break
#             else:
#                 print("ROCK SMASHES SCISSORS -> YOU LOSE")
#         else:
#             if comp=="rock":
#                 print("PAPER WRAPS ROCKS -> YOU WIN")
#                 break
#             else:
#                 print("SCISSORS CUTS PAPER -> YOU LOSE")

##########################################

##     LESSON 24 - Functions

##########################################

## Function - a block of reusable code - place () after the function name to invoke it

# def happy_bday():
#     print("Hello, how can i help you?")
#     print("Hey, how can i help you?")
#     print("Hi, how can i help you?")
    
# happy_bday()

# def happy_birthday(name):
#     print(f"Hello {name}, how can i help you?")
#     print("Hey, how can i help you?")
#     print("Hi, how can i help you?")

# happy_birthday("Hamzah")

       
# ## Return functions

# def add(x,y):
#     return x + y
    
# print(add(34,234))

##########################################

##     LESSON 25 - Default arguments

##########################################

## 4 arguments - positional, default, keyword and arbitrary

# import time

# def net_price(list_price, discount = 0,tax = 0.05):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500))
# print(net_price(500,0.1))

# def count(end,start=0):
#     for x in range(start,end+1):
#         print(x)
#         time.sleep(1)
#     print("DONE!")

# count(10,5)

##########################################

##     LESSON 26 Keyword Arguments

##########################################

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")

# hello("Hello",title="Mr",last="Gopaul",first="Hamzah")

##########################################

##     LESSON 27 Arbitrary Arguments

##########################################

## *args = allows you to pass multiple non-key arguments
## kwargs = allows you to pass multiple keyword-arguments
## *unpacking operator

## *args

# def add(*args):  # Tuple
#     total = 0
#     for arg in args:
#         total+=arg
#     return total

# print(add(1,2,4,123))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Dr.","Spongebob","Hamzah","Squarepants")

# *kwargs

# def print_address(**kwargs):  ## DICTIONARYYY
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
        

# print_address(street="123 Fake St.",city="Detroit",state="MI",zip="54321")

##########################################

##     LESSON 28 Iterable

##########################################

## Iterables = An object/collection that can return its element one at a time, allowing it to be iterated over in a loop

# numbers = [1,2,3,4,5]

# for number in reversed(numbers):
#     print(number)

# for number in numbers:
#     print(number, end="\n")

##########################################

##     LESSON 29 Membership Operators

##########################################

## IN and NOT IN
## Works for strings, lists, tuples, sets, or dictionary

# word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# if letter in word:
#     print(f"{letter} is in the word")
# else:
#     print(f"{letter} was not found")

# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"{letter} is in the word")

# grades = {"Sandy":"A",
#           "Squidward":"B",
#           "Spongebob":"C",
#           "Patrick":"D"}
# student = input("Enter the name of a student ")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")
    
    
##########################################

##     LESSON 30 - list comprehension

##########################################

## List comprehension - A concise way to create lists in python
## Compact and easier to read than traditional loops
## [expression for value in iterable if condition]

# doubles = [x * 2 for x in range(1,11)]
# print(doubles)

# fruits = [fruit.capitalize() for fruit in ["apple","pear","orange"]]
# print(fruits)

# numbers = [1,-2,3,-4,5,-6]

# pos_nums = [num for num in numbers if num >= 0]
# neg_nums = [num for num in numbers if num < 0]

# print(pos_nums)

##########################################

##     LESSON 31 - Match-case statement (switch)

##########################################

# def day_of_week(day):
#     if day == 1:
#         return "it is sunday"
#     elif day == 2:
#         return "it is monday"
# ##.......

# def day_of_week(day):
#     match day:
#         case 1:
#             return "It is sunday"
#         case 2:
#             return "It is monday"
# #.........
#         case _:
#             return "Not a valid day"
        
# print(day_of_week(2))

# def weekend(day):
#     match day:
#         case "Saturday" | "Sunday":
#             return True
#         case _:
#             return False
        
# print(weekend("Tuesday"))

# dotw = input("Day?  ")
# print(dotw == "Saturday" or dotw == "Sunday")


##########################################

##     LESSON 32 - Modules

##########################################

# import math
# print(math.pi)


# import math as m
# print(m.pi)


# from math import pi
# print(pi)


# import example

# result = example.cube(3)

# print(result)


##########################################

##     LESSON 33 - Variable Scope

##########################################

## Variable scope = where a variable is visible and accessible 
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# x = 3

# def func1():
#     x = 1
#     print(x)

# def func2():
#     x = 2
#     print(x)

# func1()
# func2()
# print(x)

##########################################

##     LESSON 34 - __main__

##########################################

## If __name__ == __main__: This script can be imported or run standalone
## Functions and classes in this module can be reused without the main block of code executing

# So basically, let's say we have 2 scripts, script1 and script2. If we import script1 to script2 and then add this
# from script1 import *
# print(__name__)

# Then what is will show in the terminal is:
# script1
# __main__

# so basically, script1 is the __name__ of the script1 file, and __main__ is the file inside your script2 file. 

# So checking if __name__ == __main__ is just to check that the __name__ will call your file and not someone else's file that
# you may have imported

# ---------------------------------------------------------------------------------------------------------------------

# script1

# def favourite_food(food):
#     print(f"Your favourite food is {fodo}")

# def main():
#     print("This is script1")
#     favourite_food("Pizza")
#     print("Goodbye")

# if __name__ == '__main__':
#     main()

# output is..

# This is script1
# Your favourite food is Pizza
# Goodbye

##########################################

##     LESSON 35 - Banking Program

##########################################

# import time

# def show_balance(balance):
#     print(f"Your balance is £{balance:.2f}")
    

# def deposit():
#     amount_input = input("Enter an amount to be deposited:  £")

#     if not amount_input.isdigit():
#         print("Amount entered is incorrect")
#         return 0
#     else:
#         amount = float(amount_input)
#         if amount <= 0:
#             print("That's not a valid amount")
#             return 0
#         else:
#             return amount


# def withdraw(balance):
#     amount_input = input("Enter amount to be withdrawn: £")

#     if not amount_input.isdigit():
#         print("Amount entered is incorrect")
#         return 0
#     else:
#         amount = float(amount_input)
#         if amount > balance:
#             print("Insufficient funds")
#             return 0
#         elif amount <= 0:
#             print("Amount must be greater than 0")
#             return 0
#         else:
#             return amount
    

# def main():
#     balance = 0.0
#     is_running = True

#     while is_running:
#         print("------------------------------------------")
#         print("Banking program")
#         print("------------------------------------------")
#         print("1. Show balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Exit")
#         print("------------------------------------------")
        
#         choice  = input("Enter your choice (1-4): ")

#         match choice:
#             case '1':
#                 show_balance(balance)
#             case '2':
#                 balance += deposit()
#             case '3':
#                 balance -= withdraw(balance)
#             case '4':
#                 is_running = False
#             case _:
#                 print("That is not a valid choice")

#     print("Thank you, have a nice day!")    

# if __name__ == '__main__':
#     main()


##########################################

##     LESSON 36 - Encrypting program

##########################################

# import random
# import string

# chars = " " + string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
# key = chars.copy()

# random.shuffle(key)

# # print(f"chars: {chars}")
# # print(f"key: {key}")

# # Encrypt

# plain_text = input("Enter a message to encrypt: ")
# cipher_text = ""

# for letter in plain_text:
#     index = chars.index(letter)
#     cipher_text += key[index]

# print(f"original message = {plain_text}")
# print(f"encrypted message = {cipher_text}")


# # Decrypt

# cipher_text = input("Enter a message to encrypt: ")
# plain_text = ""

# for letter in cipher_text:
#     index = key.index(letter)
#     plain_text += chars[index]

# print(f"encrypted message = {cipher_text}")
# print(f"original message = {plain_text}")

##########################################

##     LESSON 37 - Hangman game

##########################################

# import random
# from wordslist import words

# # dictionary of key:()
# hangman_art = {0: ("   ","   ","   "), 1: (" o ","   ","   "), 2: (" o "," | ","   "), 3: (" o ","/| ","   "), 
#                4: (" o ","/|\\","   "), 5:(" o ","/|\\","/  "), 6:(" o ","/|\\","/ \\")}

# def display_man(wrong_guesses):
#     print("**************************")
#     for line in hangman_art[wrong_guesses]:
#         print(line)
        

# def display_hint(hint):
#     print(" ".join(hint))
    

# def display_answer(answer):
#     print("**************************")
#     print(" ".join(answer))
#     print("**************************")

# def main():
#     answer = random.choice(words).lower()
#     hint = ["_"] * len(answer)   
#     wrong_guesses = 0
#     guess_letters = set()
#     is_running = True

#     while is_running:
#         display_man(wrong_guesses)
#         display_hint(hint)
#         guess = input("Enter a letter: ").lower()

#         if len(guess) != 1 or not guess.isalpha():
#             print("Invalid input")
#             continue

#         if guess in guess_letters:
#             print(f"{guess} is already guessed")
#             continue

#         guess_letters.add(guess)

#         if guess in answer:
#             for i in range(len(answer)):
#                 if answer[i] == guess:
#                     hint[i] = guess
#         else:
#             wrong_guesses += 1

#         if "_" not in hint:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("YOU WIN!")
#             is_running = False
#         elif wrong_guesses >= len(hangman_art) - 1:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("**************************")
#             print("YOU LOSE!")
#             is_running = False


# if __name__ == "__main__":
#     main()

    
##########################################

##     LESSON 38 - OOP

##########################################

# from car import Car

# ## Object = A "bundle" of related attributes (variables) and methods (functions) Ex. phone, cup ... you need a class to create many objects

# car1 = Car("Mustang", 2024, "red", False)
# print(car1.model)
# print(car1.year)
# print(car1.colour)
# print(car1.for_sale)

# car2 = Car("Corvet", 2022, "blue", True)
# print(car1.model)
# print(car1.year)
# print(car1.colour)
# print(car2.for_sale)

# car1.stop()
# car1.drive()


##########################################

##     LESSON 39 - Class variables      

##########################################

# # class variables = Shared among all instances of a class ... 
# # Defined outside the constructor ... 
# # Allow you to share data among all objects created from that class

# class Student:

#     class_year = 2024
#     num_students = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.num_students += 1
    
# student1 = Student("Smacky", 30)
# student2 = Student("Snacky", 31)
# student3 = Student("lmacky", 32)

# print(student1.name)
# print(student1.age)

# print(student1.class_year)
# # ===
# print(Student.class_year)

# print(Student.num_students)


##########################################

##     LESSON 40 - Inheritance

##########################################

# # Inheritance = Allows a class to inherit attributes and methods from another class ... 
# # Helps with code reusability and extensibility ... 
# # class Child(Parent)


# class Animal:
#    def __init__(self,name):
#       self.name = name
#       self.is_alive = True
    
#    def eat(self):
#         print(f"{self.name} is eating")
        
#    def sleep(self):
#        print(f"{self.name} is sleeping")

# class Dog(Animal):
#     def speak(self):
#         print("WOOF")

# class Cat(Animal):
#     def speak(self):
#         print("MEOW")

# class Mouse(Animal):
#     def speak(self):
#         print("SQUEEK")

# dog = Dog("Scooby")
# cat = Cat("Garfield")
# mouse = Mouse("Mickey")   

# print(dog.name)
# print(dog.is_alive)
# dog.eat()
# dog.speak()


##########################################

##     LESSON 41 - Multiple Inheritance

##########################################

# # Multiple inheritance = inherit from more than one parent class ... 
# # C(A,B) ... 
# # Multilevel inheritance = inherit from a parent which inherits from another parents ... 
# # C(B) <- B(A) <- A

# class Animal:
#     def __init__(self,name):
#        self.name = name
    
#     def sleep(self):
#         print(f"{self.name} is sleeping")
    
#     def eat(self):
#         print(f"{self.name} is eating")

# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting")

# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is fleeing")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Predator, Prey):
#     pass

# rabbit = Rabbit("BUGS")
# hawk = Hawk("Tony")
# fish = Fish("Nemo")

# rabbit.eat()
# hawk.eat()
# hawk.hunt()
        
        
##########################################

##     LESSON 42 - super()

##########################################

# # super() = Function used in a child class to call methods from a parent class (superclass) ... 
# # Allows you to extend the functionality of the inherited methods
    
# class Shape:
#     def __init__(self,colour, is_filled):
#        self.colour = colour
#        self.is_filled = is_filled
    
#     def describe(self):
#         print(f"The shape has colour {self.colour} and {"is filled" if self.is_filled else "is not filled"}")

# class Circle(Shape):
#     def __init__(self, colour, is_filled, radius):
#         self.radius = radius
#         super().__init__(colour, is_filled)
    
#     def describe(self):
#         super().describe()
#         print(f"The area of this circle is {3.14 * self.radius * self.radius}cm2")

# class Square(Shape):
#     def __init__(self,colour, is_filled, width):
#         self.width = width
#         super().__init__(colour, is_filled)
    
#     def comm(self):
#         print(f"This square has an area of {self.width * self.width}cm2")
        
    
# circle = Circle("blue", False, 10)
# circle.describe()
        
# square = Square("RED", True, 120)
# square.describe()
# square.comm()
       
        

##########################################

##     LESSON 43 - Polymorphism

##########################################

# # Polymorphism = Greek word that means to "have many forms or faces" ... 
# # Poly = Many ...
# #  Morphe = Form ... 
# # TWO WAYS TO ACHIEVE POLYMORPHISM ... 
# # 1. Inheritance = an object could be treated of the same type as a parent class ... 
# # 2. "Duck typing" = object must have necessary attributes / methods


# from abc import ABC, abstractmethod # dont know about this

# class Shape(ABC):

#     @abstractmethod ## dont know why this was added
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self,width):
#        self.width = width

#     def area(self):
#         return self.width ** 2
# # The square has two forms -> a square and a shape


# class Triangle(Shape):
#     def __init__(self,width, height):
#        self.width = width
#        self.height = height

#     def area(self):
#         return self.width * self.height * 0.5
# # The triangle has two forms -> a triangle and a shape

    
# class Pizza(Circle):
#     def __init__(self, radius, topping):
#         self.topping = topping
#         super().__init__(radius)

# # The pizza has three forms -> a pizza, a circle and a shape

# shapes = [Circle(12), Square(14), Triangle(12, 12), Pizza(13, "Margherita")]

# for shape in shapes:
#     print(shape.area())


##########################################

##     LESSON 44 - Duck Typing - Polymorphism

##########################################

# # Duck typing = Another way to achieve polymorphism besides Inheritance ... 
# # Object must have the minimum necessary attributes / methods ... 
# # "If it looks like a duck and quacks like a duck, it must be a duck"

# class Animal:
#     alive = True

# class Dog(Animal):
#     def speak(self):
#         print("WOOF")
    
# class Cat(Animal):
#     def speak(self):
#         print("MEOW")

# # If we create an object that isn't an animal but acts like it like this:

# class Car:
#     alive = False
#     def speak(self):
#         print("HONK")

# # Then because it has the min necessary attributes to become an animal, it can pass as one

# animals = [Dog(), Cat(), Car()]

# for animal in animals:
#     animal.speak()
#     print(animal.alive)
    

##########################################

##     LESSON 45 -  Static Methods

##########################################

# # Static methods = A method that belong to a class rather than any object from that class (instance) ... 
# # Usually used for general utility function ... 
# # Instance methods = Best for operations on instances of the class (objects)
# # Static methods = best for utlility functions that do not need access to class data


# class Employee:
#     def __init__(self,name, position):
#        self.name = name
#        self.position = position

#     def getInfo(self):
#         print(f"{self.name} = {self.position}")
    
#     @staticmethod
#     def is_vancancy_available(position):
#         available_positions = ["Chef", "Cashier"]
#         return "Yes it's available" if position in available_positions else "No it's not available"
    
# # The following is a static method ... 
    
# print(Employee.is_vancancy_available("Chef"))

# employer1 = Employee("Hamzah", "Manager")
# employer1.getInfo()

##########################################

##     LESSON 46 - Class methods

##########################################

# # Class methods = Allow operations related to the class itself ... 
# # Take (cls) as the first param, which represents the class itself
    
# # Instance methods = best for operations on instances of the class (objects)
# # Static methods = best of utility functions that do not need access to class data
# # Class methods = best for class-level data or require access to the class itself

# class Student:
#     count = 0
#     total_gpa = 0

#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa

#     def get_info(self):
#         print(f"{self.name} has a gpa of {self.gpa}")

#     @classmethod
#     def get_average_gpa(cls):
#         if cls.count == 0:
#            return 0
#         else:
#            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"
        
#     # This is how to define a class method. Although...when i tried it like this:

#     @classmethod
#     def get_average_gpa(self):
#         if self.count == 0:
#            return 0
#         else:
#            return f"Average gpa: {self.total_gpa / self.count:.2f}"
        
#     # Which is weird....

        


# student1 = Student("Jack", 3.2)
# student1 = Student("Jacky", 3.4)
# student1 = Student("Jackson", 3.6)
# student1 = Student("Jacksony", 1.0)
# student1 = Student("Jacksonton", 0.4)

# student1.get_info()

# print(Student.get_average_gpa())

        
##########################################

##     LESSON 47 - Magic Methods 

##########################################

# # Magic methods = Dundar methods (double underscore) __init__, __str__, __eq__
# # They are automatically called by many of Python's built-in operations.
# # They allow developers to define or customise the behaviour of objects
    
# class Book:
#     def __init__(self,title, author, pages):
#        self.title = title
#        self.author = author
#        self.pages = pages

#     def __str__(self):
#         return f"{self.title} by {self.author}"
    
#     def __eq__(self, other):
#         return self.title == other.title
    
#     def __lt__(self, other):
#         return self.pages < other.pages
    


# book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
# book2 = Book("The Hobbit", "Hamzah", 310)
# book3 = Book("Harry Potter", "J.K. Rowling", 245)
# book4 = Book("Narnia", "C.S. Lewis", 450)

# # Normally if you do this:

# print(book1)

# # You will get this: <__main__.Book object at 0x10d79cb90>
# # So we will customise the __str__ method to allow it to show something readable

# # Now it will show Narnia by C.S. Lewis

# # Check if two books are identical:

# print(book1 == book2)

# # Can customise it to make them be equal if they have the same book title

# # To compare if the pages are equal, you can customise the __lt__ method

# print(book4 < book1)
# print(book2 < book4)

##########################################

##     LESSON 48 - Property Decorator

##########################################

# # @property = Decorator used to define a method as a property (it can be accessed like an attribute)
# # Benefit = add additional logic when read, write or delete attributes
# # Gives you getter, setter, and deleter method

# class Rectangle:
#     def __init__(self,width, height):
#        self._width = width
#        self._height = height
    
#     @property
#     def width(self):
#         print(f"The width is {self._width}cm")
    
#     @property
#     def height(self):
#         print(f"The height is {self._height}cm")
    
#     @width.setter
#     def width(self, new_width):
#         if new_width > 20:
#            self._width = new_width
#         else:
#            print("Access Denied!")

#     @width.deleter
#     def width(self):
#         del self._width
#         print("Width has been deleted")

#     @height.deleter
#     def height(self):
#         del self._width
#         print("Height has been deleted")


# rectangle = Rectangle(10,20)
# rectangle.height
# rectangle.width

# rectangle.width = 2000

# rectangle.width

# del rectangle.width


##########################################

##     LESSON 49 - Decorator

##########################################

# # Decorator = A function that extends the behaviour of another function w/o modifying the base function
# # Pass the base function as an argument to the decorator

# # @add_sprinkles
# # get_ice_cream("vanilla")

# # control + command + space to add an emoji

# def add_sprinkles(func):
#     def wrapper(*args, **kwargs):
#         print("...with spinkles...")
#         func(*args, **kwargs)
#     return wrapper

# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print("...with fudge...")
#         func(*args, **kwargs)
#     return wrapper
    
# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavour):
#     print(f"...created a lovely {flavour} ice cream")

# get_ice_cream("stinky shit")


##########################################

##     LESSON 50 - Exception

##########################################

# # Exception = An event that interrupts the flow of a program 
# # ZeroDivisionError = trying to divide by 0 = x / 1
# # TypeError = trying to merge types = int + bool
# # ValueError = trying to cast something uncastable = (int) "hello"

# # Try ==> Except ==> Finally

# try:
#     number = int(input("Enter a number: "))
#     print(1 / number)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except ValueError:
#     print("Enter only numbers please!")
# except Exception:
#     print("Something went wrong!")
# finally:
#     print("Do some cleanup here!")


##########################################

##     LESSON 51 - Python file detection

##########################################

# import os

# file_path = "Project 1/test.txt"
# file_path2 = "/Users/hamzahgopaul/Desktop/Python Projects/Project 1/test.txt"

# if os.path.exists(file_path2):
#     print(f"The location {file_path2} exists")
#     if os.path.isfile(file_path2):
#         print("That is a file")
#     else:
#         print("That is a directory")
# else:
#     print("That location doesn't exist")

##########################################

##     LESSON 52 - Python writing files (.txt, .json, .csv)

##########################################

# txt_data = "I like pizza \n"

# file_path = "Project 1/output.txt"

# # the letter w writes to the file
# # the letter x writes to the file if it doesn't already exist
# # the letter a appends to the file

# try:
#     with open(file_path, "a") as file:
#         file.write(txt_data)
#         print(f"text file '{file_path}' was created.")
# except FileExistsError:
#     print("File already exists!")


# # Adding a list to the file

# employees = ["Hamzah","Abdullah","Aslam"]

# try:
#     with open(file_path, "w") as file:
#         for employee in employees:
#             file.write(employee + "\n")
#         print(f"text file '{file_path}' was created.")
# except FileExistsError:
#     print("File already exists!")


# ## USING JSON

# import json

# employees = {
#     "name" : "Spongebob",
#     "age" : 30,
#     "job" : "cook"
# }

# file_path = "Project 1/output.json"

# try:
#     with open(file_path, "w") as file:
#         json.dump(employees, file, indent=4)
#         print(f"json file '{file_path}' was created.")
# except FileExistsError:
#     print("File already exists!")


# # USING .CSV FILES

# import csv 

# employees = [["Name", "Age","Job"],
#              ["Spongebob",37, "Cook"],
#              ["Patrick", 30, "Unemployed"],
#              ["Sandy", 23, "Nurse"]]


# file_path = "Project 1/output.csv"

# try:
#     with open(file_path, "w", newline="") as file:
#         writer = csv.writer(file)
#         for guy in employees:
#             writer.writerow(guy)
#         print(f"csv file '{file_path}' was created.")
# except FileExistsError:
#     print("File already exists!")


##########################################

##     LESSON 53 - Reading files (.txt, .jsonn, .csv)

##########################################

# file_path = "Project 1/output.txt"

# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to read that file")


# # READING .JSON FILES

# import json
    
# file_path = "Project 1/output.json"

# try:
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to read that file")


# # READING .CSV FILES

# import csv

    
# file_path = "Project 1/output.csv"

# try:
#     with open(file_path, "r") as file:
#         content = csv.reader(file)
#         for line in content:
#             print(line)
#             print(line[0])
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to read that file")

##########################################

##     LESSON 54 - Datetime 

##########################################

# import datetime

# date = datetime.date(2025,1 ,2)

# print(date)

# today = datetime.date.today()

# print(today)


# time = datetime.time(12,30,0)

# print(time)

# now = datetime.datetime.now()

# print(now)

# now = now.strftime("%H:%M:%S %d-%m-%Y")

# print(now)

# target_datetime = datetime.datetime(2030,1,2,12,30,1)

# current_datetime = datetime.datetime.now()

# if target_datetime < current_datetime:
#     print("Target date has passed")
# else:
#     print("Target date has not passed")


##########################################

##     LESSON 55 - Multithreading   

##########################################


# # Multithreading - Used to perform multiple tasks concurrently (multitasking)
# # Good for I/O bound tasks like reading files or fetching data from APIs
# # threading.Thread(target=myfunction)

# import threading
# import time

# def walk_dog(first, last):
#     time.sleep(8)
#     print("Finished walking the dog")

# def take_trash():
#     time.sleep(2)
#     print("Finished taking out the trash")

# def open_mail():
#     time.sleep(4)
#     print("Finished opening the mail")

# # walk_dog("Scooby","Doo")
# # take_trash()
# # open_mail()

# chore1 = threading.Thread(target=walk_dog, args=("Scooby","Doo"))
# chore1.start()

# chore2 = threading.Thread(target=take_trash)
# chore2.start()

# chore3 = threading.Thread(target=open_mail)
# chore3.start()

# # Now they run concurrently!
# # In order to apply a message to the main thread after the completion of the tasks,
# # We must apply the join method to the tasks 

# chore1.join()
# chore2.join()
# chore3.join()

# print("All tasks have been finished yayy!")

##########################################

##     LESSON 56 - Connect to an API 

##########################################

# import requests

# base_url = "https://pokeapi.co/api/v2/"

# def get_pokemon_info(name):
#     url = f"{base_url}/pokemon/{name}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         pokemon_data = response.json()
#         return pokemon_data
#     else:
#         print(f"Failed to retrieve data {response.status_code}")



# pokemon_name = input("Enter your pokemon => ")
# pokemon_info = get_pokemon_info(pokemon_name)

# if pokemon_info:
#     print(f"Name: {pokemon_info["name"].capitalize()}")
#     print(f"ID: {pokemon_info["id"]}")
#     print(f"Height: {pokemon_info["height"]}ft")
#     print(f"Weight: {pokemon_info["weight"]}kg")




















    




    



        







    


    



       
    









        


    



















   

   
   



































    




















