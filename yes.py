def sumoftwobin(bin1, bin2):
    wynik = ""
    len1 = len(bin1)
    len2 = len(bin2)
    reszta = 0

    if(len1 > len2):
        r = len1 - len2
        for i in range(r):
            bin2 = "0" + bin2
    elif(len1 < len2):
        r = len2 - len1
        for i in range(r):
            bin1 = "0" + bin1
    len3 = len(bin1)

    for i in range(len3):
        suma = int(bin1[len3-i-1]) + int(bin2[len3-i-1]) + reszta
        if suma > 1:
            reszta = 1
            suma -= 2
        else:
            reszta = 0
        wynik = str(suma) + wynik

    if reszta:
        wynik = str(reszta) + wynik

    print("suma tych dwóch liczb to: ", wynik)


def dec2bin(dec):
    x = []
    bin = 0
    if dec < 0:
        bin = bin % 2
        x.append(bin)
        dec2bin(dec // 2)
        print(x)
        return (bin)


    print(bin)


def bin2dec(bin):
    for bit in bin:
        dec = dec + bit ^ 2
        print(dec)