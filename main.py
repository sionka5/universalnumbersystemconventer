import os
from yes import sumoftwobin, dec2bin, bin2dec

def switch(x):
     os.system('clear')
     if(x == "1"):
        bin = int(input("Wprowadz liczbe w systemie binarnym: "))
        bin2dec(bin)

     elif(x == "2"):
        dec = int(input("Wprowadz liczbe w systemie dziesietnym: "))
        dec2bin(dec)

     elif(x == "3"):
        bin1 = input("Wprowadz pierwsza liczbe: ")
        bin2 = input("Wprowadz druga liczbe: ")
        sumoftwobin(bin1, bin2)


print(
         "Co chcesz zrobić? \n",
         "1. zamiana liczby binarnej w dziesiętną \n",
         "2. zamiana liczby dziesietnej na binarna \n",
         "3. dodawanie liczb binarnych \n"
     )
switch(x = input("wbierz opcje: "))




