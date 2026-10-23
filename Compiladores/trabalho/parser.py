from lexer import Token, Lexer

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.tabela_simbolos = {}
        self.proximo_endereco = 0
        self.codigo = []

    def erro(self, msg):
        tok = self.tokens[self.pos] if self.pos < len(self.tokens) else None
        linha = tok.linha if tok else 0
        coluna = tok.coluna if tok else 0
        # mensagem sem acento
        raise Exception(f"Erro sintatico na linha {linha}, coluna {coluna}: {msg}")

    def erro_semantico(self, msg):
        tok = self.tokens[self.pos] if self.pos < len(self.tokens) else None
        linha = tok.linha if tok else 0
        coluna = tok.coluna if tok else 0
        # mensagem sem acento
        raise Exception(f"Erro semantico na linha {linha}, coluna {coluna}: {msg}")

    def espera(self, tipo):
        if self.pos >= len(self.tokens):
            self.erro(f"esperado {tipo} mas encontrou fim de arquivo")
        tok = self.tokens[self.pos]
        if tok.tipo != tipo:
            self.erro(f"esperado {tipo} mas encontrou {tok.tipo} ({tok.lexema})")
        self.pos += 1
        return tok

    def olhar(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consome(self, tipo=None):
        tok = self.olhar()
        if not tok:
            self.erro("fim de arquivo inesperado")
        if tipo and tok.tipo != tipo:
            self.erro(f"esperado {tipo} mas veio {tok.tipo}")
        self.pos += 1
        return tok

    def programa(self):
        # programa = sequencia de expressoes
        while self.olhar() and self.olhar().tipo != 'EOF':
            self.expressao()
        self.codigo.append('PARA')

    def expressao(self):
        tok = self.olhar()
        if not tok:
            return
        if tok.tipo == 'LPAREN':
            self.pos += 1
            op = self.consome()
            if op.lexema == 'print':
                self.expressao()
                self.codigo.append('IMPRIME')
                self.espera('RPAREN')
            elif op.lexema == 'setq':
                var_tok = self.consome('VAR')
                nome = var_tok.lexema
                if nome not in self.tabela_simbolos:
                    self.tabela_simbolos[nome] = self.proximo_endereco
                    self.proximo_endereco += 1
                self.expressao()
                self.codigo.append(f'STO {self.tabela_simbolos[nome]}')
                self.espera('RPAREN')
            elif op.lexema == 'if':
                self.expressao()  # condicao
                rot_falso = f'rot_{len(self.codigo)}'
                self.codigo.append(f'DESVIF {rot_falso}')
                self.expressao()  # then
                rot_fim = f'rot_{len(self.codigo)}'
                self.codigo.append(f'DESV {rot_fim}')
                self.codigo.append(f'{rot_falso}:')
                self.expressao()  # else
                self.codigo.append(f'{rot_fim}:')
                self.espera('RPAREN')
            elif op.lexema in ('+', '-', '*', '/', '>', '<', '='):
                self.expressao()
                self.expressao()
                mapeamento = {
                    '+': 'SOMA',
                    '-': 'SUB',
                    '*': 'MULT',
                    '/': 'DIV',
                    '>': 'MAIOR',
                    '<': 'MENOR',
                    '=': 'IGUAL'
                }
                self.codigo.append(mapeamento[op.lexema])
                self.espera('RPAREN')
            else:
                self.erro(f"operador desconhecido '{op.lexema}'")
        elif tok.tipo == 'VAR':
            nome = tok.lexema
            if nome not in self.tabela_simbolos:
                # erro semantico (variavel nao declarada)
                self.erro_semantico(f"variavel '{nome}' nao declarada")
            self.codigo.append(f'LOD {self.tabela_simbolos[nome]}')
            self.pos += 1
        elif tok.tipo == 'NUMERO':
            self.codigo.append(f'LIT {tok.lexema}')
            self.pos += 1
        elif tok.tipo == 'STRING':
            self.codigo.append(f'LIT "{tok.lexema}"')
            self.pos += 1
        else:
            self.erro(f"expressao invalida: {tok}")

    def parse(self):
        self.programa()
        return self.codigo, self.tabela_simbolos