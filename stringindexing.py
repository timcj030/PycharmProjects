# Enter a string value
inputstr = input('Enter a string value: ')


print("First character in '{0}' is '{1}'".format(inputstr, inputstr[0]))
print("Last character in '{0}' is '{1}'".format(inputstr, inputstr[-1]))
print("Length of string '{0}' is {1}".format(inputstr, len(inputstr)))
print("mid index is {0}".format(int(len(inputstr) / 2)))


if(int(len(inputstr) % 2)==0):
    print("Middle characters in '{0}' are '{1}' and '{2}'".format(inputstr, inputstr[int((len(inputstr) - 1) / 2)],
          inputstr[int((len(inputstr) + 1) / 2)]))
else:
    print("Middle character in '{0}' is '{1}'".format(inputstr, inputstr[int((len(inputstr)) / 2)]))



