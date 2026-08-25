import sys
from lexer import Lexer
from parser import Parser

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py arquivo.lisp")
        return

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        texto = f.read()

    lexer = Lexer(texto)
    tokens = lexer.tokenizar()
    print("=== TOKENS ===")
    for tok in tokens:
        print(tok)

    parser = Parser(tokens)
    try:
        codigo, tabela = parser.parse()
        print("\n=== TABELA DE SIMBOLOS ===")
        for nome, end in tabela.items():
            print(f"{nome} -> endereco {end}")
        print("\n=== CODIGO MEPA ===")
        for i, instr in enumerate(codigo):
            print(f"{i:4d}: {instr}")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()