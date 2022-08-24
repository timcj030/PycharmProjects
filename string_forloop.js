# Enter a string value
strval = input('Enter a string value: ')
print('Your string value is {0}'.format(strval))

print('The length of the entered value is {0}'.format(len(strval)))

#print the characters in the input string
for i in strval:
    print(i)

#reverse the string
revstr=""
for j in strval:
    revstr = j + revstr
print('The string in revere is {0}'.format(revstr))

# print the characters in revere order
for k in revstr:
    print(k)
