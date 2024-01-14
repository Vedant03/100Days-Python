letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
direction = input("Type encode or decode to encrypt or decrypt respectively:\n")
text=input("type the plain text message:\n").upper()
shift=int(input("Enter the shift number:\n"))
print(letters)
print(text)
def encrypt(plain_text, shift_amount):
    cipher_text=""
    for letter in plain_text:
        position = (letters.index(letter))
        print(letter,position)
        new_position = position + (shift_amount)
        cipher_text = cipher_text + letters[new_position]
    print(f"encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = (letters.index(letter)).upper()
        new_position = position - int(shift_amount)
        plain_text = plain_text + letters[new_position]
    print(f"Decrypted text is {plain_text}")

if(direction == "encode"):
    encrypt(text, shift)
elif(direction =="decode"):
    decrypt(text, shift)
else:
    print("please enter the correct parameters")

