# Enter number 1
First = input('Enter first number: ')

# Enter number 2
Second = input('Enter second number: ')

# Function to subtract two numbers and print it
def Subtract(num1, num2):
    if(int(num1)>int(num2)):
        Diff = int(num1) - int(num2)
    else:
        Diff= int(num2)-int(num1)
    print('The difference of {0} and {1} is {2}'.format(num1, num2, Diff))
    return Diff

#Find out the difference between 2 numbers
Difference= Subtract(First, Second)




