#Display the options available in calculator
print("Choose an option from the following:\n"
      "(1) Add(+)\n"
      "(2) Subtract(-)\n"
      "(3) Multiply(*)\n"
      "(4) Divide(/)\n"
      "(5) Find Remainder(%)\n"
      "(6) Find Quotient(//) \n"
      "(7) Find Square of a number(**)\n"
      )

#function for addition
def Addition(first, second):
    sum = int(first) + int(second)
    print('The sum of {0} and {1} is {2}'.format(first, second, sum))
    return sum

#function for subtraction
def Subtraction(first, second):
    sub = abs(int(first) - int(second))
    print('The difference of {0} and {1} is {2}'.format(first, second, sub))
    return sub

#function for multiplication
def Multiplication(first, second):
    mul = int(first) * int(second)
    print('The result of {0} * {1} is {2}'.format(first, second, mul))
    return mul

#function for division
def Division(first, second):
    if(int(second)==0):
        print('Not possible to divide by 0. Please enter another number')
        return
    elif(int(first)==0):
        print('Result will be always 0. Please enter a number greater than 0')
        return
    else:
        div = int(first)/int(second)
        print('{0} divided by  {1} is {2}'.format(first, second, div))
    return div

#function for remainder
def Remainder(first, second):
    if(int(second)==0):
        print('Not possible to divide by 0. Please enter another number')
        return
    elif(int(first)==0):
        print('Result will be always 0. Please enter a number greater than 0')
        return
    else:
        rem = int(first)%int(second)
        print('{0} %   {1} is {2}'.format(first, second, rem))
    return rem

#function for quotient
def Quotient(first, second):
    if (int(second) == 0):
        print('Not possible to divide by 0. Please enter another number')
        return
    elif (int(first) == 0):
        print('Result will be always 0. Please enter a number greater than 0')
        return
    else:
        quo = int(first) // int(second)
        print('{0} // by  {1} is {2}'.format(first, second, quo))
    return quo

#function for Square
def Square(first):
    sqr = int(first) * int(first)
    print('The square of {0} is {1}'.format(first, sqr))
    return sqr

#Select an option
Option = input("Enter an option number:")

try:
    while(int(Option)<=7 & int(Option)!=0 ):
        # Enter number 1
        first = input('Enter first number: ')
        if (int(Option) != 7):
            # Enter number 2
            second = input('Enter second number: ')

        if int(Option)== 1:
            # Add
            Addition(first, second)
            break
        elif int(Option) == 2:
            # Subtract
            Subtraction(first, second)
            break
        elif int(Option) == 3:
            # Multiply
            Multiplication(first, second)
            break
        elif int(Option) == 4:
            # Divide
            Division(first, second)
            break
        elif int(Option) == 5:
            # Find Remainder
            Remainder(first, second)
            break

        elif int(Option) == 6:
            # Find Quotient
            Quotient(first, second)
            break
        else:
            # Find Square of a number
            Square(first)
            break
    else:
        print("Please enter a number from 1 to 7")
except:
    #breakpoint()
    print("Please enter a number between 1 and 7")

















