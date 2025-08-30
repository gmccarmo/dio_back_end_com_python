'''
# O que são estruturas de repetição?
Estruturas de repetição são usadas para executar um bloco de código várias vezes,
enquanto uma condição específica for verdadeira. Elas são úteis para automatizar tarefas
repetitivas e iterar sobre coleções de dados.

# Tipos de estruturas de repetição em Python
1. for: Usado para iterar sobre uma sequência (como listas, tuplas, dicionários, conjuntos ou strings).
Fazendo mais sentido utilizando quando o número de iterações é conhecido.

Exemplo:
texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
        
print() # Apenas para pular uma linha no final

2. range(): Função built-in que gera uma sequência de números, frequentemente usada com loops for.
Recebe 3 argumentos: start (opcional), stop (obrigatório) e step (opcional).

# Exemplos de uso do range()
for numero in range (0, 11): # Vai de 0 a 10
    print(numero, end=" ")

for numero in range(0, 51, 5): # Vai de 0 a 50, de 5 em 5
    print(numero, end=" ")

Ainda é possível utilizar o break e continue dentro dos loops para controlar o fluxo de execução.
- break: Encerra o loop imediatamente.
- continue: Pula para a próxima iteração do loop.

for numero in range(100):
    if numero == 6:
        break # Sai do loop quando numero é 6

for numero in range(20):
    if numero % 2 == 0:
        continue # Pula os números pares

3. while: Executa um bloco de código enquanto uma condição for verdadeira.

# Exemplo:

opcao =-1

while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Extrato\n[0] Sair\nDigite a opção desejada: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
    elif opcao == 0:
        print("Saindo...")
    else:
        print("Opção inválida, tente novamente.")

# Observação: Cuidado com loops infinitos! Certifique-se de que a condição do while eventualmente se torne falsa.

while True:
    numero = int(input("Digite um número: "))
    
    if numero == 10:
        break
    
    if numero % 2 == 0:
        continue
    
    print(numero)
'''

