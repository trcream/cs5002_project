ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt_affine(a_key, b_key, text_to_encrypt):
    '''
    Function -- encrypt_affine
        Function to take a string from the user and encrypt it
    
    Parameter:
        a_key -- First key entered by the user
        b_key -- Second key entered by the user
        text_to_encrypt -- String input from the user to be encrypted
    
    Returns:
        Returns the string envcrpted with the cipher
    '''
    text_to_encrypt_index_list = []
    encrypted_index_value = ''
    encrypted_index_values_list = []
    encrypted_index_letter_list = []
    
    # Index values of the text to encrypt
    for character in text_to_encrypt:
        if character in ALPHABET:
            text_to_encrypt_index_list.append(ALPHABET.index(character))
    print('Text to encrypt Index List', text_to_encrypt_index_list)

    # Index values encrypted to new index values
    for index in text_to_encrypt_index_list:
        encrypted_index_value = ((a_key * index) + b_key) % 26
        encrypted_index_values_list.append(encrypted_index_value)
    print(encrypted_index_values_list)

    # Converting the decrypted values to the alphabet 
    for i in encrypted_index_values_list:
        encrypted_index_letter = ALPHABET[i]
        encrypted_index_letter_list.append(ALPHABET[i])
    print(encrypted_index_letter_list)
    return encrypted_index_letter_list


def decrypt_affine(a_key, b_key, encrypted_text, inverse_mod_a):
    '''
    Function -- decrypt_affine
        Function to take a string from the user and encrypt it
    
    Parameter:
        a_key -- First key entered by the user
        b_key -- Second key entered by the user
        encrypted_text -- Text string to be encrypted
        inverse_mod_a -- Inverse modulo which is calculated from another function
    
    Returns:
        Returns the string envcrpted with the cipher

    '''
    decrypted_index_list = []
    decrypted_index_value = ''
    decrypted_letter_values = []
    encrypted_index_list = []

    # Converting the encrypted characters to an index list 
    for character in encrypted_text:
        if character in ALPHABET:
            encrypted_index_list.append(ALPHABET.index(character))
    print('Encrypted Index List', encrypted_index_list)

    # Converting the encrypted index values to decrypted index values
    for index in encrypted_index_list:
        decrypted_index_value = (inverse_mod_a * (index - b_key)) % 26 
        decrypted_index_list.append(decrypted_index_value)

    # Converting the decrypted index values back to characters
    for i in decrypted_index_list:
        decrypted_index_letter = ALPHABET[i]
        decrypted_letter_values.append(decrypted_index_letter)
    print(decrypted_letter_values)
    return decrypted_letter_values
    

def inverse_modulo(a_key):
    '''
    Function -- inverse_modulo
        Function to calcuate the modular multiplicative inverse of the A key
    
    Parameter:
        a_key -- First key entered by the user

    Returns:
        Returns the inverse modulo of the A key
    '''
    modular_inverse = 0
    inverse_mod_result = 0
    while inverse_mod_result !=1:
        if modular_inverse <= 500:
            #print(modular_inverse)
            modular_inverse += 1
            inverse_mod_result = (a_key * modular_inverse) % 26
        else:
            print('There is no modular inverse')
            return False
    print('Modular Inverse', modular_inverse)
    return modular_inverse


def main():
    a_key = int(input('What would you like the A key to be?'))
    # Error handling for the A key to make sure it is invertible
    inverse_mod_a = inverse_modulo(a_key)
    if inverse_mod_a != 0:
        b_key = int(input('What would you like the B key to be?'))
        user_option = int(input('Please choose from:\n1: Encryption\n2: Decryption\n3: quit\n'))

        while user_option !=3: 
            if user_option == 1:
                #Encryption with Affine 
                text_to_encrypt = input('Please enter the text you would like to encrypt ').lower()
                encrypt_affine(a_key, b_key, text_to_encrypt)
                user_option = int(input('Please choose from:\n1: Encryption\n2: Decryption\n3: quit\n'))

            elif user_option == 2:
                # Decryption with Affine
                # Example: LJMKGMGMXFQEXMW
                encrypted_text = input('Please enter the text to be decrypted ').lower()
                decrypt_affine(a_key, b_key, encrypted_text, inverse_mod_a)
                user_option = int(input('Please choose from:\n1: Encryption\n2: Decryption\n3: quit\n'))
    else:
        print('Please select a new A value. There is no modular multiplicative inverse for this integer\n')
    
if __name__ == '__main__':
    main()
