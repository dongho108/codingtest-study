numbers = list(map(int, list(input())))

result = 0
left = numbers[0]

def isBinary(number):
    return number <= 1


for i in range(1, len(numbers)):
    right = numbers[i]
    if isBinary(left) or isBinary(right):
        result = left + right
    else:
        result = left * right
    left = result

print(result)