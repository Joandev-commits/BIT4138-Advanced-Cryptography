def diffie_hellman_exchange(p, g, private_key, other_public):
    public_key = pow(g, private_key, p)
    shared_secret = pow(other_public, private_key, p)
    return public_key, shared_secret

p = 23
g = 5

# Legitimate parties
alice_private = 6
bob_private   = 15

# Attacker (Eve) chooses her own private keys
eve_private_a = 9   # Eve uses this to intercept Alice
eve_private_b = 11  # Eve uses this to intercept Bob

print("=== Man-in-the-Middle Attack Simulation ===\n")
print(f"Public Parameters: p={p}, g={g}\n")

# Normal Diffie-Hellman public keys
alice_public = pow(g, alice_private, p)
bob_public   = pow(g, bob_private, p)

# Eve intercepts and substitutes her own keys
eve_public_a = pow(g, eve_private_a, p)
eve_public_b = pow(g, eve_private_b, p)

print("-- Without Attack --")
print(f"Alice's public key: {alice_public}")
print(f"Bob's public key:   {bob_public}")

print("\n-- Eve Intercepts (substitutes her keys) --")
print(f"Eve sends to Alice (pretending to be Bob): {eve_public_b}")
print(f"Eve sends to Bob (pretending to be Alice): {eve_public_a}")

# Shared secrets with Eve
alice_eve_secret = pow(eve_public_b, alice_private, p)
eve_alice_secret = pow(alice_public, eve_private_b, p)
bob_eve_secret   = pow(eve_public_a, bob_private, p)
eve_bob_secret   = pow(bob_public, eve_private_a, p)

print(f"\n-- Resulting Shared Secrets --")
print(f"Alice thinks she shares secret {alice_eve_secret} with Bob")
print(f"Eve shares secret {eve_alice_secret} with Alice (same)")
print(f"Bob thinks he shares secret {bob_eve_secret} with Alice")
print(f"Eve shares secret {eve_bob_secret} with Bob (same)")

print(f"\nEve can now decrypt all messages between Alice and Bob.")
print(f"Neither Alice nor Bob knows they are communicating through Eve.")
print(f"\nSolution: Use certificates (PKI) to authenticate public keys.")