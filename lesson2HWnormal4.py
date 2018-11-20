import random
num=int(input ('введите количество элементов:'))
s=[]
new_s=[]
i=0
while i < num:
    s.append(random.randint(0,15))
    i += 1
print (s)

print('__a_'+'_'*15)

new_s = set(s)
print(new_s)

print('__b_'+'_'*15)

d = {}
new2_s =[]
new2_s = list()
for i in s :
    d[i] = d.get(i, 0) + 1
#print (d)
for key, value in d.items() :
    if value == 1:
        new2_s.append(key)
print (new2_s)
