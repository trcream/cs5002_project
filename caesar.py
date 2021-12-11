def encrypt(user_string, shift_amount):
    '''
    • Python coverts a character to its ascii value with the function ord. Try it out in interactive 
    mode with the statement: ord(‘a’) 
    • Python converts an ascii value to its corresponding letter with the function chr. Try it out 
    in interactive mode with the statement: chr(97) 
    
    '''
    LETTER_LOWER_RANGE = 97
    LETTER_UPPER_RANGE = 122
    encrypted_value = []
    encrypted_message = []
    for character in user_string:
        asci_character = ord(character)
        print('ASCII Value Before', ord(character))
        encrypted_ascii = asci_character + shift_amount
        print(encrypted_ascii)
        if encrypted_ascii >= 97 and encrypted_ascii <= 122:
            encrypted_value = chr(encrypted_ascii)
            print('ASCII Value After', encrypted_value)
            encrypted_message.append(encrypted_value)
        elif encrypted_ascii > 122:
            # encrypted_character = TOTAL_ASCII_RANGE % 26 + 96 + shift_amount
            # encrypted_ascii = (encrypted_ascii - LETTER_UPPER_RANGE) + LETTER_LOWER_RANGE -1
            encrypted_ascii = (encrypted_ascii % 127)
            encrypted_value = chr(encrypted_ascii)
            print('ASCII Value After', encrypted_value)
            encrypted_message.append(encrypted_value)
            print('Over range ASCII', encrypted_ascii)
        else:
            asci_character = chr(asci_character)
            encrypted_message.append(asci_character)
    return encrypted_message


def decrypt(encrypted_string, shift_amount):
    print('decrypt function')
    decrypted_message = []
    unencrypted_ascii = 0
    for character in encrypted_string:
        asci_character = ord(character)
        unencrypted_ascii = asci_character - shift_amount
        print(unencrypted_ascii)
        if unencrypted_ascii >= 97 and unencrypted_ascii <= 122:
            unencrypted_value = chr(unencrypted_ascii)
            decrypted_message.append(unencrypted_value)
        elif unencrypted_ascii < 97:
            unencrypted_ascii = 122 - (97 - unencrypted_ascii) + 1
            unencrypted_value = chr(unencrypted_ascii)
            decrypted_message.append(unencrypted_value)
        else:
            decrypted_message.append(unencrypted_value)
    print(decrypted_message)


def main():

    # convert the alphabet to a letter + 3
    # should all be lower case letters
    # numbers, spaces, and special charactersw do not use a special shift
    user_string = input('Please enter a string to be encrypted ').lower()
    user_shift = int(input('How much would you like to shift by?'))
    encrypted_string = encrypt(user_string, user_shift)
    print(encrypted_string)
    decrypt(encrypted_string,user_shift )

if __name__ == ('__main__'):
    main()