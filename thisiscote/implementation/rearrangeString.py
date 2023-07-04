s = input()

chars = []
num = 0

for c in s:
    if c.isdigit():
        num += int(c)
    else:
        chars.append(c)

chars.sort()

if num != 0:
    chars.append(str(num))
print("".join(chars))

# K1KA5CB7
# AJKDLSI412K4JSJ9D