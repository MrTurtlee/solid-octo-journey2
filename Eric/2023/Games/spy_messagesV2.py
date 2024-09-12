alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 26

given_string = input("Please enter a message to encrypt\n")

# update the variable with all uppercase letters
given_string = given_string.upper()

# get the shift amount from user
shiftAmount = int(input("Please enter an interger to shift from 1-25"))

final_encryption = ""

for current_character in given_string:
    if (current_character in alphabet):
        # just finding the indes of each character in the alphabet
        current_position = alphabet.find(current_character)
        # finding the new character position after shift
        new_position = current_position + shiftAmount
        # find new character with the new character position
        new_character = alphabet[new_position]
    else:
        new_character = current_character  
    # add new character to the final_encryption variable
    final_encryption = final_encryption + new_character
   
print(final_encryption)

