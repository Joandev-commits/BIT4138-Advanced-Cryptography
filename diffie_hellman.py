def diffie_hellman(p, g, alice_private, bob_private):
    print("=== Diffie-Hellman Key Exchange ===\n")
    
    print(f"Public Parameters:")
    print(f"  Prime (p):     {p}")
    print(f"  Generator (g): {g}")
    
    print(f"\nPrivate Keys (kept secret):")
    print(f"  Alice: {alice_private}")
    print(f"  Bob:   {bob_private}")
    
    # Generate public keys
    alice_public = pow(g, alice_private, p)
    bob_public   = pow(g, bob_private, p)
    
    print(f"\nPublic Keys (exchanged openly):")
    print(f"  Alice's Public Key: A = {g}^{alice_private} mod {p} = {alice_public}")
    print(f"  Bob's Public Key:   B = {g}^{bob_private} mod {p} = {bob_public}")
    
    # Compute shared secrets
    alice_secret = pow(bob_public, alice_private, p)
    bob_secret   = pow(alice_public, bob_private, p)
    
    print(f"\nShared Secret Computation:")
    print(f"  Alice computes: S = {bob_public}^{alice_private} mod {p} = {alice_secret}")
    print(f"  Bob computes:   S = {alice_public}^{bob_private} mod {p} = {bob_secret}")
    
    print(f"\nResult:")
    print(f"  Alice's Secret: {alice_secret}")
    print(f"  Bob's Secret:   {bob_secret}")
    print(f"  Match: {alice_secret == bob_secret}")
    
    if alice_secret == bob_secret:
        print(f"\nKey exchange successful. Shared secret = {alice_secret}")
        print("Both parties can now use this secret to derive a symmetric encryption key.")
    else:
        print("\nKey exchange failed.")

# Use the exact values from the handbook
p = int(input("Enter public prime (p): "))
g = int(input("Enter generator (g): "))
alice_private = int(input("Enter Alice's private key: "))
bob_private   = int(input("Enter Bob's private key: "))

diffie_hellman(p, g, alice_private, bob_private)