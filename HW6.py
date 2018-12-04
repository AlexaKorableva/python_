
#p=0
#s=int(0)
class triangle:

    def __init__(self,a = 3,b = 4,c = 5,p=12):
        self.a = a
        self.b = b
        self.c = c
        self.p = p
        
    def Perimeter (self,a,b,c):
        
        return self.a+self.b+self.c

    def Square(self,a,b,c,p):
        p=int(0)
        p.Perimeter(a,b,c)
        return (p*(p-a)*(p-b)*(p-c))**0,5
t = triangle()

a = triangle(3)
b = triangle(4)
c = triangle(5)
p = triangle()
#if (a+b)<c or (a+c)<b or (b+c)<a:print('error. such triangle does not exist')
    
t.Perimeter(a,b,c)
print(t.Perimeter(a,b,c))
t.Square(a,b,c,p)
print(t.Square(a,b,c,p))
