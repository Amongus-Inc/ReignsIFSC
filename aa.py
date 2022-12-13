tamanho = input('Tamanho da matriz: ')

if int(tamanho) == 2:
    linha1 = input('Primeira linha: ')
    linha2 = input('Segunda linha: ')
    aaa = linha1.split('/')
    bbb = linha2.split('/')
    a = int(aaa[0]) * int(bbb[1])
    b = int(aaa[1]) * int(bbb[0])
    print(a-b)
if int(tamanho) == 3:
    linha1 = input('Primeira linha: ')
    linha2 = input('Segunda linha: ')
    linha3 = input('Terceira linha: ')
    aaa = linha1.split('/')
    bbb = linha2.split('/')
    ccc = linha3.split('/')
    a = int(aaa[0]) * int(bbb[1]) * int(ccc[2])
    b = int(aaa[1]) * int(bbb[2]) * int(ccc[0])
    c = int(aaa[2]) * int(bbb[0]) * int(ccc[1])
    abc = a + b + c
    d = int(aaa[2]) * int(bbb[1]) * int(ccc[0])
    e = int(aaa[0]) * int(bbb[2]) * int(ccc[1])
    f = int(aaa[1]) * int(bbb[0]) * int(ccc[2])
    dfe = d + f + e
    print(abc-dfe)
