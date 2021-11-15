for path in range(10):
    for i in range(-path, path + 1):
        if path - abs(i) != - path + abs(i):
            print(i, path - abs(i))
            print(i, - path + abs(i))
        else:
            print(i, path - abs(i))