# Prime number checker

alphabet = [ "a","b","c" ,"d" ,"e","f","g" ,"h" ,"i","j","k" ,"l" ,"m","n", "o","p" ,"q" ,"r","s","t" ,"u" ,"v","w", "x", "y" ,"z","a","b","c" ,"d" ,"e","f","g" ,"h" ,"i","j","k" ,"l" ,"m","n", "o",
 "p" ,"q" ,"r","s","t" ,"u" ,"v","w","x","y","z"]
direct = input(f"insert 'encode' to encrypt your message, insert 'decode' to decrypt to decrypt ypur message\n").lower()
tech = input("Type Message\n").lower()
skip =int(input("Type your skip number\n"))

def primeNoCheck(start_letter, sum_num, cipherText) :
     end_letter= " "
     for letter in start_letter :
          position = alphabet.index(letter)


          if cipherText == "decode" :
            sum_num *= -1
            new_pos = position + sum_num
            end_letter += alphabet[new_pos]

          elif cipherText == "encode" :
          # new_pos = position + sh_num
           sh_num *= 1
           new_pos = position + sum_num
           end_txt += alphabet[new_pos]

     print(f" The {cipherText} text is {end_txt}")

primeNoCheck( start_letter= tech, sum_num= skip, cipherText=direct)



#amount of paint needed to paint an area
import math
def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil( area / cover) #round is to round up a number to a whole while math ceil is used to round for upper boundaries
    
    print(f"You will need  {num_of_cans} cans of paint")

test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5
paint_calc(height = test_h , width = test_w, cover = coverage)


#function
name = input("What is your name? ")
response = input('How is the weather.\n' "Enter your response about the weather: ")
def greet(name):
    print("Hello")
    print(f"How are you doing {name}? ")
    print(f"Isn't the weather nice today {name}? {response}")
    return 
greet(name)