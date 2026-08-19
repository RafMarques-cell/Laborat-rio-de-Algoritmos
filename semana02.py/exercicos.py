1:Um haras necessita trocar todas as ferraduras dos cavalos. Sabe-se que o valor de cada ferradura custa R$80,00. Para isso, faça um algoritmo que solicite o número de cavalos e apresente o valor total

cavalos = int(input("Digite o número de cavalos: "))

total = cavalos * 4 * 80

print(f"O valor total é R$ {total:.2f}")

→ 10 × 4 × 80 = R$ 3.200,00.

2:Uma determinada loja de roupas acrescenta 30% no valor de fábrica de cada peça para ser vendida. Faça um algoritmo em Python que leia o preço de fábrica de uma peça e apresenta o valor final.

preco_fabrica = float(input("Digite o preço de fábrica da peça: ")) 

valor_final = preco_fabrica * 1.30 

print(f"O valor final da peça é R$ {valor_final:.2f}")

Digite o preço de fábrica da peça: R$ 3.00
O valor final da peça é R$ 3.90

3:Crie um algoritmo para exibir o dobro e a metade de um número.
Utilize a função input.

numero = float(input("Digite um número: ")) 
dobro = numero * 2 
metade = numero / 2 

print(f"O dobro é: {dobro}") 
print(f"A metade é: {metade}")

Digite um número: 10
O dobro é: 20.0
A metade é: 5.0

4:Faça um algoritmo que leia o ano de nascimento de uma pessoa e apresente quantos anos a pessoa tem neste ano. Considere que todas as pessoas já fizeram aniversário neste ano

ano_nascimento = int(input("Digite o ano de nascimento: ")) 

idade = 2026 - ano_nascimento 

print(f"A pessoa tem {idade} anos.")

Digite o ano de nascimento: 2006
A pessoa tem 20 anos.

5:Uma empresa deseja trocar os pneus de toda frota de carros. Sabe-se que cada pneu custa R$395,40. Com isso, leia o total de carros e apresente o valor final.
Utilize a função input.

carros = int(input("Digite o total de carros: ")) 

valor_final = carros * 4 * 395.40 

print(f"O valor final é R$ {valor_final:.2f}")

Digite o total de carros: 15
O valor final é R$ 23724.00

6:Uma determinada loja de roupas dá 18% de desconto no valor de fábrica de cada peça para ser vendida. Faça um algoritmo em Python que leia o preço de venda de uma peça e apresenta o valor final.

preco_venda = float(input("Digite o preço da peça: ")) 

valor_final = preco_venda * 0.82 

print(f"O valor final da peça é R$ {valor_final:.2f}")

Digite o preço da peça: 20
O valor final da peça é R$ 16.40

7:Faça um algoritmo para calcular o salário mensal de um funcionário. Sabe-se que o funcionário recebe R$35,00 por hora, faça um algoritmo que leia o total de horas trabalhadas no mês e apresente o salário final. Se o salário for menor que R$1000,00 dê um aumento de R$300,00 no salário recebido, senão apresente somente o resultado da multiplicação.

horas = float(input("Digite o total de horas trabalhadas no mês:"))

salario = horas * 35

if salario < 1000:
    salario = salario + 300

print(f"Salario final: R$ {salario:.2f}")

Digite o total de horas trabalhadas no mês:12
Salario final: R$ 720.00
