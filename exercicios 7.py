1:ingressos = 100

while True:
    print("\n===== CONTROLE DE INGRESSOS =====")
    print("1 - Vender ingresso")
    print("2 - Adicionar ingressos extras")
    print("3 - Mostrar ingressos disponíveis")
    print("4 - Encerrar")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        quantidade = int(input("Quantidade de ingressos para vender: "))

        if quantidade <= 0:
            print("Quantidade inválida!")
        elif quantidade <= ingressos:
            ingressos -= quantidade
            print("Venda realizada com sucesso!")
            print(f"Ingressos disponíveis: {ingressos}")
        else:
            print("Não há ingressos suficientes!")

    elif opcao == 2:
        quantidade = int(input("Quantidade de ingressos extras: "))

        if quantidade <= 0:
            print("Quantidade inválida!")
        else:
            ingressos += quantidade
            print("Ingressos extras adicionados!")
            print(f"Ingressos disponíveis: {ingressos}")

    elif opcao == 3:
        print(f"Ingressos disponíveis: {ingressos}")

    elif opcao == 4:
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")

  ---------------------------------------
2:ontador = 0

while True:
    codigo = int(input("Digite o código do brinquedo (0 para encerrar): "))

    if codigo == 0:
        break

    if codigo == 1040:
        contador += 1

print(f"O código 1040 foi digitado {contador} vezes.")

---------------------------------------
3:oma = 0
menos_30 = 0
entre_30_60 = 0

for i in range(7):
    tempo = float(input(f"Digite o tempo do corredor {i + 1} (em minutos): "))

    soma += tempo

    if tempo < 30:
        menos_30 += 1
    elif tempo >= 30 and tempo <= 60:
        entre_30_60 += 1

media = soma / 7
porcentagem = (entre_30_60 / 7) * 100

print("\n===== RESULTADO =====")
print(f"Tempo médio: {media:.2f} minutos")
print(f"Corredores que terminaram em menos de 30 minutos: {menos_30}")
print(f"Porcentagem entre 30 e 60 minutos: {porcentagem:.2f}%")

------------------------------------
4:soma_salarios = 0
mais_novo = None
mais_velho = None

atacantes = 0
defensores = 0
atacantes_ate_10000 = 0

for i in range(10):
    print(f"\nJogador {i + 1}")

    idade = int(input("Idade: "))
    posicao = input("Posição (A - Atacante / D - Defensor): ").upper()
    salario = float(input("Salário: R$ "))

    # Soma dos salários
    soma_salarios += salario

    # Conta atacantes e defensores
    if posicao == "A":
        atacantes += 1

        if salario <= 10000:
            atacantes_ate_10000 += 1

    elif posicao == "D":
        defensores += 1

    # Verifica jogador mais novo
    if mais_novo is None or idade < mais_novo:
        mais_novo = idade

    # Verifica jogador mais velho
    if mais_velho is None or idade > mais_velho:
        mais_velho = idade


# Calcula a média dos salários
media_salarios = soma_salarios / 10

print("\n===== RESULTADOS =====")
print(f"Média dos salários: R$ {media_salarios:.2f}")
print(f"Jogador mais novo: {mais_novo} anos")
print(f"Jogador mais velho: {mais_velho} anos")
print(f"Atacantes com salário até R$ 10.000,00: {atacantes_ate_10000}")
print(f"Quantidade de atacantes: {atacantes}")

-----------------------------------------
5:aiores_de_idade = 0

for i in range(10):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))

    if idade >= 18:
        maiores_de_idade += 1

print(f"\nQuantidade de pessoas com 18 anos ou mais: {maiores_de_idade}")

----------------------------------------
6:contador = 0

for i in range(10):
    temperatura = float(input(f"Digite a temperatura da cidade {i + 1}: "))

    if temperatura >= 15 and temperatura <= 25:
        contador += 1

print(f"\nQuantidade de cidades entre 15 °C e 25 °C: {contador}")

----------------------------------------------
7:expresso = 0
cappuccino = 0
cha = 0

for i in range(10):
    print("\nA - Café Expresso")
    print("B - Cappuccino")
    print("C - Chá")

    voto = input(f"Cliente {i + 1}, escolha sua bebida: ").upper()

    if voto == "A":
        expresso += 1
    elif voto == "B":
        cappuccino += 1
    elif voto == "C":
        cha += 1
    else:
        print("Opção inválida!")

# Calcula as porcentagens
porcentagem_expresso = (expresso / 10) * 100
porcentagem_cappuccino = (cappuccino / 10) * 100
porcentagem_cha = (cha / 10) * 100

print("\n===== RESULTADO =====")
print(f"Café Expresso: {expresso} votos - {porcentagem_expresso:.2f}%")
print(f"Cappuccino: {cappuccino} votos - {porcentagem_cappuccino:.2f}%")
print(f"Chá: {cha} votos - {porcentagem_cha:.2f}%")

-----------------------------------------------
8:# Solicita o dinheiro inicial em caixa
caixa = float(input("Digite o dinheiro atual em caixa: R$ "))

while True:
    print("\n===== CONTROLE DO CAIXA =====")
    print("1 - Realizar vendas")
    print("2 - Retirar dinheiro")
    print("3 - Dinheiro em caixa")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        valor = float(input("Digite o valor da venda: R$ "))

        if valor > 0:
            caixa += valor
            print("Venda realizada com sucesso!")
        else:
            print("Valor inválido!")

    elif opcao == 2:
        valor = float(input("Digite o valor a retirar: R$ "))

        if valor <= 0:
            print("Valor inválido!")
        elif valor <= caixa:
            caixa -= valor
            print("Retirada realizada com sucesso!")
        else:
            print("Não há dinheiro suficiente em caixa!")

    elif opcao == 3:
        print(f"Dinheiro disponível em caixa: R$ {caixa:.2f}")

    elif opcao == 4:
        print("Caixa encerrado!")
        break

    else:
        print("Opção inválida!")
