

# we creating a BMI calc, with looping
for i in range(0, 5):
    weight = float(input('Your Weight: '))
    height = float(input('Your Height: '))

    bmi = weight/pow(height, 2)
    print('Your BMI is ', bmi)


# above BMI calc is being looped 5 times using a for loop