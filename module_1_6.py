my_dict = {'Alex': 1985, 'Diana': 2005, 'Sam': 1812}
print('Dict:',
      my_dict)
print('Value:',
      my_dict['Sam'])
print('Not existing value:',
      my_dict.get('Dasha'))
my_dict.update({'Kira': 1587,
                'Igor': 2020})
print('Del:',
      my_dict.pop('Alex'))
print('Modified dict:',
      my_dict)


my_set = {3.14, 2012, 'Sam', "Sam", 3.14}
print('Set:', my_set)
my_set.update({True, 2024})
my_set.discard('Sam')
print('Modified set:', my_set)