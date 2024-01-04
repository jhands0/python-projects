key = int(input("Enter your chosen key: "))
while key >= 26 or key <= 0:
    print("Invalid key")
    key = int(input("Enter your chosen key: "))

text = str(input("Enter your text you would like to encrypt or decrypt: "))

e_or_c = int(input("Select whether you would like to encrypt or decrypt (1 = encrypt)(2 = decrypt): "))
while e_or_c < 1 or e_or_c > 2:
    print("Invalid option")
    e_or_c = int(input("Select whether you would like to encrypt or decrypt (1 = encrypt)(2 = decrypt): "))

if e_or_c == 1:
    plain_text = text
    cipher_text = ""

    for letter in plain_text:
        if letter.isalpha():
            val = ord(letter)
            val = val + key
            if letter.isupper():
                if val > ord('Z'):
                    val -= 26
                elif val < ord('A'):
                    val += 26
            elif letter.islower():
                if val > ord('z'):
                    val -= 26
                elif val < ord('a'):
                    val += 26
            new_letter = chr(val)
            cipher_text += new_letter
        else:
            cipher_text += letter
    print("Your cipher text is",cipher_text)

if e_or_c == 2:
    plain_text = ""
    cipher_text = text

    for letter in cipher_text:
        if letter.isalpha():
            val = ord(letter)
            val = val + key
            if letter.isupper():
                if val > ord('Z'):
                    val -= 26
                elif val < ord('A'):
                    val += 26
            elif letter.islower():
                if val > ord('z'):
                    val -= 26
                elif val < ord('a'):
                    val += 26
            new_letter = chr(val)
            plain_text += new_letter
        else:
            plain_text += letter
    print("Your plain text is",plain_text)