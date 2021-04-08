#Catetos e Hipotenusa
from math import sqrt
co = float(input('Comprimento do \033[7:1:31mCATETO OPOSTO:\033[m '))
ca = float(input('Comprimento do \033[7:1:34mCATETO ADJACENTE:\033[m '))
h = sqrt(ca**2+co**2)
print(f'A hipotenusa vai medir \033[7:1:30m{h:.2f}\033[m.')