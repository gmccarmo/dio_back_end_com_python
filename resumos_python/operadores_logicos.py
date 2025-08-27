# Exemplo
saldo = 1000
saque = 200
limite = 100

saldo >= saque # Saída: True
saque <= limite # Saída: False

# Operador 'E'
saldo >= saque and saque <= limite # Saída: False

# Operador 'OU'
saldo >= saque or saque <= limite # Saída: True

# Operador de negação
contatos_emergencia = [] # Lista vazia é considerada False

not 1000 > 1500 
# Saída: True

not contatos_emergencia 
# Saída: True

not "saque 1500;" # String não vazio é considerado True
# Saída: False

not "" # String vazia é considerado False
# Saída: True

# Parênteses para agrupar expressões
saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)
# Saída: True

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)
# Saída: True

saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo = (conta_especial and saldo >= saque)
exp_3 = saldo_suficiente or conta_especial_com_saldo
print(exp_3)
