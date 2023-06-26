#using function key
def my_function():
    print("Hello")
    print("How are you doing")
my_function()


#Another function
def greeting(fname):
    print("Hello",fname)
greeting("Python")


#Another function
def greeting(fname = "Python"):
    print("Hello", fname)
greeting()
greeting("World")
greeting("Idan")


#Another function
def add_num(i):
    return i + 5
print(add_num(43))



def factorial(i):
    if(n>3):
        result = n + factorial(n-1)
        print(result)
    else :
        result = 0
    return result
factorial(7)
