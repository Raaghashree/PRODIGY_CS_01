def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += char
    return result

choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

if choice in ['e', 'encrypt', 'd', 'decrypt']:
    text = input("Enter text: ")
    s = int(input("Enter shift value: "))

    if choice in ['e', 'encrypt']:
        print("\nEncrypted Text: ", encrypt(text, s))
    else:
        print("\nDecrypted Text: ", decrypt(text, s))
else:
    print("Invalid choice! Please enter 'E' for encrypt or 'D' for decrypt.")
