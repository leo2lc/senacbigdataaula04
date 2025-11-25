valor = float(input('Qual o valor da compra? '))


if valor >= 250:
    desconto = valor * 0.84
    print(f'O desconto é de: {desconto}')
else:
    print(f'Não tem desconto para compras de {valor}')