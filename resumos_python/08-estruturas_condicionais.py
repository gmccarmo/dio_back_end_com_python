'''
# Estruturas Condicionais em Python
São usadas para tomar decisões no código, permitindo executar diferentes blocos de código com base em condições específicas.

# If
A estrutura básica de decisão. Se a condição for verdadeira, o bloco de código dentro do if será executado.
Tendo apenas um único desvio possível.
'''
# Exemplo de uso do if

saldo = 2000.0
saque = float(input("Digite o valor do saque: "))

if saldo >= saque:
    print("Saque realizado com sucesso!")

if saldo < saque:
    print("Saldo insuficiente!")

'''
# If...else
Permite dois desvios possíveis: um bloco de código é executado se a condição for verdadeira, e outro bloco é executado se a condição for falsa.
'''
# Exemplo de uso do if...else

saldo = 2000.0
saque = float(input("Digite o valor do saque: "))

if saldo >= saque:
    print("Saque realizado com sucesso!")

else:
    print("Saldo insuficiente!")

'''
# If...elif...else
Permite múltiplos desvios possíveis. Você pode testar várias condições em sequência, executando o bloco de código correspondente à primeira condição verdadeira.
'''
# Exemplo de uso do if...elif...else

opcao = int(input("Escolha uma opção: \n1 - Sacar \n2 - Depositar \n3 - Extrato \n4 - Sair\n"))
if opcao == 1:
    valor = float(input("Digite o valor do saque: "))
elif opcao == 2:
    valor = float(input("Digite o valor do depósito: "))
elif opcao == 3:
    print("Exibindo extrato...")
else:
    print("Saindo do sistema...")

'''
# If aninhado
Permite colocar uma estrutura condicional dentro de outra, útil para verificar múltiplas condições relacionadas.
'''
# Exemplo de uso do if aninhado
conta_normal = True
conta_universitaria = False
cheque_especial = 500.0

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")        

'''
If ternário
Uma forma concisa de escrever uma estrutura condicional simples em uma única linha.
A primeira expressão é o valor retornado se a condição for verdadeira, e a segunda expressão é a expressão lógica e a terceira parte é o retorno se a condição for falsa.
'''
# Exemplo de uso do if ternário

status = "Sucesso" if saldo >= saque else "Falha"

print(f'{status} ao realizar o saque.')