def times_ten(start_index: int, end_index: int):
    my_dictionary = {}
    number = start_index
    while number <= end_index:
        my_dictionary[number] = number * 10
        number += 1
    return my_dictionary