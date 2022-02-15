"""
    Exercício 6

    Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
"""

# Intervalo de canais: 1 ~ 10
# Intervalo do volume: 0 ~ 100

class Tv():
    def __init__(self, canal=1, volume=50):
        self.canal = canal
        self.volume = volume

    def num_canal(self, num):
        if 1 <= num <= 10:
            self.canal = num
        else:
            print(f'Canal {num} indisponível, fora da faixa de canais (1 à 10).')

    def aumentar_canal(self):
        if self.canal + 1 > 10:
            print(f'Não é possível aumentar o canal, você já atingiu o canal máximo (10).')
        else:
            self.canal += 1

    def diminuir_canal(self):
        if self.canal - 1 < 10:
            print(f'Não é possível diminuir o canal, você já atingiu o canal mínimo (1).')
        else:
            self.canal -= 1

    def aumentar_volume(self):
        if self.volume + 1 > 100:
            print('Volume máximo (100)')
        else:
            self.volume += 1

    def diminuir_volume(self):
        if self.volume - 1 < 0:
            print('Volume mínimo (0)')
        else:
            self.volume -= 1

    def mostrar_conf(self):
        print(f'Canal: {self.canal} | Volume: {self.volume}')


# Exemplo
tv = Tv(volume=98)
tv.mostrar_conf()

tv.aumentar_canal()
tv.aumentar_canal()
tv.aumentar_canal()
tv.aumentar_canal()
tv.mostrar_conf()

tv.num_canal(12)
tv.mostrar_conf()

tv.aumentar_canal()
tv.aumentar_canal()
tv.aumentar_canal()
tv.mostrar_conf()

tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.mostrar_conf()            

