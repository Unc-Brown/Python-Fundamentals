#import string module gives access to a collection of pre-built string constants and utility tools that would otherwise be tedious to type out manually
#Ex
# string.ascii_letters: This prints out all the letters, including lower and uppercase
# string.ascii_lowercase and string.ascii_uppercase: Prints out lowercase and uppercase letters respectively
# string.digits: Prints out digits from 1-9
# string.punctuation: Prints out every punctuation and special character
# string.whitespace
# string.printable

import random
import string

chars = " "+string.punctuation+string.ascii_letters+string.digits
chars = list(chars)
key = chars.copy()
random.shuffle(key)
print(f"chars: {chars}")
print(f"key  : {key}")

#ENCRYPTION
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""
decrypted_text = ""

for char in plain_text:
    index = chars.index(char)
    cipher_text+=key[index]

print(f"Encrypted text: {cipher_text}")

#DECRYPTION
for char in cipher_text:
    index = key.index(char)
    decrypted_text+=chars[index]

print(f"Decrypted text: {decrypted_text}")