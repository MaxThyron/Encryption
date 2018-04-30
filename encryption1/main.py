import encryption, decryption

def main():
    mode = "off"
    while True:
        try:
            print("Current mode:", mode)
            if mode == "off":
                mode = input("Mode(dec, enc, q)> ")
            else:
                if mode == "dec":
                    print(decryption.decrypt())
                    mode = input("Mode(dec, enc, q)> ")
                elif mode == "enc":
                    print(encryption.encrypt())
                    mode = input("Mode(dec, enc, q)> ")
                else:
                    mode = input("Mode(dec, enc, q)> ")
            print()
        except:
            break

if __name__ == "__main__":
    main()
