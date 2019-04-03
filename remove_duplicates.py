def remove_duplicates(lst):
    newLst = []
    for elem in lst:
        if elem not in newLst:
            newLst.append(elem)
    return newLst

print(remove_duplicates([1, 1, 1, 2, 2]))