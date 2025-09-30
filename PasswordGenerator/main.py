# Password generator

# Used to generate a password full of random chars.
# Also used to encrypt text and decrypt

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)      #   converts into a list of easy access
keys = chars.copy()
random.shuffle(keys)    #   shuffle the chars into a random order.
password = ""
encrypted_text = ""
decrypted_text = ""

# Generating a random password

def generatePassword():
    try:
        length = int(input("Enter length of password (Min 8 chars, Max 32 chars): "))
        if (length >= 8) or (length <= 32):
            for i in range(length):
                password += random.choice(chars)    # pick chars at random from the chars list and append to the password string.
            print(f"Your password is: {password}")
        else:
            print("Invalid value! Try again idiot.")            
    except ValueError:
        print("Not a valid password length!")
  
    
# Encrypting text

def encryptText():
    global encrypted_text
    plain_text = input("Enter your text to encrypt: ")
    for letter in plain_text:           
        encrypted_text += keys[chars.index(letter)]
    print(f"Encrypted text: {encrypted_text}")
    
    
# Decrypt the text.
        
def decryptText():
    global decrypted_text
    for letter in encrypted_text:
        decrypted_text += chars[keys.index(letter)]
    print(f"Decrypted text: {decrypted_text}")
    
encryptText()
decryptText()