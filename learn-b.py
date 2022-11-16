# Learning Python with Afida <3 Part 2

# Here you'll find :
# 1. If else statement
# 2. If else statement with input

myHeight    = 160
yourHeight  = 173

if myHeight < yourHeight:
    print('Huft, why are you so tall?')
else:
    print('Haha! I am taller :p')

myMoney     = 50000
yourMoney   = input('Btw, lets grab some snacks, how much many do you have?')

if myMoney > int(yourMoney):
    print ('So, you have ' + str(yourMoney) + '. Its okay, the bills is on me.')
elif myMoney == int(yourMoney):
    print ('We have the same amount of money, lets do rock-paper-scissors!')
else:
    print ('Yeay! You have ' + str(yourMoney) +'. Then you should pay!')