'''
A classe string em Python é uma sequência imutável de caracteres que pode ser usada para armazenar e manipular texto. Strings são definidas entre aspas simples (' '), aspas duplas (" ") ou aspas triplas (''' ''' ou """ """).
Possui diversos métodos embutidos que facilitam operações como formatação, busca, substituição e divisão de texto.
Além de ser simples e intuitiva, a classe string é amplamente utilizada em praticamente todos os programas Python, tornando-se uma ferramenta essencial para desenvolvedores.

# Exemplo de uso da classe string:

## Maiusculas, minúsculas e título

curso = "pYtHon"

print(curso.upper())  # Saída: PYTHON

print(curso.lower())  # Saída: python

print(curso.title())  # Saída: Python

## Eliminar espaços em branco

curso = "   Python   "

print(curso.strip() + ".")  # Saída: "Python."

print(curso.lstrip() + ".") # Saída: "Python   ."

print(curso.rstrip() + ".") # Saída: "   Python."

## Junção e centralização
curso = "Python"

print(curso.center(10, "#"))  # Saída: "##Python##"
Obs.: O center pode ser usado sem o caractere de preenchimento, nesse caso o padrão é o espaço.

print(".".join(curso))  # Saída: "P.y.t.h.o.n" 

'''
