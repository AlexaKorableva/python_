Bnames= ['Саша','Дима','Андрей','Валя','Денис','Женя','Сергей']
Gnames= ['Женя','Марта','Саша','Лера','Катя']
common_names= []
for i in Bnames:
    for j in Gnames:
        if i == j:
            common_names.append(i)
            break
print(common_names)
        
