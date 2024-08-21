#escreva um programa para ler 2 valores (considerando que nao serao informados valores iguais) e escrever o maior deles.

#entrada
valor1 = float (input("qual o primeiro valor ? "))
valor2 = float (input("qual o segundo valor ? ")) 

#processamento
resposta = 0
if valor1 > valor2:
    resposta = valor1
else:
    resposta = valor2

#saida
print (" o maior deles", resposta)        
