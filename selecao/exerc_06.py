# Reescreva o programa do exercício anterior considerando o zero como neutro, ou seja, se for digitado o valor zero, escrever a palavra zero.

#entrada
valor= int(input ("escreva um valor : "))

#processamento
resposta = ""
if valor == 0:
    resposta = "zero"
elif valor > 0:
    resposta = "positivo"
else:
    resposta = "negativo"    

#saida    
print ("o valor é ", resposta)