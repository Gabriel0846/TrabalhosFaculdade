class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __lt__(self, outro):
        if self.idade != outro.idade:
            return self.idade < outro.idade
        return self.nome < outro.nome

    def __eq__(self, outro):
        return self.idade == outro.idade and self.nome == outro.nome

    def __gt__(self, outro):
        return not self.__lt__(outro) and not self.__eq__(outro)


class Nodo:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.esquerda = None
        self.direita = None


class ArvoreBST:
    def __init__(self):
        self.raiz = None

    def inserir(self, pessoa):
        novo = Nodo(pessoa)
        if self.raiz is None:
            self.raiz = novo
        else:
            self._insere(self.raiz, novo)

    def _insere(self, atual, novo):
        if novo.pessoa < atual.pessoa:
            if atual.esquerda is None:
                atual.esquerda = novo
            else:
                self._insere(atual.esquerda, novo)
        else:
            if atual.direita is None:
                atual.direita = novo
            else:
                self._insere(atual.direita, novo)

    def em_ordem(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        resultado = []
        if nodo:
            if nodo.esquerda:
                resultado.extend(self.em_ordem(nodo.esquerda))
            resultado.append(nodo.pessoa)
            if nodo.direita:
                resultado.extend(self.em_ordem(nodo.direita))
        return resultado

    def pre_ordem(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        resultado = []
        if nodo:
            resultado.append(nodo.pessoa)
            if nodo.esquerda:
                resultado.extend(self.pre_ordem(nodo.esquerda))
            if nodo.direita:
                resultado.extend(self.pre_ordem(nodo.direita))
        return resultado

    def pos_ordem(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        resultado = []
        if nodo:
            if nodo.esquerda:
                resultado.extend(self.pos_ordem(nodo.esquerda))
            if nodo.direita:
                resultado.extend(self.pos_ordem(nodo.direita))
            resultado.append(nodo.pessoa)
        return resultado

    def ordem_invertida(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        resultado = []
        if nodo:
            if nodo.direita:
                resultado.extend(self.ordem_invertida(nodo.direita))
            resultado.append(nodo.pessoa)
            if nodo.esquerda:
                resultado.extend(self.ordem_invertida(nodo.esquerda))
        return resultado

    def largura(self):
        if self.raiz is None:
            return []
        resultado = []
        fila = [self.raiz]
        while fila:
            atual = fila.pop(0)
            resultado.append(atual.pessoa)
            if atual.esquerda:
                fila.append(atual.esquerda)
            if atual.direita:
                fila.append(atual.direita)
        return resultado


def main():
    arvore = ArvoreBST()

    # cadastra uns pessoas
    pessoas = [
        Pessoa("Maria", 50),
        Pessoa("Pedro", 40),
        Pessoa("Joao", 20),
        Pessoa("Bruno", 33),
        Pessoa("Tulio", 40),
        Pessoa("Luiz", 60),
        Pessoa("Lucas", 55),
        Pessoa("Marcos", 70),
        Pessoa("Ana", 25),
        Pessoa("Carla", 30),
        Pessoa("Rafael", 45),
        Pessoa("Sofia", 35)
    ]

    for p in pessoas:
        arvore.inserir(p)

    # mostra os resultados
    print("In Order:")
    for p in arvore.em_ordem():
        print(f"    Nome: {p.nome:<8} - Idade: {p.idade}")
    print()

    print("Pre Order:")
    for p in arvore.pre_ordem():
        print(f"    Nome: {p.nome:<8} - Idade: {p.idade}")
    print()

    print("Pos Order:")
    for p in arvore.pos_ordem():
        print(f"    Nome: {p.nome:<8} - Idade: {p.idade}")
    print()

    print("Dec Order:")
    for p in arvore.ordem_invertida():
        print(f"Nome: {p.nome:<8} - Idade: {p.idade}")
    print()

    print("Largura:")
    for p in arvore.largura():
        print(f"Nome: {p.nome:<8} - Idade: {p.idade}")
    print()

    # so pra confirmar q ta certo
    print("=" * 50)
    print(f"Total de pessoas: {len(pessoas)}")
    print("A arvore segue a regra: idade primeiro, nome depois")
    print("Se idade e nome igual, vai pra direita")
    print("=" * 50)


if __name__ == "__main__":
    main()