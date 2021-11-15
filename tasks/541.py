
N = int(input())

cities = []
center_x = 0
center_y = 0

for i in range(N):
    x, y = map(int, input().split())

    center_x += x
    center_y += y

    cities.append((x, y))

center_x = round(center_x / N)
center_y = round(center_y / N)

cities = list(map(lambda city: (city[0] - center_x, city[1] - center_y), cities))
cities.sort(key=lambda city:city[0] + city[1])

path = 0

found = False
while not found:
    for i in range(-path, path+1):
        for j in (path - abs(i), -path + abs(i)):
            if (i, j) not in cities:
                print(center_x + i, center_y + j)
                found = True
                break
        if found:
            break

    path += 1

