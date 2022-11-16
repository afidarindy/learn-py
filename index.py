# Learning Python with Afida <3

# Here you'll find :
# 1. Data types
# 2. Concatenation
# 3. Escaping from certain characters
# 4. Line break
# 5. Playing with number
# 6. Print strings along with numbers

print("Print a string with quotation marks")
print('Print a string with apostrophe')

print('--------------------------------------')

print('1. Data Types')

yourVar = 'This is string in a defined variable'
print(yourVar)

myID = 11042000
print(myID)

print('--------------------------------------')

print('2. Concatenate two or more strings :')

firstName   = 'Afida'
lastName    = 'Annisa'
print (firstName + ' Rindy ' + lastName)

print('--------------------------------------')

print('3. Escaping characters/symbols :')

print (firstName + " \"Rindy\" " + lastName)
print (firstName + " \'Rindy\' " + lastName)


print('--------------------------------------')

print('4. Adding a break/new line :')

stepOne = '  One : Close your eyes'
stepTwo = '  Two : Count all the blessings you have'
print (stepOne + '\n' + stepTwo)

print('--------------------------------------')

print('5. Playing with number :')

x   = 11
y   = 4
z   = 200
p   = 11.04

print(x + y)
print(x * y)
max(x, y, z)
min(x, y, z, 1)
round(p)
round(89.9)

import math
math.pi

print('--------------------------------------')

print('6. Print strings along with numbers :')

ticketPrice = 45000
year        = 2022
print('The ticket is ' + str(ticketPrice) + ' rupiah in ' + str(year))
print('The ticket is ', ticketPrice, ' rupiah in ', year)