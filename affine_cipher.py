ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def decrypt_affine(a_key, b_key, encrypted_text, inverse_mod_a):
    '''
    Decrypt x = NOT A * (Y - B) mod 26

    A = Key 1
    B - Key 2
    Y - Encrypted Cipher Text

    NOT A = Modular Multiplicative Inverse

    '''
    print(ALPHABET[0])
    print('A Key', a_key)
    print('B Key', b_key)
    print("Encrypted Text", encrypted_text)

def inverse_modulo(a_key):
    print('Inverse Mod Function')
    print('A Key', a_key)
    modular_inverse = 0
    inverse_mod_result = 0
    while inverse_mod_result !=1:
        if modular_inverse <= 500:
            print(modular_inverse)
            modular_inverse += 1
            inverse_mod_result = (a_key * modular_inverse) % 26
        else:
            print('There is no modular inverse')
            break
    print('Modular Inverse', modular_inverse)


def main():
    a_key = 7
    b_key = 10
    inverse_mod_a = inverse_modulo(a_key)
    encrypted_text = 'LJMK'.lower()
    #decrypt_affine(a_key, b_key, encrypted_text)

if __name__ == '__main__':
    main()
