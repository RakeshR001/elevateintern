# to get the input from the user
num1 = int(input('Enter the number1:'))
num2 = int(input('Enter the number2:'))

#to choose the arithmetic operation
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
operation = input("Enter the operation (+, -, *, /): ")

# the execution of the arithmetic operation
if operation == '+':
    var = num1+num2
    print('the result is',var)
elif operation == '*':
    var = num1*num2
    print('the result is',var)
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        var = num1/num2
        print('the result is',var)
elif operation == '-':
    var = num1-num2
    print('the result is',var)