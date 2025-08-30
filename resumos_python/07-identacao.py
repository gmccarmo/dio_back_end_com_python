'''
# Estética
Identar código é uma forma de manter o código fonte mais legível e manutenível.
Em Python ela exerce um papel fundamental, pois a linguagem utiliza a indentação para definir blocos de código,

# Bloco de comando
As linguagens de programação costumam utilizar chaves ({}) ou palavras-chave (como begin e end) para definir blocos de código.
Em Python, a indentação (espaços em branco no início de uma linha) é usada para esse propósito.

# Convenção de indentação
A convenção mais comum é usar 4 espaços para cada nível de indentação.
É importante ser consistente com a quantidade de espaços usados em todo o código.
No VSCode, você pode configurar para que a tecla Tab insira 4 espaços, além de configurar a exibição de espaços em branco.
Nele também é possível configurar a formatação automática do código ao salvar o arquivo, o que ajuda a manter a indentação correta.
Quando estiver dentro de um bloco, irá aparecer uma linha vertical indicando o nível de indentação atual, de forma a não se perder.
'''

# Exemplo de bloco de código em Python

def sacar(valor): #inicio do bloco do método
    saldo = 1000 #definição de variável dentro do bloco

    if saldo >= valor: # início do bloco do if
        print("Saque realizado com sucesso!")
    # fim do bloco do if

    print("Obrigado por usar nosso banco!") #continuação do bloco do método fora do if
# fim do bloco do método

# Exemplo incorreto de indentação, onde irá gerar um erro de indentação
def depositar(valor): #inicio do bloco do método
saldo = 500
saldo += valor