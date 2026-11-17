import itertools
import re
from typing import List, Dict


class CalculadoraTabelaVerdade:
    """Calculadora de tabela-verdade com suporte a 4 variáveis (A, B, C, D)."""

    PRECEDENCIA = {
        '∼': 5,
        '∧': 4,
        '∨': 3, '⊻': 3, '↓': 3, '↑': 3,
        '→': 2,
        '↔': 1,
    }

    # Aliases aceitos na digitação.
    # Convenção booleana: + = OU, . = E  (o ponto tem precedência maior que o +, igual à matemática)
    ALIASES = {
        # negação
        '~': '∼', '!': '∼', 'not': '∼', 'NOT': '∼',
        # conjunção (E)
        '.': '∧', '·': '∧', '&': '∧', '^': '∧', 'and': '∧', 'AND': '∧',
        # disjunção (OU)
        '+': '∨', '|': '∨', 'or': '∨', 'OR': '∨',
        # implicação / equivalência
        '<->': '↔', '<=>': '↔',
        '->': '→', '=>': '→',
        # outros
        'xor': '⊻', 'XOR': '⊻',
        'nor': '↓', 'NOR': '↓',
        'nand': '↑', 'NAND': '↑',
    }

    def __init__(self, formula: str):
        self.formula_original = formula
        self.formula = self._normalizar(formula)
        self.variaveis = self._extrair_variaveis()
        self.tokens = self._tokenizar(self.formula)
        self.posfixa = self._infixa_para_posfixa(self.tokens)

    def _normalizar(self, formula: str) -> str:
        formula = formula.strip()
        # Aliases mais longos primeiro para evitar conflitos ('<->' antes de '->')
        for alias in sorted(self.ALIASES.keys(), key=len, reverse=True):
            formula = formula.replace(alias, self.ALIASES[alias])
        formula = re.sub(r'\s+', '', formula)
        return formula

    def _extrair_variaveis(self) -> List[str]:
        encontradas = set(re.findall(r'[A-Da-d]', self.formula))
        return sorted(v.upper() for v in encontradas)

    def _tokenizar(self, formula: str) -> List[str]:
        tokens = []
        for c in formula:
            if c in 'ABCD':
                tokens.append(c)
            elif c in '∼∧∨→↔⊻↓↑()':
                tokens.append(c)
            else:
                raise ValueError(f"Caractere inválido na fórmula: '{c}'")
        return tokens

    def _infixa_para_posfixa(self, tokens: List[str]) -> List[str]:
        saida, pilha = [], []
        for token in tokens:
            if token in 'ABCD':
                saida.append(token)
            elif token == '(':
                pilha.append(token)
            elif token == ')':
                while pilha and pilha[-1] != '(':
                    saida.append(pilha.pop())
                if not pilha:
                    raise ValueError("Parênteses desbalanceados: ')' sem '('")
                pilha.pop()
            elif token == '∼':
                pilha.append(token)
            else:
                while (pilha and pilha[-1] != '(' and pilha[-1] != '∼'
                       and self.PRECEDENCIA.get(pilha[-1], 0) >= self.PRECEDENCIA[token]):
                    saida.append(pilha.pop())
                pilha.append(token)
        while pilha:
            topo = pilha.pop()
            if topo == '(':
                raise ValueError("Parênteses desbalanceados: '(' sem ')'")
            saida.append(topo)
        return saida

    def _avaliar(self, valores: Dict[str, bool]) -> bool:
        pilha: List[bool] = []
        for token in self.posfixa:
            if token in 'ABCD':
                pilha.append(valores[token])
            elif token == '∼':
                pilha.append(not pilha.pop())
            else:
                if len(pilha) < 2:
                    raise ValueError(f"Operador '{token}' sem operandos suficientes")
                b = pilha.pop()
                a = pilha.pop()
                if token == '∧':   pilha.append(a and b)
                elif token == '∨': pilha.append(a or b)
                elif token == '→': pilha.append((not a) or b)
                elif token == '↔': pilha.append(a == b)
                elif token == '⊻': pilha.append(a != b)
                elif token == '↓': pilha.append(not (a or b))
                elif token == '↑': pilha.append(not (a and b))
        if len(pilha) != 1:
            raise ValueError("Fórmula inválida (pilha com mais de um valor)")
        return pilha[0]

    def gerar_tabela(self) -> str:
        if not self.variaveis:
            raise ValueError("A fórmula não contém variáveis (A, B, C, D)")
        n = len(self.variaveis)
        linhas = [self.variaveis + [self.formula_original.strip()]]
        for combinacao in itertools.product([False, True], repeat=n):
            valores = dict(zip(self.variaveis, combinacao))
            resultado = self._avaliar(valores)
            linhas.append(['1' if v else '0' for v in combinacao] +
                          ['1' if resultado else '0'])
        return self._formatar_tabela(linhas)

    @staticmethod
    def _formatar_tabela(linhas: List[List[str]]) -> str:
        larguras = [max(len(l[i]) for l in linhas) for i in range(len(linhas[0]))]
        montar = lambda l: ' | '.join(c.ljust(larguras[i]) for i, c in enumerate(l))
        sep = '-+-'.join('-' * w for w in larguras)
        out = [montar(linhas[0]), sep]
        for linha in linhas[1:]:
            out.append(montar(linha))
        return '\n'.join(out)


def main():
    print("=" * 60)
    print(" CALCULADORA DE TABELA-VERDADE")
    print("=" * 60)
    print("Variáveis:  A, B, C, D")
    print("Notação booleana:  + = OU   . = E   ~ = NÃO")
    print("Simbólica:         ∨ = OU   ∧ = E   ∼ = NÃO")
    print("Outros:  → ↔ ⊻ ↓ ↑   e  parênteses ( )")
    print()
    print("Exemplos:  A + B.C      (A + B).C      ~A + B      A -> B")
    print("Digite 'sair' para encerrar.\n")

    while True:
        try:
            entrada = input("Fórmula: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAté logo!"); break
        if entrada.lower() in ('sair', 'exit', 'quit', ''):
            break
        try:
            calc = CalculadoraTabelaVerdade(entrada)
            print(f"\nVariáveis: {', '.join(calc.variaveis)}")
            print(f"Normalizada: {calc.formula}\n")
            print(calc.gerar_tabela())
            print()
        except ValueError as e:
            print(f"  ⚠ Erro: {e}\n")


if __name__ == '__main__':
    main()