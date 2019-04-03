def product(intLst):
    result = intLst[0]
    x = 1
    while x < len(intLst):
        result *= intLst[x]
        x += 1
    return result