# Enter a string value
inputstr = input('Enter a string value:\n\r ')
print("You entered: {0}".format(inputstr))

print("Slice of '{0}' after removing first and last character is '{1}'".format(inputstr, inputstr[1:-1]))
print("Slice of '{0}' after removing first 2 characters is '{1}'".format(inputstr, inputstr[2:]))
print("Slice of '{0}' after removing last 2 characters is '{1}'".format(inputstr, inputstr[:len(inputstr)-2]))
print("mid index is {0}".format(int(len(inputstr) / 2)))
print("First half Slice of '{0}' is '{1}'".format(inputstr, inputstr[:int(len(inputstr) / 2)]))
print("Second half Slice of '{0}' is '{1}'".format(inputstr, inputstr[int(len(inputstr) / 2):]))