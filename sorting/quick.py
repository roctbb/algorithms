import random

def quick_sort(L, start, end):
    pivot = L[(start + end) // 2]

    i = start
    j = end

    while i <= j:
        while L[i] < pivot:
            i += 1

        while L[j] > pivot:
            j -= 1

        if i <= j:
            L[i], L[j] = L[j], L[i]
            i += 1
            j -= 1


    if i < end:
        quick_sort(L, i, end)


    if j > start:
        quick_sort(L, start, j)


if __name__ == "__main__":
    for i in range(10):
        L = [random.randint(0, 100) for _ in range(100)]
        Lcp = L[:]

        quick_sort(L, 0, len(L) - 1)
        Lcp.sort()

        assert L == Lcp
