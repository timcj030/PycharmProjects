# Enter a year:
year = input('Enter a year:\n ')

# Checkin if the year entered is a leap year
print('Checking if '+year+' is a leap year')

# If the year is not divisible by 4 it is not a leap year
if int(year) % 4 != 0:
    print("{0} is not a leap year as it is not divisible by 4.".format(int(year)))

# If the year is divisible by 100 means it's century year. Century year must be divisible by 400 to become a leap year
elif int(year) % 100 == 0 and int(year) % 400 != 0:
    print("{0} is not a leap year as it is divisible by 100 but not by 400.".format(int(year)))

# If the year is not divisible by 4 or
# if the year is divisible by 100 but not divisible by 400 means it's not a leap year
else:
    print("{0} is a leap year as it is divisible by 4 or 400.".format(int(year)))


