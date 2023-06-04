def uppercase(s):
    for c in s:
        ascii_val = ord(c)
        if ascii_val >= 97 and ascii_val <= 122:
            upper_ascii = ascii_val - 32
            print("{}".format(chr(upper_ascii)), end="")
        else:
            print("{}".format(c), end="")
    print()

def main():
    string = "lol"
    uppercase(string)

if __name__ == "__main__":
    main()
