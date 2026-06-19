sbox = {
    0: 14, 1: 4, 2: 13, 3: 1,
    4: 2,  5: 15, 6: 11, 7: 8,
    8: 3,  9: 10, 10: 6, 11: 12,
    12: 5, 13: 9, 14: 0, 15: 7
}

def permute(bits):
    return bits[2] + bits[3] + bits[0] + bits[1]

def spn_round(value, key):
    mixed = value ^ key
    substituted = sbox[mixed % 16]
    binary = format(substituted, '04b')
    permuted = int(permute(binary), 2)
    return permuted

def spn_encrypt(value, key, rounds=2):
    for _ in range(rounds):
        value = spn_round(value, key)
    return value

def count_bit_differences(a, b):
    xor_result = a ^ b
    return bin(xor_result).count('1')

key = 5
input1 = 9   # 1001
input2 = 8   # 1000  (only 1 bit different)

output1 = spn_encrypt(input1, key, rounds=2)
output2 = spn_encrypt(input2, key, rounds=2)

print("=== Avalanche Effect Demonstration ===")
print(f"Input 1:  {input1} ({format(input1, '04b')})")
print(f"Input 2:  {input2} ({format(input2, '04b')})  <- 1 bit different")
print(f"\nOutput 1: {output1} ({format(output1, '04b')})")
print(f"Output 2: {output2} ({format(output2, '04b')})")

bit_diff = count_bit_differences(output1, output2)
print(f"\nBit differences in output: {bit_diff} out of 4 bits")
print(f"Percentage changed: {(bit_diff/4)*100:.0f}%")
print("\nConclusion: A 1-bit input change caused a significant output change,")
print("demonstrating the avalanche effect produced by the S-Box and permutation.")