# print com a mensagem de boas vindas
print('Bem-vindo a Loja do Gabriel Lopes dos Santos')

# Entrada do valor unitario
preco = float(input('Digite o valor do produto: '))

# Entrada da quantidade do produto
quantidade = float(input('Digite a quantidade do produto: '))

# calcula o valor total da compra
Total = preco * quantidade

# calculo dos descontos
if Total < 2500:
    desconto = 0
elif Total >= 2500 and Total < 6000:
    desconto = 4
elif Total >= 6000 and Total < 10000:
    desconto = 7
# caso não se enquadre em nenhum dos testes acima, então é total é maior que 10000
else:
    desconto = 11

# calcula o valor do desconto
Valor_desconto = (Total * desconto) / 100

# calcula o valor com desconto
Total_desconto = Total - Valor_desconto

# print do valor total sem o desconto
print(f"Valor total sem desconto: R$ {Total:.2f}")

# se houver desconto retorna o valor com desconto
if desconto >= 4:
    print(f"Valor total com desconto: R$ {Total_desconto:.2f}")
