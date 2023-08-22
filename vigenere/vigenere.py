#!/usr/bin/python3
from re import sub as re_sub
import argparse


def filter_string(data: str) -> str:
    """remove all non-alphabet char and return string in uppercase"""
    result = re_sub(r"[^a-zA-Z]", "", data)
    return result.upper()


def encrypt(plaintext: str, key: str) -> str:
    key = filter_string(key)
    key_length = len(key)
    plaintext = filter_string(plaintext)

    key = "".join(key[i % key_length] for i in range(len(plaintext)))

    encrypted_message = []
    for i, j in zip(plaintext, key):
        data = (ord(i) + ord(j)) % 26
        data = chr(data + 65)
        encrypted_message.append(data)

    return "".join(encrypted_message)


def decrypt(ciphertext: str, key: str) -> str:
    key = filter_string(key)
    key_length = len(key)
    ciphertext = filter_string(ciphertext)

    key = "".join(key[i % key_length] for i in range(len(ciphertext)))

    decrypted_message = []
    for i, j in zip(ciphertext, key):
        data = (ord(i) - ord(j)) % 26
        data = chr(data + 65)
        decrypted_message.append(data)

    return "".join(decrypted_message)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VIGENERE CIPHER by PBL-RKS304")
    parser.add_argument('-m', '--mode', choices=["encrypt", "decrypt"], required=True, help="Mode: encrypt or decrypt")
    parser.add_argument('message', type=str, help="text to be encrypted or decrypted")
    parser.add_argument('key', type=str, help="key for encryption/decryption")
    args = parser.parse_args()

    if args.mode == "encrypt":
        res = encrypt(args.message, args.key)
        print(f"plaintext : {args.message}\nciphertext : {res}\nkey : {args.key}")
    else:
        res = decrypt(args.message, args.key)
        print(f"ciphertext : {args.message}\nplaintext : {res}\nkey : {args.key}")
