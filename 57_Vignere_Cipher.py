s = str(input("String: "))
key = str(input("Key: "))
enc = ''
i = 0

for i in range(len(s)):
    k = ord(s[i]) + ord(key[i%len(key)])%97
    if (k < 123):
        enc += chr(k)
    else:
        enc += chr(k-26)

print(enc)
