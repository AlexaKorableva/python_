

def round_num (number,q):
    q = int(q)
    degree = pow(10, int(q))
    mul = number*degree
    res = int(mul)
    osr = mul-res
    if not (abs(osr)<0.5):
        if res>0: res+=1
        else:
            res-=1
    return (res/degree)

a=2.1234537
n=5
nnum = round_num (a,n)
print (nnum)

a=2.1999967
n=5
nnum = round_num (a,n)
print (nnum)

a=2.9999967
n=5
nnum = round_num (a,n)
print (nnum)
