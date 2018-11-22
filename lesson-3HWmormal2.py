
def srtlist(s_list):
    lst = []
    while len(s_list) > 0:
        a = s_list[0]
        for i in s_list:
            if i <= a:
                a = i
        s_list.remove(a)
        lst.append(a)
    print (lst)
    
s_list = ([2, 10, -12, 2.5, 20, -11, 4, 4,0])   
srtlist(s_list)
