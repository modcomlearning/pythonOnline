
# Control Statements
#  if , if else, else if
marks = int(input('Enter Your Marks: '))

if marks < 30:
    print('Failed')

elif marks >= 30 and marks < 45:
    print('Good, But below average')

elif marks >= 45 and marks < 60:
    print('Perfect, you have an average')

elif marks >=60 and marks < 75:
    print('Bravo, you have above average')

else:
    print('Excellent, You passed')