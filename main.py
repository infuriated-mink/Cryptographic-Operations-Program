# Program Name: Question 1
# Program Description: Question 1performs cryptographic operations, including verifying file hashes, decrypting AES-
# encrypted data, and verifying plaintext integrity using a provided signature and public key
# Written By: Vanessa Rice
# Written On: September 18, 2023

# Imports
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA256, MD5
import base64


# Step 1: Define AESCrypto class for AES encryption and decryption
class AESCrypto:
    def md5_hash(self, text):
        h = MD5.new()
        h.update(text.encode())
        return h.hexdigest()

    def __init__(self, key):
        # Key Size is 128 bits
        self.key = self.md5_hash(key)


    def decrypt(self, enctext):
        enctext = base64.b64decode(enctext)
        iv = enctext[:16]
        crypto = AES.new(self.key.encode(), AES.MODE_CBC, iv)
        # Inpad the blocks before decrypting
        unpad = lambda s: s[:-ord(s[-1:])]
        return unpad(crypto.decrypt(enctext[16:]))

# Step 2: Read the expected hash values from 'part1.sha256' file
def calculate_hash(filename):
    hasher = SHA256.new()
    with open(filename, 'rb') as f:
        while True:
            data = f.read()
            if not data:
                break
            hasher.update(data)
    return hasher

def verify_hash(filename, expected_hash):
    calculated_hash = calculate_hash(filename).hexdigest()
    return calculated_hash == expected_hash

def read_expected_hashes(filename):
    expected_hashes = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                file_name, hash_value = parts
                expected_hashes[file_name] = hash_value
    return expected_hashes

# Read expected hash values from 'part1.sha256' file
expected_hashes = read_expected_hashes('part1.sha256')

# Verify the hashes using the expected_hashes dictionary
for file_name, expected_hash in expected_hashes.items():
    if verify_hash(file_name, expected_hash):
        print(f"Hash for {file_name} verified successfully.")
    else:
        print(f"Hash verification failed for {file_name}.")

# Step 3: Decrypt the encrypted text file using AES-128.
aes = AESCrypto('sfhaCS2023')
with open('part1.txt.enc', 'rb') as encrypted_file:
    encrypted_text = encrypted_file.read()
    decrypted_text = aes.decrypt(encrypted_text)

print("Decrypted Text:")
print(decrypted_text.decode())

# Step 4: Verify the plaintext using the provided signature and public key.
with open('publickey.pem', 'rb') as key_file:
    public_key = RSA.import_key(key_file.read())

with open('part1.txt.sig', 'rb') as signature_file:
    signature = signature_file.read()

hasher = SHA256.new()
hasher.update(decrypted_text)

try:
    PKCS1_PSS.new(public_key).verify(hasher, signature)
    print("Signature verification successful. The file is authentic.")
except (ValueError, TypeError):
    print("Signature verification failed. The file may have been tampered with.")