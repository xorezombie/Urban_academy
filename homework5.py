immutable_var = tuple([1,'cat',4+2,4])
print(immutable_var)
#immutable_var[1] = 'dog' #Изменить не получилось потому-что элементы типа tuple не изменяемые,так как не поддерживает обращение по элементам.
mutable_list= [4, 8, 15, 16, 23, 'lost']
mutable_list[-1]=21*2
print(mutable_list)