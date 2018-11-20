s=[1,4,6,9,12,15]
s_1 =[]
for i in s:
    if i % 2 == 0:
       s_1.append(i / 4)
    else:
        s_1.append(i*2)

print (s_1)
