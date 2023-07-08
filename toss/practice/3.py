# 백준 11655

s = list(input())

new_s = ""
for c in s:
    if c.isalpha():
        rot13 = ord(c) + 13
        if ord('Z') < rot13 <= ord('Z') + 13 or ord('z') < rot13:
            new_s += chr(ord(c) - 13)
        else:
            new_s += chr(ord(c) + 13)
    else:
        new_s += c
print(str(new_s))