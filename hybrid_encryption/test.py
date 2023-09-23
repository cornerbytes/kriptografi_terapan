# import class dan function yang dipake
from PBL_RKS_304 import Hybrid, generate_pair_key

if __name__ == '__main__':
    ## initiliasisi class Hybrid
    cipher = Hybrid()

    ## generate pair key for alice and bob
    generate_pair_key('alice')
    generate_pair_key('bob')

    """Skenario 1.
    alice mempunyai file dummy.txt dan ingin mengenkripsi file tersebut.
    alice meminta bob untuk mengirim kan public key miliknya.
    alice lalu mengenkripsi file dummy.txt menggunakan public key milik bob.
    """
    ## encryption
    public_key_bob = "bob_public.pem"
    filename = "dummy.txt"
    cipher.encrypt(public_key_bob, filename)

    """Selanjutnya
    Setelah bob menerima file yang telah dienkripsi dari alice. Bob akan melakukan proses 
    dekripsi menggunakan private key miliknya.
    """
    ## decyrption
    file_dari_alice = "dummy.txt.enc"
    private_key_bob = "bob_private.pem"
    cipher.decrypt(private_key_bob, file_dari_alice)
