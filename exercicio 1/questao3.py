# print com as boas vindas e serviços
print('Bem vindo a Copiadora do Gabriel Lopes dos Santos')


# função para seleção do serviço, upper evita case sensive e else retorna um erro caso seja escolha invalida
def Seleção_servico():
    while True:
        print()
        print('Entre com o tipo de serviço desejado')
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')
        print()
        Servico = input('>> ').upper()
        if Servico in ['DIG', 'ICO', 'IPB', 'FOT']:
            return Servico
        else:
            print('Escolha inválida, entre com o tipo do serviço novamente')

def N_paginas():
    while True:
        try:
            Num_p = int(input('Digite o numero de páginas: '))
            if Num_p >= 20000:
                print('Não aceitamos tantas páginas de uma vez.')
                print('Por favor, digite o numero de paginas novamente.')
            else:
                if Num_p < 20:
                    return Num_p
                elif Num_p < 200:
                    return int(Num_p * 0.85)
                elif Num_p < 2000:
                    return int(Num_p * 0.80)
                else:
                    return int(Num_p * .75)
        except ValueError:
            print('Numero de paginas invalido, por favor digite um numero inteiro.')

def S_extra():
    print('Deseja adicionar algum serviço extra?')
    print('1 - Encadernação Simples - R$ 15.00')
    print('2 - Encadernação Capa Dura - R$ 40.00')
    print('0 - Não desejo mais nada')
    while True:
        S_extra = input('>> ')
        if S_extra in ['1', '2', '0']:
            return  int(S_extra)
        else:
            print('Escolha inválida, tente novamente.')

Servico = Seleção_servico()
num_pag = N_paginas()
extra = S_extra()