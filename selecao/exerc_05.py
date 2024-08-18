#  Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.

#entrada
valor= int(input ("escreva um valor : "))

#processamento
resposta = ""
if valor >= 0:
    resposta = "positivo"
else:
    resposta ("negativo")

#saida    
print ("o valor é ", resposta)