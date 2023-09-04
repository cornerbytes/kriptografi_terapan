# proof of concept nomor 2

def FPB(x, y) -> int:   
    """mengimplementasi algoritma euclidian"""
    while y: # jika y == 0 maka loop akan berhenti dan melanjutkan pesa
        x, y = y, x%y 
    return x


if __name__ == "__main__":
    """
    SOAL : 
        Manakah bilangan berikut yang relatif prima?
        20 dan 3
        7 dan 11
        20 dan 5
    """
    soal  = [(20, 3), (7, 11), (20, 5)]
    for x, y in soal:
        hasil = FPB(x, y)
        if hasil == 1:
            print(f"{x} dan {y} adalah relatif prima")
        else:
            print(f"{x} dan {y} bukan relatif prima")
