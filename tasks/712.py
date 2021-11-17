a = int(input())
positions = [-1 for i in range(10 ** 5 + 5)]
cols = list(map(int, input().split()))
step = 0

for col in cols:
    positions[col] = step
    step += 1

for i in range(len(positions)):
    positions[i] = (i, positions[i])

positions.sort(key=lambda x:x[1])

count = 0
for i, v in positions:
    if v != -1:
        count += 1

print(count)

for i, v in positions:
    if v != -1:
        print(i, end=' ')