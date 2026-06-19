from collections import Counter

def calculate_difference(a, b):
    """XOR-based difference calculation"""
    return a ^ b

def frequency_analysis(data):
    """Analyze frequency distribution of characters"""
    return Counter(data)

def statistical_bias(successes, total):
    """Calculate probability/bias for linear cryptanalysis"""
    return successes / total

def avalanche_test(text1, text2):
    """Demonstrate avalanche effect using Python's built-in hash"""
    h1 = hash(text1)
    h2 = hash(text2)
    return h1, h2

def algebraic_recovery_demo(plaintext, key):
    """Demonstrate algebraic attack on weak XOR cipher"""
    ciphertext = plaintext ^ key
    recovered_key = ciphertext ^ plaintext
    return ciphertext, recovered_key

print("=== Mini Cryptanalysis Toolkit ===\n")

print("--- 1. Difference Calculation ---")
diff = calculate_difference(12, 9)
print(f"Difference between 12 and 9: {diff} ({format(diff, '04b')})\n")

print("--- 2. Frequency Analysis ---")
sample = "ABABABABCCCCDDD"
freq = frequency_analysis(sample)
print(f"Sample data: {sample}")
print(f"Frequency distribution: {freq}\n")

print("--- 3. Statistical Bias (Linear Cryptanalysis) ---")
bias = statistical_bias(75, 100)
print(f"Observed bias: {bias} (expected by chance: 0.5)")
print(f"Deviation from expected: {abs(bias - 0.5)}\n")

print("--- 4. Avalanche Effect Test ---")
h1, h2 = avalanche_test("HELLO", "HELLo")
print(f"hash('HELLO') = {h1}")
print(f"hash('HELLo') = {h2}")
print("A single character change produces a completely different hash.\n")

print("--- 5. Algebraic Attack Demonstration ---")
plaintext = 45
key = 99
ciphertext, recovered = algebraic_recovery_demo(plaintext, key)
print(f"Plaintext: {plaintext}")
print(f"Key (secret): {key}")
print(f"Ciphertext: {ciphertext}")
print(f"Recovered key using algebraic attack (C XOR P): {recovered}")
print(f"Attack successful: {recovered == key}")