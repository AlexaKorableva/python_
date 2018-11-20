fruit=['apple','pear','watermelon','lemon','orange','banana']

for index, value in enumerate(fruit):
    print('{} {:>1}'.format(str(index + 1) + '.', value))

print('_________________')

fruits=['apple','pear','watermelon','lemon','orange','banana']
for index, value in enumerate(fruits):
    print(f'{index + 1}. {value}')
