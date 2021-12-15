
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def decrypt_affine(a_key, b_key, encrypted_text, inverse_mod_a):
    '''
    Decrypt x = NOT A * (Y - B) mod 26

    A = Key 1
    B - Key 2
    Y - Encrypted Cipher Text

    NOT A = Modular Multiplicative Inverse

    '''
    decrypted_index_list = []
    decrypted_index_value = ''
    decrypted_letter_values = []
    encrypted_index_list = []
    print(ALPHABET[0])
    print('A Key', a_key)
    print('B Key', b_key)
    print("Encrypted Text", encrypted_text)
    print('Inverse Mod A', inverse_mod_a)

    for character in encrypted_text:
        print(character)
        if character in ALPHABET:
            print(ALPHABET.index(character))
            encrypted_index_list.append(ALPHABET.index(character))
    print('Encrypted Index List', encrypted_index_list)

    for index in encrypted_index_list:
        decrypted_index_value = (inverse_mod_a * (index - b_key)) % 26 
        print('Decrypted Index Value', decrypted_index_value)
        decrypted_index_list.append(decrypted_index_value)
    print(decrypted_index_list)

    for i in decrypted_index_list:
        print(i)
        decrypted_index_letter = ALPHABET[i]
        decrypted_letter_values.append(decrypted_index_letter)
    print(decrypted_letter_values)


def inverse_modulo(a_key):
    # print('A Key', a_key)
    modular_inverse = 0
    inverse_mod_result = 0
    while inverse_mod_result !=1:
        if modular_inverse <= 500:
            #print(modular_inverse)
            modular_inverse += 1
            inverse_mod_result = (a_key * modular_inverse) % 26
        else:
            print('There is no modular inverse')
            break
    print('Modular Inverse', modular_inverse)
    return modular_inverse


def main():
    a_key = 7
    b_key = 10
    inverse_mod_a = int(inverse_modulo(a_key))
    encrypted_text = 'LJMKGMGMXFQEXMW'.lower()
    decrypt_affine(a_key, b_key, encrypted_text, inverse_mod_a)

if __name__ == '__main__':
    main()
