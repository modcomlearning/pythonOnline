# Nested if statements
# Loops
# Nested if statements is an if statement inside another one
age = int(input('Your Age: '))
weight = float(input('Your weight: '))
# check if someone can donate blood
if age > 18:
    print('You can donate blood')
    if weight > 50:
        print('You are eligible, you are over 50kgs')
    else:
        print('You are not eligible, you are less 50kgs')

else:
    print('You cannot blood')

# above we check weight in a nested if else statement

