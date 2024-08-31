
# Encryption
import boto3
# Create a KMS client
kms_client = boto3.client('kms')
# KMS key ID
key_id = 'our-kms-key-id'
# Data to encrypt
plaintext = 'Sensitive data'.encode('utf-8')
# Encrypt the data
response = kms_client.encrypt(
    KeyId=key_id,
    Plaintext=plaintext
)
ciphertext = response['CiphertextBlob']
print(f'Encrypted data: {ciphertext}')

# Decryption
# Decrypt the data
response = kms_client.decrypt(
    CiphertextBlob=ciphertext
)

decrypted_text = response['Plaintext'].decode('utf-8')

print(f'Decrypted data: {decrypted_text}')

