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
            return servico
        else:
            print('Escolha inválida, entre com o tipo do serviço novamente')

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
                    return int(num_p * 0.85)
                elif num_p < 2000:
                    return int(num_p * 0.80)
                else:
                    return int(num_p * .75)
        except ValueError:
            print('Numero de paginas invalido, por favor digite um numero inteiro.')

def servico_extra():
    print('Deseja adicionar algum serviço extra?')
    print('1 - Encadernação Simples - R$ 15.00')
    print('2 - Encadernação Capa Dura - R$ 40.00')
    print('0 - Não desejo mais nada')
    while True:
        s_extra = input('>> ')
        if s_extra in ['1', '2', '0']:
            return int(s_extra)
        else:
            print('Escolha inválida, tente novamente.')

servico = escolha_servico()
num_p = num_pagina()
extra = servico_extra()

if servico == 'DIG':
    v_serviço = num_p * 1.10
elif servico == 'ICO':
    v_serviço = num_p * 1.00
elif servico == 'IPB':
    v_serviço = num_p * 0.40
else:
    v_serviço = num_p * 0.20

if extra == 1:
    v_extra = 15
elif extra == 2:
    v_extra = 40
else:
    v_extra = 0

total = v_serviço + v_extra

print(f'Total: R$ {total:.2f} (Serviço: {v_serviço:.2f} X Páginas: {num_p} + Extra: {v_extra:.2f})')


