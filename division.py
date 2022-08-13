# Enter number 1
First = input('Enter first number: ')

# Enter number 2
Second = input('Enter second number: ')

# Function to subtract two numbers and print it
def Division(num1, num2):
    if(int(num2)==0):
        print('Not possible to divide by 0. Please enter another number')
    elif(int(num1)==0):
        print('Result will be always 0. Please enter a number greater than 0')
    else:
        div = int(num1)/int(num2)
        print(' {0} divided by  {1} is {2}'.format(num1, num2, div))
    return

#Division of 2 numbers
DivisionNum= Division(First, Second)




