"""Hybrid Encryption by pbl-rks 304.
Modul ini berisi penggabungan antara dua algoritma kriptografi
yaitu AES dan RSA."""

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from base64 import b64encode
from base64 import b64decode
import json


def generate_pair_key(filename: str):
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    with open(f"{filename}_private.pem", "wb") as f:
        f.write(private_key)
    with open(f"{filename}_public.pem", "wb") as f:
        f.write(public_key)


class Hybrid:
    def read_rsa_key(self, filename: str):
        with open(filename, "rb") as f:
            return RSA.import_key(f.read())

    def aes_encrypt(self, data: bytes):
        key = get_random_bytes(16)
        nonce = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        result = {
            "ciphertext": b64encode(ciphertext).decode(),
            "tag": b64encode(tag).decode(),
            "nonce": b64encode(nonce).decode(),
        }
        return result, key

    def aes_decrypt(self, key: bytes, enc_file: dict):
        enc_file = {x: b64decode(y) for x, y in enc_file.items()}
        cipher = AES.new(key, AES.MODE_GCM, nonce=enc_file["nonce"])
        plaintext = cipher.decrypt_and_verify(enc_file["ciphertext"], enc_file["tag"])
        return plaintext

    def rsa_encrypt(self, public_key_filename: str, data: bytes):
        public_key = self.read_rsa_key(public_key_filename)
        cipher = PKCS1_OAEP.new(public_key)
        ciphertext = cipher.encrypt(data)
        return b64encode(ciphertext).decode()

    def rsa_decrypt(self, private_key_filename: str, data: bytes):
        private_key = self.read_rsa_key(private_key_filename)
        cipher = PKCS1_OAEP.new(private_key)
        return cipher.decrypt(data)

    def encrypt(self, public_key_filename: str, file_to_encrypt: str):
        with open(file_to_encrypt, "rb") as f:
            data = f.read()
        data, aes_key = self.aes_encrypt(data)
        data["aes_key"] = self.rsa_encrypt(public_key_filename, aes_key)
        data = json.dumps(data)
        with open(f"{file_to_encrypt}.enc", "w") as f:
            f.write(data)

    def decrypt(self, private_key_filename: str, file_to_decrypt: str):
        with open(file_to_decrypt, "rb") as f:
            data = f.read()
        data = json.loads(data)
        aes_key = b64decode(data["aes_key"])
        aes_key = self.rsa_decrypt(private_key_filename, aes_key)
        plaintext = self.aes_decrypt(aes_key, data)
        with open(file_to_decrypt, "wb") as f:
            f.write(plaintext)
