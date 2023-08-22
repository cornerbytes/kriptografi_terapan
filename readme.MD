# VIGENERE
The Vigenère cipher (French pronunciation: ​[viʒnɛːʁ]) is a method of encrypting alphabetic text where each letter of the plaintext is encoded with a different Caesar cipher, whose increment is determined by the corresponding letter of another text, the key.

### usage:
general / windows

> python3 vigenere.py -m encrypt/decrypt "your message" "your key"

unix based
> ./vigenere.py -m encrypt/decrypt "your messgae" "your key"

### example:

```
python3 vigenere.py -m encrypt "RKSunderCover" "hide"
plaintext : RKSunderCover
ciphertext : YSVYULHVJWYIY
key : hide
```
