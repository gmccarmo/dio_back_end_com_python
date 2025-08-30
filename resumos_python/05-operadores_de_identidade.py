# Exemplo

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso 
# Saída: True

curso is not nome_curso
# Saída: False

saldo is limite
# Saída: True

saldo = 1000
limite = 1000

print(saldo is limite)
# Saída: False

print(saldo is not limite)
# Saída: True