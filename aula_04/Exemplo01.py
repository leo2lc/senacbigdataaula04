# Verifica se é maior de idade
# idade = int(input('Informe sua idade: '))

# if idade >= 18:
#     print('Autorizado')
# else:
#     print('Não autorizado')
#___________________________________________________________________

# Testando com mais condições
# Teste de pontos

# pontos = int(input('Quantos pontos? '))

# if pontos >= 100:
#     print('Nível máximo!')
# elif pontos >= 50:
#     print('Nível bom!')
# elif pontos >= 25:
#     print('Nível ruim')
# else:
#     print('Pontuação Baixa')
#____________________________________________________________________

# Verificação de login

# usuario = input('Informe o usuario: ').lower()
# senha = input('Digite a senha: ')

# if usuario == 'admin' and senha == '1234':    # "and" para mais de um critério no "if"
#     print('acesso permitido')
# else:
#     print('acesso negado, usuário ou senha incorretos')
#____________________________________________________________________

# Condição para premiação

# compra = float(input('valor da compra: R$'))
# cliente_frequente = input('Cliente frequente? [S/N]').lower()

# if compra >= 1000 or cliente_frequente == 's':
#     print('Tem direito a brinde')
# else:
#     print('Sem brinde')
#____________________________________________________________________

# Verificação de Nota e Freqüência

nota = float(input('Informe a nota: '))
frequencia = float(input('Informe a freqüência: '))

if nota >= 7:
    if frequencia >= 75:
        print('APROVADO')
    else:
        print('Boa nota, mas reprovado por falta')
else:
    print('reprovado por nota!')