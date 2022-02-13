"""
    Exercício 14

    Leet spek generator.
    Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo.
A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos
jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo.
Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.
"""

from random import randint

a = ['4', '/\\', '@', '/-\\', 'ä', 'ª']
b = ['8', '|3', 'ß']
c = ['[', '¢', '<', '(']
d = ['|))', 'o|', '[)', 'I>', '|>']
e = ['3', '&', '£', 'ë', '€', 'ê']
f = ['|=']
g = ['(_+', 'C-', 'gee']
h = ['#', '/-/', '[-]', '{=}', '<~>', '|-|', ']~[', '}{', ']-[', '}-{']
i = ['1', '!', '|', '&', 'ï']
j = ['j', ';', '_/', '</']
k = ['|<', '|{', ']{', '}<', '|(']
l = ['1_', '|', '|_', '¬', '£']
m = ['//.', '^^', '|v|', '[V]', '|\/|', '/\\/\\', '(u)', '[]V[]', '(V)', '/|\\', 'IVI']
n = ['//', '^/', '|\|', '/\/', '[\]', '<\>', '{\}', '[]\[]', 'n', '/V']
o = ['0', '()', 'ö']
p = ['|^', '|*', '|o', '|^(o)', '|>', '|"', '9', '[]D', '|7']
q = ['q', '9', '(_',') o']
r = ['|2', 'P\\', '|?', '|^', 'lz', '[z', '12', 'Я']
s = ['5', '$', 'z', '§', 'ehs']
t = ['7', '+', '-|-', '1', '"]["', '"|"']
u = ['(_)', '|_|', 'v', 'ü']
v = ['V']
w = ['\/\/', 'vv', '"//', '\^/', '(n)', '\V/', '\//', '\X/', '\|/']
x = ['><', 'Ж', 'ecks', ')(']
y = ['Y', 'j', '`/', '¥']
z = ['2', 'z', '~\_', '~/_', '%']

palavra = input('Informe uma palavra: ')
palavra = list(palavra)

for c in palavra:
    if c == 'a':
        print(a[randint(0, len(a)-1)], end=' ')
    elif c == 'b':
        print(b[randint(0, len(b)-1)], end=' ')
    elif c == 'c':
        print(c[randint(0, len(c)-1)], end=' ')
    elif c == 'd':
        print(d[randint(0, len(d)-1)], end=' ')
    elif c == 'e':
        print(e[randint(0, len(e)-1)], end=' ')
    elif c == 'f':
        print(f[randint(0, len(f)-1)], end=' ')
    elif c == 'g':
        print(g[randint(0, len(g)-1)], end=' ')
    elif c == 'h':
        print(h[randint(0, len(h)-1)], end=' ')
    elif c == 'i':
        print(i[randint(0, len(i)-1)], end=' ')
    elif c == 'j':
        print(j[randint(0, len(j)-1)], end=' ')
    elif c == 'k':
        print(k[randint(0, len(k)-1)], end=' ')
    elif c == 'l':
        print(l[randint(0, len(l)-1)], end=' ')
    elif c == 'm':
        print(m[randint(0, len(m)-1)], end=' ')
    elif c == 'n':
        print(n[randint(0, len(n)-1)], end=' ')
    elif c == 'o':
        print(o[randint(0, len(o)-1)], end=' ')
    elif c == 'p':
        print(p[randint(0, len(p)-1)], end=' ')
    elif c == 'q':
        print(q[randint(0, len(q)-1)], end=' ')
    elif c == 'r':
        print(r[randint(0, len(r)-1)], end=' ')
    elif c == 's':
        print(s[randint(0, len(s)-1)], end=' ')
    elif c == 't':
        print(t[randint(0, len(t)-1)], end=' ')
    elif c == 'u':
        print(u[randint(0, len(u)-1)], end=' ')
    elif c == 'v':
        print(v[randint(0, len(v)-1)], end=' ')
    elif c == 'w':
        print(w[randint(0, len(w)-1)], end=' ')
    elif c == 'x':
        print(x[randint(0, len(x)-1)], end=' ')
    elif c == 'y':
        print(y[randint(0, len(y)-1)], end=' ')
    elif c == 'z':
        print(z[randint(0, len(z)-1)], end=' ')