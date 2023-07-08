s = input()
alphas = dict()

for c in s:
    c = c.upper()
    if c in alphas:
        alphas[c] += 1
    else:
        alphas[c] = 0

max_value = max(alphas.values())
dupli_check = 0
result = ''
for alpha in alphas:
    if alphas[alpha] == max_value:
        result = alpha
        dupli_check += 1

if dupli_check > 1:
    print("?")
else:
    print(result)