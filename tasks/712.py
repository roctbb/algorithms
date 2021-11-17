a = int(input())
positions = {}
cols = list(map(int, input().split()))
step = 0

for col in cols:
    positions[col] = step
    step += 1


positions = list(positions.items())
positions.sort(key=lambda x:x[1])

print(len(positions))

for i, v in positions:
    print(i, end=' ')