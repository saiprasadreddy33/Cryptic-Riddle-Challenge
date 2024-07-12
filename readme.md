# Cryptic Riddle Challenge API 🕵️‍♂️
## _Welcome to the Cryptic Riddle Challenge API, where you can decipher encrypted messages and verify your decrypted solutions. This API uses a Vigenère cipher to encrypt and decrypt messages._


## Table of Contents
- Endpoints
  - /encrypt
  -  /verify
- ✨Encryption Details ✨

## Endpoints

- /encrypt
   - Generates an encrypted message along with a key used for encryption.
[Get Encrypted Text.png](https://github.com/saiprasadreddy33/Cryptic-Riddle-Challenge/blob/main/Get%20Encrypted%20Text.png)
`HTTP Method
GET
curl -X GET http://localhost:3000/encrypt

/verify
Verifies a decrypted text against the original encrypted message.
`
GET

HTTP Method
POST

> Encryption Details
The API uses the Vigenère cipher, which is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. It uses a keyword to shift letters based on their positions in the alphabet.
[Verify Decrypted Text.png](https://github.com/saiprasadreddy33/Cryptic-Riddle-Challenge/blob/main/Verify%20Decrypted%20Text.png)
[verification_fail.png](https://github.com/saiprasadreddy33/Cryptic-Riddle-Challenge/blob/main/verification_fail.png)
## Running the Server
>To run the server locally:
```
Install Flask if not already installed:pip install Flask

```

```
Start the server: python FILENAME.py
```

->The server will start on http://localhost:3000.
