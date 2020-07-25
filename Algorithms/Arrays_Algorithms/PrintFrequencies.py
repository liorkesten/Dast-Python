def print_frequencies(lst):
    table = dict()
    for val in lst:
        if val in table:
            table[val] += 1

        else:
            table[val] = 1

    for key, val in table.items():
        print(f"Key: {key}, Counter: {val}")
