# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.


m = ["lemon", "banana", "pear","pineapple", "melon", 'apple']
n = ['banana', 'watermelon', 'lime', 'mango', 'pear','apple']
k = [i for i in m if i in n]
print(k)
