def BinarySeach(data, key):
    l = 0
    r = len(data)

    while r - l >= 1:
        m = (l + r) // 2
        guess = data[m]
        if guess == key:
            return True
        elif guess < key:
            l = m + 1
        else:
            r = m
            
    return False