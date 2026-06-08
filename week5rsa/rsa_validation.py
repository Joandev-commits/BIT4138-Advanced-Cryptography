from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def generate_keypair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return private_key, private_key.public_key()

print("=== RSA Testing and Validation ===")

private_key_1, public_key_1 = generate_keypair()
private_key_2, public_key_2 = generate_keypair()

message = "Confidential login token"

ciphertext = public_key_1.encrypt(
    message.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(f"\nOriginal message: {message}")
print(f"\nTest 1: Decrypt with CORRECT private key")
try:
    result = private_key_1.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(f"Result: SUCCESS — {result.decode()}")
except Exception as e:
    print(f"Result: FAILED — {e}")

print(f"\nTest 2: Decrypt with WRONG private key")
try:
    result = private_key_2.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(f"Result: SUCCESS — {result.decode()}")
except Exception as e:
    print(f"Result: FAILED as expected — wrong key cannot decrypt.")

print("\nValidation complete: RSA key pair integrity confirmed.")