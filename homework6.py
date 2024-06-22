my_dict={'Denis' : 2001, 'Vasiliy': 2000, 'Nickolay': 1997}
print(my_dict)
print(my_dict.get('Denis'))
print(my_dict.get('Valeria'))
my_dict.update({'German': 1995,
                'Arkadiy': 1996})
print(my_dict.pop('Vasiliy'))
print(my_dict)

my_set={14,'Denis',22+22,'Denis',33,13,True,False,True,1}
print(my_set)
my_set.update([1223, 'Valentina'])
my_set.discard(13)
print(my_set)