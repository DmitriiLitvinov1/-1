def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(a=5, b=8.3)
# print_params(a = 5, b = 8.3, c = 'V', d = False) количество передаваемых
# аргументов может быть меньше, чем аргументов в функции,(если они определены заранее) но не больше!
values_list = [3, [8, 6], False]
values_dict = {'a': True, 'b': 7, 'c': 'значение'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [3.14, 'Yes']
print_params(*values_list_2, 42)
