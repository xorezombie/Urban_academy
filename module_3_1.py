calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    len_ = (len(string))
    up_string = string.upper()
    low_string = string.lower()
    return (len_, up_string, low_string)
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return string in list_to_search
info1 = string_info('Hello, world')
info2 = string_info('Urban university')
contains1 = is_contains('cLas', ['UrBan','Clas', 'BuRban'])
contains2 = is_contains('Pycharm', ['PYTHon', 'c++', 'Scratch'])
print(info1)
print(info2)
print(contains1)
print(contains2)
print(calls)

