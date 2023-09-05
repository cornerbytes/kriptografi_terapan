"""
BULLET TRAIN CIPHER (VIGENERE DAN DOUBLE TRANPOSITION CIPHER)
objektif :
    - algoritma enkripsi dan dekripsi dengan penggabungan antara
    transposition cipher dan substitution cipher
    - plaintext dan ciphertext dibatasi hanya pada [A-Z]
"""
from re import sub as re_sub


def filter_string(data: str) -> str:
    """
    fungsi ini melakukan filter terhadap seluruh karakter
    non alphabet
    """
    result = re_sub(r"[^a-zA-Z]", "", data)
    if len(result) == 0:
        print("not containin ascii char")
    return result.upper()


def columnar_encrypt(data: str, key: str) -> str:
    # Mapping data ke dalam list
    result = []
    for index, value in enumerate(key):
        result.append((value, data[index :: len(key)]))

    # sorted data
    result = sorted(result, key=lambda x: x[0])
    result = "".join([i[1] for i in result])
    return result


def columnar_decrypt(data: str, key: str) -> str:
    sorted_key = "".join(sorted(key))

    # membuat list panjang column setiap karakter yang ada pada key yang sudah terurut
    mapping_data = [[char, data[index :: len(key)]] for index, char in enumerate(key)]
    mapping_data = sorted(mapping_data, key=lambda x: x[0])
    mapping_data = [len(i[1]) for i in mapping_data]

    # memetakan tiap-tiap kolom dari setiap karakter yang ada pada key (bentuk terurut)
    res_2, ctr = [], 0
    for index, char in enumerate(sorted_key):
        value = data[ctr : ctr + mapping_data[index]]
        res_2.append([char, value])
        ctr += mapping_data[index]

    # reposisi kolom ke posisi semula berdasarkan key yang diberikan
    res_3 = []
    for i in range(len(key)):
        for index, (keyword, value) in enumerate(res_2):
            if key[i] == keyword:
                res_3.append(res_2.pop(index))
                break

    # membaca huruf satu persatu setiap baris berdasarkan kolom yang telah direposisi
    res_4 = []
    max_length = max(len(val) for _, val in res_3)
    for i in range(max_length):
        for char, value in res_3:
            if i < len(value):
                res_4.append(value[i])

    result = "".join(res_4)
    return result


def vigenere_encrypt(plaintext: str, key: str) -> str:
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


def vigenere_decrypt(ciphertext: str, key: str) -> str:
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


def menu():
    print("===========================================================")
    print("NAMA ALGORITMA CIPHER : BULLET TRAIN")
    print("GABUNGAN ANTARA DOUBLE TRANSPOSITION CIPHER DENGAN VIGENERE")

    while True:
        print("1. encrypt\n2. decrypt")
        get_mode = input("Masukkan Mode : ")
        
        if int(get_mode) not in range(1,3):
            print("enter yang bener!")
            exit()
        get_vigenere_key = input("enter vigenere key : ")
        get_first_trans_key = input("enter kunci pertama double tranposition : ")
        get_second_trans_key = input("enter kunci kedua double tranposition : ")
        get_message = filter_string(input("enter pesan : "))
        if get_mode == "1":
            ciphertext_1 = columnar_encrypt(get_message, get_first_trans_key)
            ciphertext_2 = columnar_encrypt(ciphertext_1, get_second_trans_key)
            ciphertext_final = vigenere_encrypt(ciphertext_2, get_vigenere_key)
            print(f"PLAINTEXT : {get_message}\nCIPHERTEXT : {ciphertext_final}")
        elif get_mode == "2":
            plaintext_1 = vigenere_decrypt(get_message, get_vigenere_key)
            plaintext_2 = columnar_decrypt(plaintext_1, get_second_trans_key)
            plaintext_final = columnar_decrypt(plaintext_2, get_first_trans_key)
            print(f"CIPHERTEXT : {get_message}\nPLAINTEXT : {plaintext_final}")
        print("===========================================================")


if __name__ == "__main__":
    menu()
