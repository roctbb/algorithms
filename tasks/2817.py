arr = []
for i in range(4):
    n = int(input())
    arr.extend([(int(x), i) for x in input().split(" ")])
arr.sort()
l = 0
ans = 1e9
ans_l = 0
cnts = [0, 0, 0, 0]


def ok():
    # Можно собрать коплект
    return all(x > 0 for x in cnts)


for r in range(len(arr)):
    # Двигаем правый
    r_color, kind = arr[r]
    cnts[kind] += 1

    while ok():
        # Двигаем левый
        l_color, kind = arr[l]
        cnts[kind] -= 1
        new_ans = r_color - l_color
        if new_ans < ans:
            # Обновляем ответ
            ans = new_ans
            ans_l = l
        l += 1
found = [None for i in range(4)]
# Восстанавливаем ответ
while not all(found):
    color, kind = arr[ans_l]
    found[kind] = color
    ans_l += 1
print(" ".join(str(c) for c in found))