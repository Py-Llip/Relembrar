import string
import random

class Cruzadinha:
    alfabeto = list(string.ascii_lowercase)
    def __init__(self, lista_palavras, altura, largura):
        self.lista_palavras = lista_palavras
        self.altura = altura
        self.largura = largura
        self.cruzadinha_0 = []
        self.celulas = {} #{(x, y): {'letra': 'a', 'palavra': 'qualquer'}}

    def criar_cruzadinha(self):
        self.cruzadinha_0 = []
        for l in range(1, self.altura+1):
            self.cruzadinha_0.append([random.choice(Cruzadinha.alfabeto) for n in range(self.largura)])
        print(self.cruzadinha_0)

    def _misturar_cruzadinha(self):
        def fabricar_celulas(letra: str, palavra: str, posicao: tuple = (0, 0)):
            if self.celulas:
                arm_chaves_iguais = []
                for k in self.celulas.keys():
                    if k[0] == letra:
                        arm_chaves_iguais.append(int(k[1:]))
                if arm_chaves_iguais:
                    maior = 0
                    for e, k in enumerate(arm_chaves_iguais):
                        if e == 0:
                            maior = k
                        if k > maior:
                            maior = k
                    letra = letra + str(maior + 1)
                else:
                    letra = letra + '0'
            else:
                letra = letra + '0'
            self.celulas[letra] = {'posicao': posicao, 'letra': letra[0], 'palavra': palavra}
            return letra


        for p in self.lista_palavras:
            possibilidades = []
            tentativas = 0
            while tentativas <= 100:
                print(possibilidades)
                tentativas += 1
                a = random.randint(0, self.altura-1)
                l = random.randint(0, self.largura-1)
                direcao = random.choice(['^', '>'])
                if (a, l, direcao) in possibilidades:
                    tentativas -= 1
                    continue
                possibilidades.append((a, l, direcao))
                vai_invertida = random.choice([True, False])
                if vai_invertida:
                    p = p[::-1]
                reiniciar_while = False
                #preenchimento_palavra = []
                if direcao == '^' and len(p) + a <= self.altura:
                    for n, y in enumerate(range(a, len(p) + a)):
                        nome_celula = fabricar_celulas(p[n], p, (l, y))
                        if self._verificacao_conflitos_cruzadinha(nome_celula):
                            reiniciar_while = True
                            break
                        #preenchimento_palavra.append(p[n])
                        self.cruzadinha_0[y][l] = p[n]
                        print('Passou')
                    if reiniciar_while:
                        print('reiniciou')
                        continue
                    break

                elif direcao == '>' and len(p) + l <= self.largura:
                    for n, x in enumerate(range(l, len(p) + l)):
                        nome_celula = fabricar_celulas(p[n], p, (x, a))
                        if self._verificacao_conflitos_cruzadinha(nome_celula):
                            reiniciar_while = True
                            break
                        self.cruzadinha_0[a][x] = p[n]
                    if reiniciar_while:
                        continue
                    break
            else:
                print(f'Não foi possível encaixar "{p}" na cruzadinha, verifique o tamanho da palavra, tamanho da cruzadinha ou tente novamente.')
        self.executar_cruzadinha()

    def _verificacao_conflitos_cruzadinha(self, nome_celula: str):
        print(self.celulas[nome_celula])
        for k, v in self.celulas.items():
            if self.celulas[nome_celula]['posicao'] == v['posicao']:
                if self.celulas[nome_celula]['letra'] == v['letra']:
                    continue
                else:
                    del self.celulas[nome_celula]
                    return True
        return False

    def executar_cruzadinha(self):
        for l in self.cruzadinha_0:
            for c in l:
                print(c, end='  ')
            print()
        print(self.celulas)

a = Cruzadinha(['úááú' ,'úóóú', 'óááó', 'áóóá'], 4, 4)
a.criar_cruzadinha()
a._misturar_cruzadinha()

