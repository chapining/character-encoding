"""
vasya 100

a-z A-Z 0-9
"""
import string

alphabet = string.ascii_lowercase + string.ascii_uppercase
alphabet += "0123456789-_"

print(alphabet)
print(len(alphabet))

def encode(text: str) -> str:
    result = ""
    for i in text:
        index = alphabet.index(i)
        if len(str(index)) < 2:
            result = result + "0" + str(index)
        else:
            result += str(index)
    return result
print(encode(alphabet))