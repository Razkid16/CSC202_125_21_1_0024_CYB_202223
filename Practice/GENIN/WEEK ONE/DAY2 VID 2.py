#DATATYPES 

#STRING Printing out individual characters
print("Hello"[4])

#INTEGERS/WHOLE NUMBERS (does not use "")
print(123 + 333)

#FLOAT/DECIMAL NUMBERS
print(124.44)

#BOOLEAN (TRUE/FALSE)
True
False 

#DATATYPE CONVERSION 
name = len(input("What is your name?"))
new_name = str(name)
print("Your name has " + new_name + " characters")

#addind the first digit to the second digit
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
two_digit_number = second_digit + first_digit
print(two_digit_number)

#Mathematical operations NB( Double ** is used to raise a number to that power)
6 + 3 
6 - 3
6 * 3
6 / 3
6 ** 2
3 * 2 + 3 / 4 - 2

#Calculating BMI(  )
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
calc = int(weight) / float(height) ** 2
calc_as_int = int(calc) #converting float numbers to integers(whole numbers)
print(calc_as_int)

#Rounding up of numbers and to the number of places it should be rounded up to
print(round(7 / 4, 3))

print(8 // 5) #floor division(it divides it as an integer that is whole number)

#f-String
score = 1
height = 1.56
weight = 76
isWinning = True

print(f"your score is {score}, your height is {height}, your weight is {weight}, you are winning is {isWinning}")

#calculating months weeks and days left if you are to live up until 90
age = input("What is your age?")
age_int = int(age)
years_remaining = 90 - age_int
days_remaining = years_remaining * 365
week_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"you have {days_remaining} days, {months_remaining} months, {years_remaining} years remaining")


#builing a tip calculatator
print("Welcome to the tip calculator!")
Price = float(input("What is the total bill? $"))
tip = int(input("What percentage of tip would you like to give? 10, 12, 15? "))
people = int(input("How many people to split the bill?"))
Price_with_tip = tip / 100 * Price + Price
print(Price_with_tip)
