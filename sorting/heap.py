import random


def get_left_child(position):
    return (position + 1) * 2 - 1


def get_right_child(position):
    return (position + 1) * 2


def get_parent(position):
    return (position - 1) // 2


def piramide_sort(L):
    H = []
    N = len(L)

    print("List", L)

    for i in range(N):
        add_to_heap(H, L.pop())

    print("Heap", H)

    for i in range(N):
        L.append(remove_from_heap(H))


def add_to_heap(H: list, elem):
    H.append(elem)
    position = len(H) - 1

    while position > 0:
        parent = get_parent(position)

        if H[parent] > H[position]:
            H[parent], H[position] = H[position], H[parent]
            position = parent
        else:
            break


def remove_from_heap(H: list):
    if len(H) == 1:
        return H.pop()

    position = 0
    min_elem = H[position]
    H[position] = H.pop()

    while position < len(H):
        left_child = get_left_child(position)
        right_child = get_right_child(position)

        if left_child >= len(H):
            break

        if right_child >= len(H):
            min_child = left_child
        else:
            if H[left_child] < H[right_child]:
                min_child = left_child
            else:
                min_child = right_child

        if H[position] > H[min_child]:
            H[position], H[min_child] = H[min_child], H[position]
            position = min_child
        else:
            break

    return min_elem


def check_heap(H: list):
    for position in range(len(H)):
        left_child = get_left_child(position)
        right_child = get_right_child(position)

        if left_child < len(H) and H[left_child] < H[position]:
            return False

        if right_child < len(H) and H[right_child] < H[position]:
            return False

    return True


H = []

for i in range(10):
    random_number = random.randint(0, 10)
    add_to_heap(H, random_number)
    print(H)

assert check_heap(H) == True

for i in range(10):
    correct = min(H)
    answer = remove_from_heap(H)
    print(H)
    assert answer == correct

L = [random.randint(0, 100) for i in range(10)]
Lcp = L[:]

print(L)

piramide_sort(L)
Lcp.sort()

print(L)

assert L == Lcp
