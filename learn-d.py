# Learning Python with Afida <3 Part 4

# Here you'll find :
# 1. Lists

name = ['Ahn Dae Bom', 'Lee Yeo Reum', 'Kook Yeon Soo', 'Choi Woong']

age = [28, 27, 30, 32]

mixed = [11, 'Summer Strike', 'Our Beloved Summer', 45.7]

name.append('Jessica')

# print out the 3th value or index number 2 of mixed list (index always start with 0)
print(mixed[2])

# print out the name list after added Jessica
print(name)

# update the list and print them
name[3] = 'Choi Woongiee'
print(name)

# deleting a value in age
del age[2]
print(age)

print(len(name))
print(min(name))
print(max(name))

print(len(age))
print(min(age))
print(max(age))

print(len(mixed))
print(min(mixed))
print(max(mixed))