# Interpolação de Variáveis em Strings
'''
A interpolação de variáveis em strings é uma técnica que permite inserir valores de variáveis diretamente dentro de uma string. Isso facilita a criação de mensagens dinâmicas e a formatação de texto.
Existem várias maneiras de realizar a interpolação de variáveis em Python, incluindo o uso do operador `%`, o método `str.format()` e as f-strings (disponíveis a partir do Python 3.6).
A primeira não sendo mais recomendada, mas ainda funcional. As f-strings são a forma mais moderna e eficiente de interpolar variáveis em strings.

## Estilos de Interpolação
# Usando o operador % - utiliza-se de especificadores de formato como %s para strings, %d para inteiros, %f para floats, entre outros.
Também é importante manter a ordem das variáveis ao usar esse método, pois elas são inseridas na string na ordem em que aparecem.

nome = "Alice"
idade = 30
print("Meu nome é %s e eu tenho %d anos." % (nome, idade))
# Saída: Meu nome é Alice e eu tenho 30 anos.

# Usando o método str.format() - permite a inserção de variáveis em posições específicas dentro da string.
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))
# Saída: Meu nome é Alice e eu tenho 30 anos.


'''