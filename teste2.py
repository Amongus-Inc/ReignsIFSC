numero = 120

if (numero - 128) >= 0:
    bit1 = 1
    numero = numero - 128
else 
    bit1 = 0

if (numero - 64) >= 0:
    bit2 = 1
    numero = numero - 64
else 
    bit2 = 0

if (numero - 32) >= 0:
    bit3 = 1
    numero = numero - 32
else 
    bit3 = 0


print (numero)
print (bit1)(bit2)(bit3)