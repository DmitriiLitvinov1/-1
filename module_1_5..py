immutable_var = 3.14, 'setc', True,
print(immutable_var)
#
# immutable_var[2] = False             # Это кортеж! = защишенный от изменения список
# print(immutable_var)
mutable_list = [3.14, 'setc', True]
mutable_list[0] = 50
mutable_list[1] = 'seconds'
mutable_list.append('run')
print(mutable_list)
