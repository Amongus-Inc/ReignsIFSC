numero = 101

if (numero - 128) >= 0:
    binario = "1"
    numero = numero - 128
else:
    binario = "0"

if (numero - 64) >= 0:
    binario = binario + "1"
    numero = numero - 64
else:
    binario = binario + "0"

if (numero - 32) >= 0:
    binario = binario + "1"
    numero = numero - 32
else:
    binario = binario + "0"

if (numero - 16) >= 0:
    binario = binario + "1"
    numero = numero - 16
else:
    binario = binario + "0"

if (numero - 8) >= 0:
    binario = binario + "1"
    numero = numero - 8
else:
    binario = binario + "0"

if (numero - 4) >= 0:
    binario = binario + "1"
    numero = numero - 4
else:
    binario = binario + "0"

if (numero - 2) >= 0:
    binario = binario + "1"
    numero = numero - 2
else:
    binario = binario + "0"

if (numero - 1) >= 0:
    binario = binario + "1"
    numero = numero - 1
else:
    binario = binario + "0"





print (numero)
print (binario)
