# 백준 19637

n, m = map(int, input().split())
styles = list()
left = -1
for i in range(n):
    name, value = input().split()
    styles.append((name, int(left), int(value)))
    left = value

results = []
for i in range(m):
    power = int(input())
    start = 0
    end = len(styles) - 1
    # result = ""
    while start <= end:
        mid = (start + end) // 2
        left, right = styles[mid][1], styles[mid][2]
        if left < power <= right:
            results.append(styles[mid][0])
            break
        else:
            if power <= left:
                end = mid - 1
            else:
                start = mid + 1

print("\n".join(results))