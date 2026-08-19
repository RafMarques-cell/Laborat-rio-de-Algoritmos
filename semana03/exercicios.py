
1:Faça um algoritmo para calcular o salário mensal de um funcionário. Sabe-se que o funcionário recebe R$35,00 por hora, faça um algoritmo que leia o total de horas trabalhadas no mês e apresente o salário final. Se o salário for menor que R$1000,00 dê um aumento de R$300,00 no salário recebido, senão apresente somente o resultado da multiplicação.

horas = float(input("Digite o total de horas trabalhadas no mês:"))

salario = horas * 35

if salario < 1000:
    salario = salario + 300

print(f"Salario final: R$ {salario:.2f}")

Digite o total de horas trabalhadas no mês:12
Salario final: R$ 720.00

2:Faça um algoritmo que leia dois números distintos e apresente-os em ordem crescente.

numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo número:"))

if numero1 < numero2:
   print(numero1, numero2)
else:
   print(numero2, numero1)

Digite o primeiro número:12
Digite o segundo número:16
12.0 16.0

3:Faça um algoritmo que leia o ano de nascimento de uma pessoa e verifique se ela pode ou não votar (desconsidere o mês de nascimento).

ano_nascimento = int(input("Digite o ano de nascimento:"))
ano_atual = 2026

idade = ano_atual - ano_nascimento

if idade >= 16:
    print("Você pode votar.")
else:
    print("Você não pode votar")

Digite o ano de nascimento:2003
Você pode votar.

4:Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.

preco_litro = float(input("Digite o preço do litro  da gasolina: R$"))
pagamento = float(input("Digite o valor de pagamento: R$"))

litros = pagamento / preco_litro

print("Você conseguir colocar litros no tanque:", litros)

Digite o preço do litro  da gasolina: R$5.60
Digite o valor de pagamento: R$100
Você conseguir colocar litros no tanque: 17.857142857142858

5:Escreva um algoritmo em Python que dada a idade de uma pessoa, determine sua classificação:
maior de idade;
menor de idade;

idade = int(input("Digite a sua idade: "))

# Verifica a classificação de idade
if idade >= 18:
    print("Classificação: Maior de idade")
elif idade >= 0:
    print("Classificação: Menor de idade")
else:
    print("Idade inválida! Digite um valor maior ou igual a zero.")

Digite a sua idade: 20
Classificação: Maior de idade

6:eia um número fornecido pelo usuário. Se esse número for positivo, apresente o dobro do valor digitado. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

# Solicita um número ao usuário (pode ser inteiro ou com casas decimais)
numero = float(input("Digite um número: "))

# Verifica se o número é positivo
if numero > 0:
    dobro = numero * 2
    print(f"O dobro do valor digitado é: {dobro}")
elif numero < 0:
    print("O número é inválido.")
else:
    # Caso o usuário digite 0 (que não é estritamente positivo nem negativo)
    print("O número 0 é neutro (nem positivo, nem negativo).")

Digite um número: 28
O dobro do valor digitado é: 56.0

7:Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes formulas (onde  h corresponde a altura): 
Homens: (72.7 ∗ h) − 58
Mulheres: (62, 1 ∗ h) − 44, 7

# Recebe a altura (convertida para número decimal)
altura = float(input("Digite a altura em metros (ex: 1.75): "))

# Recebe o sexo do usuário e padroniza para maiúsculo
sexo = input("Digite o sexo (M para Masculino, F para Feminino): ").strip().upper()

# Verifica o sexo e aplica a fórmula correspondente
if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f"O peso ideal para um homem de {altura:.2f}m é: {peso_ideal:.2f} kg")
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher de {altura:.2f}m é: {peso_ideal:.2f} kg")
else:
    print("Opção de sexo inválida! Use apenas 'M' ou 'F'.")

Digite a altura em metros (ex: 1.75): 1.80
Digite o sexo (M para Masculino, F para Feminino): m
O peso ideal para um homem de 1.80m é: 72.86 kg

8:Peça o valor de uma compra.
Se o valor for maior que R$100, aplique 10% de desconto.
Senão, não aplique desconto.
# Solicita o valor total da compra
valor_compra = float(input("Digite o valor da compra (R$): "))

# Verifica se o valor é maior que R$ 100
if valor_compra > 100:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print(f"Desconto de 10% aplicado (R$ {desconto:.2f}).")
    print(f"Valor final a pagar: R$ {valor_final:.2f}")
else:
    print("Nenhum desconto aplicado.")
    print(f"Valor final a pagar: R$ {valor_compra:.2f}")
