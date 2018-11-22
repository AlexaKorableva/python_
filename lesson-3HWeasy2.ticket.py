
answer3=('error')
def luck (ticket):
    ticket_list = str(ticket)
    if len(ticket_list)!= 6:
        return answer3
    answer = ('no')
    answer2 = ('yes')
    sum1_3=0
    sum4_6=0
    for i in range(3):
        sum1_3 += int(ticket_list[i])
        sum4_6 += int(ticket_list[-i-1])




    if sum1_3 == sum4_6:
        return answer2
    else: return answer
    
ticket = (123006)
print(luck(ticket))

ticket = (12321)
print(luck(ticket))

ticket = (436751)
print(luck(ticket))
