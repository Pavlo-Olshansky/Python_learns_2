epic_dict = {'Jack': 5, 'Bill': 14, 'Kat': 3, 'Jess': 33, 'Alex': 4}


def sort_by_key(dict_):
    sorted_by_key_dict = sorted(dict_.items(), key=lambda t: t[0])
    print(sorted_by_key_dict)


def sort_by_value(dict_):
    sorted_by_key_dict = sorted(dict_.items(), key=lambda t: t[1])
    print(sorted_by_key_dict)

sort_by_key(epic_dict)
sort_by_value(epic_dict)
