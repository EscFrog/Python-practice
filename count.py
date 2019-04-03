def count(sequence, item):
    found = 0
    for element in sequence:
        if element == item:
            found += 1
    return found

print(count([4, 9, 2, 5], 9))