import datetime

n = int(input())

result = 0
time = datetime.datetime(2023, 7, 3, 0, 0, 0)
while True:
    timeToString = time.strftime("%X")
    if time.hour == n + 1:
        break
    if "3" in timeToString:
        result += 1
    time += datetime.timedelta(seconds=1)

print(result)