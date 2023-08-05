# Usimg if and else statement / elif statement
print("Welcome to the betting center!")
age = int(input("What is your age? "))

if age >= 18:
    print("You are eligible to bet!")
    stake = int(input("How much are staking?"))
    if stake <= 49:
        print("You get a discount of $2")
    elif stake >= 50:
        print("You get a discount of $10")
    else:
        print("You do not get a discount!")
else:
    print("You have to be at least 18 to bet.")

#Using if and else statement to check for odd and even numbers
number = int(input("Which number would you like to check?"))

if number % 2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")


#Calculating BMI(2.0)
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(int(weight) / float(height) ** 2)
calc_as_int = int(bmi) #converting float numbers to integers(whole numbers)
print(calc_as_int)

if calc_as_int < 18.5:
    print(f"Your bmi is {bmi}, You are underwieght!")
elif calc_as_int < 25:
    print(f"Your bmi is {bmi}, You are normal size")
elif calc_as_int < 30:
    print(f"Your bmi is {bmi}, You are overweight!")
elif calc_as_int > 30:
    print(f"Your bmi is {bmi}, You are obese!")
else:
    print("Nothing")

# Leap year checker
year = int(input("What year would you like to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
    else:
        print("Leap year")
else: 
    print("Not a leap year")

#Using multiple if statement (Indentation matters alot.)
height = int(input("How tall are you in cm? "))
age = int(input("How old are you? "))
bill = 0
if height > 120:
    print("You can ride")
    if age < 12:
        bill = 5
        print("Ticket price $5.")
    elif age <= 18:
        bill = 7
        print("Ticket price $7.")
    else:
        bill = 12
        print("Ticket price $12.")

    want_to_add_photo = input("Would you like a photo? Yes or No. ")
    if want_to_add_photo == "Yes":
        bill = bill =+ 3
    print(f"Your total bill is {bill}")
else:
    print("You are not qualified for the ride.")


# Pizza Palace 
print("Welcome to Pizza Palace.")
size = input("What size of pizza would you like? S, M, L ")
pepperoni = input("Do you want pepperoni? Yes or No ")
extra_cheese = input("Would you like extra cheese? Yes or No ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

# adding pepperoni
if pepperoni == "Yes":
    if size == "S":
        bill += 2
    else:
        bill += 3

# adding cheese
if extra_cheese == "Yes":
    bill =+ 1

print(f"Your total bill is ${bill}")


# Using logical and statement.
height = int(input("How tall are you in cm? "))
age = int(input("How old are you? "))
bill = 0
if height > 120:
    print("You can ride")
    if age < 12:
        bill = 5
        print("Ticket price $5.")
    elif age <= 18:
        bill = 7
        print("Ticket price $7.")
    elif age >= 45 and age <= 55:
        print("Everything would be okay. You get to ride for free. ") 
    else:
        bill = 12
        print("Ticket price $12.")

    want_to_add_photo = input("Would you like a photo? Yes or No. ")
    if want_to_add_photo == "Yes":
        bill = bill =+ 3
    print(f"Your total bill is ${bill}")
else:
    print("You are not qualified for the ride.")

# Love calculator
print("Welcome to love calculator")
first_name = input("What is your name? \n")
second_name = input("What is thier name? \n")

# using combined_string to add both names
# using lower_case_string to convert the wrods to lower case letters
combined_string = first_name + second_name
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(true) + int(love)

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like garri and water.")
elif (love_score <= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, You are alright together.")
else:
    print(f"Your love score is {love_score}")


#project(treasure island)
print('''
    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Razkid]
*******************************************************************************
''')


print("Welcome to treasure island.\n Your goal is to find the treasure.")
print("Your goal is to find the treasure.")

choice1 = input('You are at cross road, where would you like to go? Type "Left" or "Right".').lower()
if choice1 == "left":
    choice2 = input('You come to a lake. There is an island in the middle of the lake. Type Wait to "wait" for a boat or Type "Swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. "red", "yellow", "blue". What color would you choose?').lower()
        if choice3 == "red":
            print("You got eaten by a dragon. Game over.")
        elif choice3 == "yellow":
            print("You found the treasure. you win!")
        elif choice3 == "blue":
            print("You entered a room full of angry bees. Game over.")
        else:
            print("Game over.")
    else:
        print("You got attacked by a great white shark. Game over.")
else:
    print("You made the wrong choice. Game over.")
