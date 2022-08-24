# Enter a string value
strval = input('Enter a string value: ')
print('Your first string value is {0}'.format(strval))

#initialize a variable
i=0
print('The length of the entered value is {0}'.format(len(strval)))

#print the characters in the input string
while(i<len(strval)):
    print(strval[i])
    i=i+1

#print in reverse order
j=len(strval) -1
print('------------------')
while(j>=0):
    print(strval[j])
    j=j-1
