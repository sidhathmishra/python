hexadecimal = b'x00\x01\x01\x81'
number1 = int.from_bytes(hexadecimal,"big")
number2 = int.from_bytes(hexadecimal,"little")
print(number1)
print(number2)
