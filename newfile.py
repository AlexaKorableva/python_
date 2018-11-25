import random
m = [random.randint(-50,50) for i in range (10)]
print (m)
n =[i**2 for i in m]
print (n)

m = ["lemon", "banana", "pear","pineapple", "melon", 'apple']
n = ['banana', 'watermelon', 'lime', 'mango', 'pear','apple']
k = [i for i in m if i in n]
print(k)

import random
m = [random.randint(-100,100) for i in range(10)]
print (m)
n =[i for i in m if i%3 == 0 or i>0 or i%4 != 0]
print (n)
