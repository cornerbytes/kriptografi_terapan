# proof of concept 
def modInverse(A, M):
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

if __name__ == "__main__":
    soal  = [(200, 256), (-4, 11), (12, -1, 5)]
    for x in soal:
        if len(x) == 2:
            print(x[0] % x[1])
        else:
            print(modInverse(x[0], x[2]))
 
