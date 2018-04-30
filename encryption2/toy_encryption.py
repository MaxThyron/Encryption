#!/usr/bin/env/ python
def decrypt(s):
    s = list(s)

    for i in range(len(s)):
        if s[i] == "_":
            s[i] = " "

    first_part = s[:len(s)//2]
    second_part = s[len(s)//2:]
    second_part = second_part[::-1]

    result = [" "] * (len(s) + 1)
    for i in range(len(first_part)):
        result[i * 2] = first_part[i]

    for j in range(len(second_part)):
        result[j * 2 + 1] = second_part[j]

    print("".join(result))

def encrypt(s):
    s = list(s)
    first_part = []
    second_part = []

    for i in range(len(s)):
        if s[i] == " ":
            s[i] = "_"

        if i % 2 == 0:
            first_part.append(s[i])
        else:
            second_part.append(s[i])

    second_part = second_part[::-1]

    print("".join(first_part) + "".join(second_part))
            
def main():
    mode = "off"
    while True:
        try:
            print("Current mode:", mode)
            if mode == "off":
                mode = input("Mode(dec - decrypt, enc - encrypt)> ")
            else:
                s = input("String> ")
                if s == "#c":
                    mode = "off"
                elif s == "#q":
                    break
                elif mode == "dec":
                    print(decrypt(s))
                elif mode == "enc":
                    print(encrypt(s))
            print()

            if mode == "#q":
                break
        except:
            break

if __name__ == "__main__":
    main()
