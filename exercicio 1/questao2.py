# print de boas vindas junto com a lista dos produtos
print('  Bem-vindo a loja de gelados do Gabriel Lopes dos Santos  ')
print('                          CARDÁPIO                        ')
print('     ________________________________________________     ')
print('    |   TAMANHO   |   CUPUAÇU (CP)   |   AÇAI (AC)   |    ')
print('   |       P      |    R$  9.00      |   R$ 11.00     |   ')
print('   |       M      |    R$ 14.00      |   R$ 16.00     |   ')
print('    |      G      |    R$ 18.00      |   R$ 20.00    |    ')
print('     ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´     ')
print()

# variavel que ira receber o total do pedido
Total = 0

# Loop principal para fazer o pedido e verificar se é valido
while True:
    # input de sabor, adicionei .upper() para usuario não ter problema com case sensive
    Sabor = input("Digite o sabor desejado (CP ou AC): ").upper()

    # verifica se o sabor digitado é como os exibidos na tabela, caso não for retorna invalido e retorna no loop
    if Sabor not in ['CP', 'AC']:
        print("Sabor inválido. Tente novamente.")
        print()
        continue

    # mesmo principio do sabor acima
    Tamanho = input("Digite o tamanho desejado (P, M, ou G): ").upper()
    if Tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido. Tente novamente.")
        print()
        continue

    # verificação do preco do produto pela combinação escolhida nos inputs, e adicionando o preço ao Total
    if Sabor == 'CP':
        if Tamanho == 'P':
            print('Você pediu um Cupuaçu de tamanho P: R$ 9.00')
            print()
            Total += 9
        elif Tamanho == 'M':
            print('Você pediu um Cupuaçu de tamanho M: R$ 14.00')
            print()
            Total += 14
        elif Tamanho == 'G':
            print('Você pediu um Cupuaçu de tamanho G: R$ 18.00')
            print()
            Total += 18
    elif Sabor == 'AC':
        if Tamanho == 'P':
            print('Você pediu um Açai de tamanho p: R$ 11.00')
            print()
            Total += 11
        elif Tamanho == 'M':
            print('Você pediu um Açai de tamanho M: R$ 16.00')
            print()
            Total += 16
        elif Tamanho == 'G':
            print('Você pediu um Açai de tamanho G: R$ 20.00')
            print()
            Total += 20

    # pergunta se o usuario quer fazer mais algum pedido, caso sim retorna no loop.
    # adicionei .upper aqui tambem para evitar problema de case sensive
    continuar = input('Deseja pedir mais alguma coisa? (S/N): ').upper()
    if continuar != 'S':
        break

# da um print com o valor total da compra
print()
print(f'Valor total a ser pago: R$ {Total:.2f}')