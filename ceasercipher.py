def caesar_encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# User input
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))

encrypted_text = caesar_encrypt(text, shift)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = caesar_decrypt(encrypted_text, shift)
print(f"Decrypted Text: {decrypted_text}")
