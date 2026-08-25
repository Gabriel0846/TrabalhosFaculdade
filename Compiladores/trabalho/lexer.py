class Token:
    def __init__(self, tipo, lexema, linha, coluna):
        self.tipo = tipo
        self.lexema = lexema
        self.linha = linha
        self.coluna = coluna

    def __repr__(self):
        return f"Token({self.tipo}, {self.lexema}, {self.linha}, {self.coluna})"

class Lexer:
    def __init__(self, texto):
        self.texto = texto
        self.pos = 0
        self.linha = 1
        self.coluna = 1
        self.tokens = []
        self.palavras_chave = {'print', 'setq', 'if', 'while'}
        self.operadores = {'+', '-', '*', '/', '>', '<', '='}

    def erro(self, msg):
        # mensagem de erro sem acento
        raise Exception(f"Erro lexico na linha {self.linha}, coluna {self.coluna}: {msg}")

    def proximo_token(self):
        if self.pos >= len(self.texto):
            return Token('EOF', '', self.linha, self.coluna)

        c = self.texto[self.pos]

        # ignora espacos e quebras de linha
        if c.isspace():
            if c == '\n':
                self.linha += 1
                self.coluna = 1
            else:
                self.coluna += 1
            self.pos += 1
            return self.proximo_token()

        # parenteses
        if c == '(':
            tok = Token('LPAREN', '(', self.linha, self.coluna)
            self.pos += 1
            self.coluna += 1
            return tok
        if c == ')':
            tok = Token('RPAREN', ')', self.linha, self.coluna)
            self.pos += 1
            self.coluna += 1
            return tok

        # strings
        if c == '"':
            inicio_col = self.coluna
            self.pos += 1
            self.coluna += 1
            inicio = self.pos
            while self.pos < len(self.texto) and self.texto[self.pos] != '"':
                if self.texto[self.pos] == '\n':
                    self.linha += 1
                    self.coluna = 1
                else:
                    self.coluna += 1
                self.pos += 1
            if self.pos >= len(self.texto):
                self.erro("String nao fechada")
            string = self.texto[inicio:self.pos]
            self.pos += 1
            self.coluna += 1
            return Token('STRING', string, self.linha, inicio_col)

        # numeros
        if c.isdigit():
            inicio_col = self.coluna
            inicio = self.pos
            while self.pos < len(self.texto) and self.texto[self.pos].isdigit():
                self.pos += 1
                self.coluna += 1
            numero = self.texto[inicio:self.pos]
            return Token('NUMERO', numero, self.linha, inicio_col)

        # identificadores e palavras-chave
        if c.isalpha():
            inicio_col = self.coluna
            inicio = self.pos
            while self.pos < len(self.texto) and (self.texto[self.pos].isalnum() or self.texto[self.pos] == '_'):
                self.pos += 1
                self.coluna += 1
            lexema = self.texto[inicio:self.pos]
            if lexema in self.palavras_chave:
                return Token(lexema.upper(), lexema, self.linha, inicio_col)
            else:
                return Token('VAR', lexema, self.linha, inicio_col)

        # operadores (depois de letras e digitos)
        if c in self.operadores:
            tok = Token('OPER', c, self.linha, self.coluna)
            self.pos += 1
            self.coluna += 1
            return tok

        # caractere invalido
        self.erro(f"caractere invalido '{c}'")

    def tokenizar(self):
        while True:
            tok = self.proximo_token()
            self.tokens.append(tok)
            if tok.tipo == 'EOF':
                break
        return self.tokens