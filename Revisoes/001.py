"""1. **Listas e Condições**

python
# Filtrar todos os números pares e positivos de uma lista e elevar ao quadrado.
numeros = [10, -3, 4, -7, 0, 8, 13, -2]
# Faça: lista_pares_quadrado = [...]
"""

class Filtro:
    def __init__(self, lista: list):
        self.lista = lista

    def filtrar(self):
        nova_lista = []
        for i in self.lista:
            if i % 2 == 0 and i > 0:
                nova_lista.append(i * i)
        return nova_lista

numeros = [10, -3, 4, -7, 0, 8, 13, -2, 2]
f = Filtro(numeros)
print(f.filtrar())