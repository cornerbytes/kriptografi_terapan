# proof of concept
def FPB(x, y) -> int:   
    """mengimplementasi algoritma euclidian"""
    while y:
        x, y = y, x%y 
    return x

if __name__ == "__main__":
    """
    Latihan: 
        FPB(6, 12) = ?
        FPB(18, 20) = ?
        FPB(32, 42) = ?
    """
    soal = [(6, 12), (18, 20), (32, 42)]
    for x, y in soal:
        hasil = FPB(x, y)
        print(f"FPB({x}, {y}) = {hasil}")
