"""
Implementasi ecdh
"""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization
from binascii import hexlify
from time import sleep

def create_pair_key():
    return ec.generate_private_key(ec.SECP384R1())


def get_derived_key(shared_key):
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"Info RKS pagi",
    ).derive(shared_key)

    return derived_key

def print_public_key_in_pem(key):
    return key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()

if __name__ == "__main__":
    ## putri pair key
    putri_private_key = create_pair_key()
    putri_public_key = putri_private_key.public_key()

    ## udin pair_key
    udin_private_key = create_pair_key()
    udin_public_key = udin_private_key.public_key()

    """ key exchange begin """
    putri_shared_key = putri_private_key.exchange(ec.ECDH(), udin_public_key)
    putri_derived_key = get_derived_key(putri_shared_key)

    udin_shared_key = udin_private_key.exchange(ec.ECDH(), putri_public_key)
    udin_derived_key = get_derived_key(udin_shared_key)

    print("Generating key for putri...");sleep(1)
    print("Putri public_key : \n", print_public_key_in_pem(putri_private_key))

    print("Generating key for udin...");sleep(1)
    print("Uding public_key : \n", print_public_key_in_pem(udin_private_key))

    print("Putri derivide key : ", hexlify(putri_derived_key).decode())
    print("Udin derivide key : ", hexlify(udin_derived_key).decode())
    
    if putri_derived_key == udin_derived_key:
        print("Key match. Successfully")
    else:
        print("something weird happen.")
