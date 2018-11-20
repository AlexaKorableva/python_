import math

s = [2,-2,1,25,8,16,121,-64,0]
t = []
for i in s:
    if i >=0 and (math.sqrt(i)  == int(math.sqrt(i))):
        t.append(int(math.sqrt(i)))

print(t)        

                                     
