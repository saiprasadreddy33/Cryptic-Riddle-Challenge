from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

# Function to encrypt text using Vigenère cipher
def encrypt_vigenere(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()
    
    encrypted_text = ''
    
    j = 0
    for i in range(len(plain_text)):
        char = ord(plain_text[i])
        if char < 65 or char > 90:
            encrypted_text += plain_text[i]
            continue
        
        encrypted_text += chr(((char - 65 + (ord(key[j % len(key)]) - 65)) % 26) + 65)
        j += 1
    
    return encrypted_text

# Function to decrypt text using Vigenère cipher
def decrypt_vigenere(encrypted_text, key):
    encrypted_text = encrypted_text.upper()
    key = key.upper()

    decrypted_text = ''

    j = 0
    for i in range(len(encrypted_text)):
        char = ord(encrypted_text[i])
        if char < 65 or char > 90:
            decrypted_text += encrypted_text[i]
            continue

        decrypted_text += chr(((char - 65 - (ord(key[j % len(key)]) - 65) + 26) % 26) + 65)
        j += 1

    return decrypted_text

# Endpoint to generate encrypted text and key
@app.route('/encrypt', methods=['GET'])
def encrypt():
    try:
        # Generate random text and key
        plain_text = "In shadows deep, secrets keep, Locked away from prying eyes. Through ciphered code, the truth shall seep, Unravel the mystery, and claim your prize."
        key = generate_random_key(5)  # Generate a random key of length 5
        
        # Encrypt the text using the generated key
        encrypted_text = encrypt_vigenere(plain_text, key)
        
        return jsonify({"key": key, "encrypted_text": encrypted_text})
    except Exception as error:
        print('Error generating encrypted text:', error)
        return jsonify({"error": "Internal Server Error"}), 500

# Endpoint to verify decrypted text
@app.route('/verify', methods=['POST'])
def verify():
    try:
        data = request.json
        encrypted_text = data.get('encrypted_text')
        key = data.get('key')
        decrypted_text = data.get('decrypted_text')

        # Decrypt the text using the provided key
        verification_decrypted_text = decrypt_vigenere(encrypted_text, key)

        # Check if the decrypted text matches the provided decrypted text
        if verification_decrypted_text == decrypted_text.upper():
            return jsonify({"message": "Verification successful"})
        else:
            return jsonify({"error": "Verification failed"}), 400
    except Exception as error:
        print('Error verifying decrypted text:', error)
        return jsonify({"error": "Internal Server Error"}), 500

# Function to generate a random key of a specified length
def generate_random_key(length):
    characters = string.ascii_uppercase
    key = ''.join(random.choice(characters) for _ in range(length))
    return key

if __name__ == '__main__':
    app.run(port=3000)
