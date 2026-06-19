def simple_cipher(plaintext_value, key):
    """A deliberately weak cipher for demonstration purposes"""
    return (plaintext_value ^ key) % 256

def analyze_difference(p1, p2, key):
    c1 = simple_cipher(p1, key)
    c2 = simple_cipher(p2, key)

    input_diff = p1 ^ p2
    output_diff = c1 ^ c2

    print(f"Plaintext 1: {p1} ({format(p1, '08b')})")
    print(f"Plaintext 2: {p2} ({format(p2, '08b')})")
    print(f"Input Difference (XOR):  {input_diff} ({format(input_diff, '08b')})")
    print()
    print(f"Ciphertext 1: {c1} ({format(c1, '08b')})")
    print(f"Ciphertext 2: {c2} ({format(c2, '08b')})")
    print(f"Output Difference (XOR): {output_diff} ({format(output_diff, '08b')})")
    print()

    if input_diff == output_diff:
        print("WEAKNESS DETECTED: Input difference equals output difference.")
        print("This is a major vulnerability — the cipher uses simple XOR")
        print("with no substitution or diffusion, so differences pass through unchanged.")
    else:
        print("Input and output differences do not match directly.")

print("=== Differential Cryptanalysis Simulation ===\n")
key = 170  # secret key, unknown to attacker

p1 = int(input("Enter first plaintext value (0-255): "))
p2 = int(input("Enter second plaintext value (0-255): "))

analyze_difference(p1, p2, key)