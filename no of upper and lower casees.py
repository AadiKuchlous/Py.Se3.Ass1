lower = 0
upper = 0
i = input("Enter a senence with Uppercase and Lowercase letters \n")

for x in i:
    if ord(x) >= 97 and ord(x) <= 122:
        lower = lower + 1
    elif ord(x) >= 65 and ord(x) <= 90:
        upper = upper + 1

print("uppercase", upper)
print("lowercase", lower)
