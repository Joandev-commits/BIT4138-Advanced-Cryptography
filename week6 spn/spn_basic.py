
sbox = {
    0: 14, 1: 4, 2: 13, 3: 1,
    4: 2,  5: 15, 6: 11, 7: 8,
    8: 3,  9: 10, 10: 6, 11: 12,
    12: 5, 13: 9, 14: 0, 15: 7
}

def substitute(value):
    """Apply S-Box substitution to a 4-bit value"""
    return sbox[value]

def permute(bits):
    """Simple permutation - rearranges 4-bit positions"""
    return bits[2] + bits[3] + bits[0] + bits[1]

def spn_encrypt_char(value, key):
    """One round of SPN: key mixing -> substitution -> permutation"""
    
    mixed = value ^ key
    print(f"  Key Mixing:   {value} XOR {key} = {mixed}")

    
    substituted = substitute(mixed % 16)
    print(f"  Substitution: S-Box[{mixed % 16}] = {substituted}")

    
    binary = format(substituted, '04b')
    permuted_binary = permute(binary)
    permuted_value = int(permuted_binary, 2)
    print(f"  Permutation:  {binary} -> {permuted_binary} = {permuted_value}")

    return permuted_value

def spn_encrypt(plaintext, key, rounds=2):
    print(f"=== SPN Encryption ===")
    print(f"Plaintext: {plaintext}")
    print(f"Key:       {key}\n")

    result = []
    for char in plaintext:
        value = ord(char) % 16  
        print(f"Processing character '{char}' (value={value}):")
        encrypted_value = value
        for r in range(rounds):
            print(f" Round {r+1}:")
            encrypted_value = spn_encrypt_char(encrypted_value, key)
        result.append(encrypted_value)
        print()

    return result

plaintext = input("Enter plaintext to encrypt: ")
key = 5

ciphertext = spn_encrypt(plaintext, key, rounds=2)
print(f"Final Ciphertext (values): {ciphertext}")