# 백준 2979

a, b, c = map(int, input().split())
b *= 2
c *= 3

cars = [0] * 100

for i in range(3):
    x, y = map(int, input().split())
    for j in range(x, y):
        cars[j] += 1

result = 0
for car in cars:
    if car == 1:
        result += a
    elif car == 2:
        result += b
    elif car == 3:
        result += c

print(result)