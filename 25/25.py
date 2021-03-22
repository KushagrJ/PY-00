# -*- coding: utf-8 -*-
# Python 3.8.6

import random


birthdays = []


i = 0

while i < 23:

    yearOfBirth = random.randrange(1900,2022)

    if yearOfBirth%100 == 0:
        if yearOfBirth%400 == 0:
            leapYear = 1
        else:
            leapYear = 0
    else:
        if yearOfBirth%4 == 0:
            leapYear = 1
        else:
            leapYear = 0

    monthOfBirth = random.randrange(1,13)

    if monthOfBirth == 2 and leapYear == 1:
        dayNumberOfBirthMonth = random.randrange(1,30)
    elif monthOfBirth == 2 and leapYear == 0:
        dayNumberOfBirthMonth = random.randrange(1,29)
    elif monthOfBirth in [1,3,5,7,8,10,12]:
        dayNumberOfBirthMonth = random.randrange(1,32)
    else:
        dayNumberOfBirthMonth = random.randrange(1,31)

    if dayNumberOfBirthMonth < 10 and monthOfBirth < 10:
        birthdays.append("0"+str(monthOfBirth)+"/0"+str(dayNumberOfBirthMonth))
    elif dayNumberOfBirthMonth > 9 and monthOfBirth < 10:
        birthdays.append("0"+str(monthOfBirth)+"/"+str(dayNumberOfBirthMonth))
    elif dayNumberOfBirthMonth < 10 and monthOfBirth > 9:
        birthdays.append(str(monthOfBirth)+"/0"+str(dayNumberOfBirthMonth))
    else:
        birthdays.append(str(monthOfBirth)+"/"+str(dayNumberOfBirthMonth))

    i = i+1


birthdays.sort()

print("The birthdays (MM/DD) of 23 random people are :-")

# To print the list like a, b, c, d instead of like ['a', 'b', 'c', 'd'].
for x in range(len(birthdays)):
    if x+1 == len(birthdays):
        print(birthdays[x])
    else:
        print(birthdays[x], end = ", ")





# /* Trivia
#
#  * The birthday paradox states that in a random group of 23 people, there is
#    about a 50% chance that two people will have the same birthday. For 70
#    people, the chances increase up to 99.9%.
#    [This result is easily obtainable by using basic Probability formulae]
#
#  * import datetime; a = 2001; b = 6; c = 22; d = datetime.date(a,b,c);
#    dayNumberOfYear = d.timetuple().tm_yday; dayNumberOfYear returns 173.
#    [Also, d = datetime.date(2001, 6, 22) works as well]
#    [d = datetime.date(year, month, dayNumber) is a recommended alias]
#  * import datetime; datetime.date.today() returns the current date (for eg.,
#    datetime.date(2021, 3, 22)). [Leading zeroes are not printed]
#    import datetime; datetime.date.today().strftime("%Y") returns the current
#    year (for eg., '2021'). ["%y" should be used for short version (for eg.,
#    '21')]
#    import datetime; datetime.date.today().strftime("%B") returns the current
#    month (for eg., 'March'). ["%b" should be used for short version (for eg.,
#    'Mar')]
#    import datetime; datetime.date.today().strftime("%d") returns the current
#    day number of the month (for eg., '22'). [Leading zeroes are printed]
#    import datetime; datetime.date.today().strftime("%W") returns the current
#    week number of the year (for eg., '12'). [Leading zeroes are printed]
#    import datetime; datetime.date.today().strftime("%w") returns the current
#    day number of the week (for eg., '1'). [Leading zeroes are not printed]
#    [0 is for Sunday]
#    import datetime; datetime.date.today().strftime("%A") returns the current
#    day name of the week (for eg., 'Monday'). ["%a" should be used for short
#    version (for eg., 'Mon')]
#    import datetime; datetime.date.today().strftime("%j") returns the current
#    day number of the year (for eg., '081'). [Leading zeroes are printed]
#    import datetime; datetime.datetime.now() returns the current date and time
#    (for eg., datetime.datetime(2021, 3, 22, 16, 34, 9, 575362)) [Leading
#    zeroes are not printed]
#    [Also, d.strftime("specifier") works as well]
#  */