# print com as boas vindas e serviços
print('Bem vindo a Copiadora do Gabriel Lopes dos Santos')
print()
print('Entre com o tipo de serviço desejado')
print('DIG - Digitalização')
print('ICO - Impressão Colorida')
print('IPB - Impressão Preto e Branco')
print('FOT - Fotocópia')
print()

# função para seleção do serviço, upper evita case sensive e else retorna um erro caso seja escolha invalida
def Seleção_servico():
    while True:
        Servico = input('Selecione o serviço: ').upper()
        if Servico in ['DIG', 'ICO', 'IPB', 'FOT']:
            return Servico
        else:
            print('Escolha inválida, entre com o tipo do serviço novamente')



