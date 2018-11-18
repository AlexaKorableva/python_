import random
num=int(input ('введите количество элементов:'))
s=[]
i=0
while i < num:
    s.append(random.randint(-100,100))
    i += 1
print (s)           
