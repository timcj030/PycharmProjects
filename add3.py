# Enter number 1
First = input('Enter first number: ')

# Enter number 2
Second = input('Enter second number: ')


# Function to add two numbers and print it
def add_num(num1, num2):
    sum = int(num1) + int(num2)
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
    return sum


# call the function to add 2 numbers
sum1 = add_num(First, Second)

# Add 100
Third = input('Adding 100: ')

# Add 3rd number to sum of 1st and 2nd
sum2 = add_num(sum1, Third)

# Add 1000
Fourth = input('adding 1000: ')

# Add 4th number to first 3
sum3 = add_num(sum2, Fourth)
