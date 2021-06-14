# We have done variables, datatypes, operators, control statements = if and loops.
# Today we do functions
# What is a function? - a piece of code that runs when referenced/called
# advantages of functions - they split a big code into small pieces called functions
# when we have many small pieces of code, its easier to understand and maintain
# functions make a single piece code used in different places in your program.

def function1():
    print('I am learning Python functions')
    print('I am Loving it')


def function2():
    print('This is another piece of code')



# create a function to find square of number
def square():
    x = 5
    answer = x * x
    print('Square is ', answer)



def simple_interest():
    principle = 40000
    rate = 1.5
    time = 3.5
    answer = (principle * rate * time)/100
    print('Your Interest is ', answer)



# Assignment: create a function to convert degree celsius to degree fahrenheit
def convert():
    celsius = 30
    answer = 9/5 * celsius + 35
    print(answer)



# reference/call a function
# Reference square twice
simple_interest()
simple_interest()
simple_interest()
























