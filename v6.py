import operator
name = input("What is your name? ")
calculation_type = input("What type of calculation are we doing today, " + name + "? E.g +, -, /, * ")
number_of_numbers = int(input("How many numbers? "))
if number_of_numbers < 2 :
    print("You can't proceed with 2 numbers.")
elif number_of_numbers == 2 :
    print("Okay, let's begin!")
    num1 = int(input("What is your first number? "))
    num2 = int(input("What is your second number? "))
    operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}
    op = operations[calculation_type]
    result = op(num1, num2)
    print("Hi " + name + ", your result is " + str(result) + ".")
else:
    print("Insufficient computational power.")


