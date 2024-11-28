calls = 0


def count_calls():
    global calls
    calls += 1
    return


def string_info(string):
    print(len(string), string.upper(), string.lower())
    count_calls()
    return


def is_contains(string, list_to_search):
    mut_list = [ind.lower() for ind in list_to_search]
    print(string.lower() in mut_list)
    count_calls()
    return


print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))

print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)
