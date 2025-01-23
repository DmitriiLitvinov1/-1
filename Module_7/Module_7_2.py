def custom_write(file_name, strings):
    strings_positions = {}

    file = open(file_name, 'w', encoding='utf-8')

    n = 0

    for item in strings:
        n += 1
        strings_positions.update({f'{(n, file.tell())}': f'{item}'})
        file.write(f'{item}\n')
        file.close
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)