# Enter a  count
count = int(input('Enter a count value: '))
print('You entered {0}'.format(count))

# Enter a  starting odd value
num = int(input('Enter a number value: '))
print('You entered {0}'.format(num))
if num%2==0:
    print("even numbers are: ")
else:
    print("odd numbers are: ")

for i in range(count):
    print(num)

# Increment by 2  in every iteration
    num += 2

