# print com as boas vindas e serviços
print('Bem vindo a Copiadora do Gabriel Lopes dos Santos')


# função para seleção do serviço, upper evita case sensive e else retorna um erro caso seja escolha invalida
def escolha_servico():
    while True:
        print()
        print('Entre com o tipo de serviço desejado')
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')
        servico = input('>> ').upper()
        if servico in ['DIG', 'ICO', 'IPB', 'FOT']:
            if servico == 'DIG':
                return 0.10
            elif servico == 'ICO':
                return 1.00
            elif servico == 'IPB':
                return 0.40
            else:
                return 0.20
        else:
            print('Escolha inválida, entre com o tipo do serviço novamente')


# função de numero de paginas verifica no try except se o valor digitado é maior que 20000 e se não são letras respectivamente
# se os dados forem validos, retorna o numero de paginas com desconto aplicado, sequguindo a regra para aplicar segundo quantidade de paginas
def num_pagina():
    while True:
        try:
            num_p = int(input('Digite o numero de páginas: '))
            if num_p >= 20000:
                print('Não aceitamos tantas páginas de uma vez.')
                print('Por favor, digite o numero de paginas novamente.')
                print()
            else:
                if num_p < 20:
                    return num_p
                elif num_p < 200:
                    return int((num_p * 85) / 100)
                elif num_p < 2000:
                    return int((num_p * 80) / 100)
                else:
                    return int((num_p * 75) / 100)
        except ValueError:
            print('Numero de paginas invalido, por favor tente novamente.')


# função que pergunta se o usuario quer algum serviço extra e retorna o valor do serviço extra
def servico_extra():
    print('Deseja adicionar algum serviço extra?')
    print('1 - Encadernação Simples - R$ 15.00')
    print('2 - Encadernação Capa Dura - R$ 40.00')
    print('0 - Não desejo mais nada')
    while True:
        s_extra = input('>> ')
        if s_extra in ['1', '2', '0']:
            if s_extra == '1':
                return 15
            elif s_extra == '2':
                return 40
            else:
                return 0
        else:
            print('Escolha inválida, tente novamente.')


# atribuo ao retorno de cada função um nome mais usual
servico = escolha_servico()
num_p = num_pagina()
extra = servico_extra()

# faço a soma dos serviços
total = (servico * num_p) + extra

# print do total do serviço, com detalhes do valor do tipo de serviço, numero de paginas, e serviço extra
print(f'Total: R$ {total:.2f} (Serviço: {servico:.2f} X Páginas: {num_p} + Extra: {extra:.2f})')
