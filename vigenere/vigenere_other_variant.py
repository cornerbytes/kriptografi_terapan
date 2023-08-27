#!/usr/bin/python3
from re import sub as re_sub
import argparse


def filter_string(data: str) -> str:
    """remove all non-alphabet char and return string in uppercase"""
    result = re_sub(r"[^a-zA-Z]", "", data)
    if len(result) == 0:
        print("unable to find alphabet character with your message or key")
        exit()
    return result.upper()


def encrypt(plaintext: str, key: str) -> str:
    key = filter_string(key)
    key_length = len(key)
    plaintext = filter_string(plaintext)
    encrypted_message = []
    key = "".join(key[i % key_length] for i in range(len(plaintext)))

    for i, j in zip(plaintext, key):
        data = (ord(i) + ord(j)) % 26
        data = chr(data + 65)
        encrypted_message.append(data)

    return "".join(encrypted_message)


def decrypt(ciphertext: str, key: str) -> str:
    key = filter_string(key)
    key_length = len(key)
    ciphertext = filter_string(ciphertext)
    decrypted_message = []

    key = "".join(key[i % key_length] for i in range(len(ciphertext)))

    for i, j in zip(ciphertext, key):
        data = (ord(i) - ord(j)) % 26
        data = chr(data + 65)
        decrypted_message.append(data)

    return "".join(decrypted_message)


def combine_non_alpha(origin: str, new_data: str) -> str:
    """this function return string(ciphertext or plaintext) with non alphabet character"""
    counter = 0
    res = []
    for i in origin:
        if i.isupper():
            res.append(new_data[counter])
            counter += 1
        elif i.islower():
            res.append(new_data[counter].lower())
            counter += 1
        else:
            res.append(i)
    return ''.join(res)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VIGENERE CIPHER by PBL RKS-304 (support with non alpha char)")
    parser.add_argument('-m', '--mode', choices=["encrypt", "decrypt"], required=True, help="Mode: encrypt or decrypt")
    parser.add_argument('message', type=str, help="Key for encryption/decryption")
    parser.add_argument('key', type=str, help="text to be encrypted or decrypted",)
    args = parser.parse_args()

    if args.mode == "encrypt":
        res = encrypt(args.message, args.key)
        res = combine_non_alpha(args.message, res)
        print(f"plaintext : {args.message}\nciphertext : {res}\nkey : {args.key}")
    else:
        res = combine_non_alpha(args.message, decrypt(args.message, args.key))
        print(f"ciphertext : {args.message}\nplaintext : {res}\nkey : {args.key}")
