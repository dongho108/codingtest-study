now = input()

sy = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x = int(now[1]) - 1
y = int(ord(now[0])) - int(ord('a'))

night_steps = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

result = 0
for night_step in night_steps:
    nx = x + night_step[0]
    ny = y + night_step[1]
    if 0 <= nx < 8 and 0 <= ny < 8:
        result += 1
print(result)
