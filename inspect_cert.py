import ssl
import socket
import datetime

def inspect_certificate(hostname):
    context = ssl.create_default_context()
    
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
    
    print(f"=== Certificate Inspection: {hostname} ===\n")
    
    # Subject
    subject = dict(x[0] for x in cert['subject'])
    print(f"Subject (Owner):     {subject.get('commonName', 'N/A')}")
    
    # Issuer
    issuer = dict(x[0] for x in cert['issuer'])
    print(f"Issuing CA:          {issuer.get('organizationName', 'N/A')}")
    print(f"Issuer Common Name:  {issuer.get('commonName', 'N/A')}")
    
    # Validity
    not_before = cert['notBefore']
    not_after  = cert['notAfter']
    print(f"\nValid From:          {not_before}")
    print(f"Expiry Date:         {not_after}")
    
    # Protocol version
    print(f"\nTLS Version:         {ssock.version()}")
    print(f"Cipher Suite:        {ssock.cipher()[0]}")
    
    # SANs
    san = cert.get('subjectAltName', [])
    print(f"\nSubject Alt Names:   {[s[1] for s in san[:5]]}")
    
    print(f"\nCertificate is valid and trusted by Python's SSL context.")

inspect_certificate("google.com")