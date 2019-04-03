def purify(numLst):
    newLst = []
    for num in numLst:
        if num % 2 == 0:
            newLst.append(num)
    return newLst

print(purify([1,2,3]))