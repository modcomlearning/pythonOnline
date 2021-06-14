
# functions with parameters and arguments
# parameters are put in the function defination, inside the brackets
# below x and y are parameters
# looking at below value of x and y is unknown
def multiply(x, y):
    answer = x * y
    print('Product is ', answer)


# Reference the function
# You provide the arguments to fit the parameters
# when calling the function you provide arguments
multiply(x = 4, y = 10)
multiply(x = 2, y = 10)



# below principle, rate, time are parameters
def simple_interest(principle, rate, time):
    answer = (principle * rate * time)/100
    print('Interest is ', answer)



# function reference\
# Remember to provide arguments
simple_interest(principle=20000, rate=1.2, time=4)
simple_interest(principle=40000, rate=1.2, time=4)
simple_interest(principle=50000, rate=1.2, time=4)

