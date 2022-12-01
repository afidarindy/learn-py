# Learning Python with Afida <3 Part 4

# Here you'll find :
# 1. Dictionary
# 2. Nested dictionary

data = {
    'name'      : 'myosotis',
    'aliases'   : 'forget me not/scorpion grasses',
    'type'      : 'flower',
    'size'      : '15',
    'meaning'   : 'a testament to your relationships and promises the other person that you will never forget them in your thoughts'
}

print('The ' + data['name'] + ' ' + data['type'] + ' also known as ' + data['aliases'])

# Add data maxSize
data['maxSize'] = 60
print(data)

# Update name to Myositis
data['name'] = 'Myositis'
print(data)

# Delete maxSize data
del data['maxSize']
print(data)

for key, value in data.items():
    print(key + ' - ' + value + '\n')