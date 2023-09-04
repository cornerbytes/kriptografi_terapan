"""
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

def columnar(data: str, key: str) -> str:
    # Padding data jika data data tidak habis dibagi kunci
    cek_data = len(data) % len(key)
    if cek_data != 0:
        data = ''.join([data, 'X'*(len(key) - cek_data)]) 

    # Mapping data ke dalam list
    result = []
    for index, value in enumerate(key):
        result.append((value, data[index::len(key)]))

    # sorted data 
    result = sorted(result, key=lambda x: x[0])
    result = "".join([i[1] for i in result])
    return result

def columnar_decrypt(data: str, key:str) -> str:
    sorted_key = "".join(sorted(key))
    len_data = len(data)
    len_div = int(len_data / len(key))
    
    # chunk data
    result = [data[i:i + len_div] for i in range(0, len_data, len_div)]
    result = list(zip(list(sorted_key), result))
    res_2 = []
    for i in range(len(key)):
        for index, (huruf, value) in enumerate(result):
            if key[i] == huruf:
                res_2.append(result.pop(index))
                break

    res_2 = "".join([i[1] for i in res_2])
    res_2 = "".join([res_2[i::len_div] for i in range(len_div)])
    return res_2

def unit_test(plaintext, key):
    plaintext = filter_string(plaintext)
    ciphertext = columnar(plaintext, key)
    plain_2 = columnar_decrypt(ciphertext, key)
    print(ciphertext, plain_2, sep='\n')

if __name__ == "__main__":
    plaintext = "WE ARE DISCOVERED. FLEE AT ONCE."
    key = "ZEBRASA"
    unit_test(plaintext, key)
