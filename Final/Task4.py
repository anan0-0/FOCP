import re
from sys import argv

# Function to decrypt the ciphertext using a shift value
def decrypt(ciphertext, shift):
    """ This function decrypts the given text using the shift key passed as an argument"""
    
    plaintext = ""
    for c in ciphertext: 
        if c.isalpha():
            # Only shift letters, not symbols
            shift %= 26
            if c.isupper():
                c = chr((ord(c) - shift - 65) % 26 + 65)
            else:
                c = chr((ord(c) - shift - 97) % 26 + 97)
        plaintext += c
    return plaintext

# Function to check if the decrypted text conatins English words
def is_english(text):
    """ This function checks weather the decrpyted message contains english words"""
        
    english_words = ["hello","the", "be", "of", "and", "a", "in", "that", "have", "I", "it", "for", "not", "on", "with", "he", "as", "you", "at","world","this", "if", "about", "but", "his","from","they","we","say","her","she","an","will","my","one","all","would","there","their","what","so","up","out","who","get","which","go"]
    for word in english_words:
        if re.search(r"\b" + word + r"\b", text):
            return True
    return False

try:
    # Try to open the file passed as command line argument
    file_name = argv[1]
    f = open(file_name, "r")
    crypted = f.read()
    f.close()
    result="Cannot decrypt. Most likely not a Caesar Cypher at work here."
    for shift in range(26):
        decrypted_text = decrypt(crypted, shift)
        if is_english(decrypted_text):
            result=decrypted_text
            j=shift
    print(result,shift)

except IndexError:
    # Handle the case where no file name was passed as an argument
    print("Error: Missing command-line argument.")

except FileNotFoundError:
    # Handle the case where the file could not be opened
    print(f"Error: Cannot open {file_name}. Please check if the file exists and try again.")
