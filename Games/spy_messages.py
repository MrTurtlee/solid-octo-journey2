
# english alphabet

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

string_to_encrypt = input("Please enter a message to encrypt: \n" )

# turns all the letters in the variable to upper case
string_to_encrypt = string_to_encrypt.upper()

shift_amount = int(input("Please enter a whole number from 1-25 to be your key"))

encrpted_string = ""

for letter in string_to_encrypt:
    print (letter)

