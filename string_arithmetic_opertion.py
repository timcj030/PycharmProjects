# Enter a string value
First = input('Enter a string value: ')
print('Your first string value is {0}'.format(First))
# Enter another string value
Second = input('Enter another string value: ')
print('Your second string value is {0}'.format(Second))

# Enter a number (preferably less than 10)
Number = input('Enter a number (preferably less than 10): ')
print('You entered number: {0}'.format(Number))

print ('{0} + {1} is {0}{1}' . format(First,Second))

#print ('{0} * {1} is {0*1}' . format(First,Number))
#print ('{0} * {1} is {0*1}' . format(Second,Number))
print (f"{First}  {Number} is {First*Number}')
