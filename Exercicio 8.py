1:total = 0
maior_producao = 0
menor_producao = 0
dia_maior = 0
dia_menor = 0

for dia in range(1, 8):
    producao = float(input(f"Digite a produção do dia {dia} (em kg): "))

    total += producao

    # Primeiro dia
    if dia == 1:
        maior_producao = producao
        menor_producao = producao
        dia_maior = dia
        dia_menor = dia

    # Verifica maior produção
    if producao > maior_producao:
        maior_producao = producao
        dia_maior = dia

    # Verifica menor produção
    if producao < menor_producao:
        menor_producao = producao
        dia_menor = dia

media = total / 7

print("\n===== RESULTADO DA SEMANA =====")
print(f"Quantidade total produzida: {total:.2f} kg")
print(f"Dia de maior produção: Dia {dia_maior} ({maior_producao:.2f} kg)")
print(f"Dia de menor produção: Dia {dia_menor} ({menor_producao:.2f} kg)")
print(f"Média diária de produção: {media:.2f} kg")

----------------------------------
2:gua = 1800  # 1,8 litro = 1800 ml
cuias = 0

while agua >= 45:
    agua -= 45
    cuias += 1

print(f"Quantidade de cuias completas servidas: {cuias}")
print(f"Água restante: {agua} ml")

------------------------------------
3:pacotes = int(input("Digite a quantidade total de pacotes: "))
caixas = int(input("Digite a quantidade de caixas disponíveis: "))

if caixas > 0:
    pacotes_por_caixa = pacotes // caixas
    sobras = pacotes % caixas

    print("\n===== RESULTADO =====")
    print(f"Pacotes em cada caixa: {pacotes_por_caixa}")
    print(f"Pacotes que irão sobrar: {sobras}")
else:
    print("A quantidade de caixas deve ser maior que zero!")

------------------------------------
4:chimarraos_por_dia = int(input("Quantos chimarrões você prepara por dia? "))

consumo_diario = chimarraos_por_dia * 40
consumo_mensal = consumo_diario * 30

print(f"\nConsumo diário: {consumo_diario} gramas")
print(f"Consumo mensal: {consumo_mensal} gramas")
print(f"Consumo mensal: {consumo_mensal / 1000:.2f} kg")

if consumo_mensal > 3000:
    print("Grande consumidor de erva-mate")
else:
    print("Consumidor moderado de erva-mate")

--------------------------------------
5:folhas = float(input("Digite a quantidade de folhas colhidas (em kg): "))

produto_final = folhas / 3

print(f"\nQuantidade de erva-mate pronta: {produto_final:.2f} kg")

-------------------------------------------
6:preco = 18.90

print("Ervateira Recanto - Tabela de Preços")
print("--------------------------------------")

for quantidade in range(1, 31):
    total = quantidade * preco
    print(f"{quantidade:2d} pacote(s) - R$ {total:.2f}")

------------------------------------------------
7:soma = 0
maior = 0
menor = 0
todos_os_dias = 0

for i in range(20):
    vezes = int(input(f"Quantas vezes por semana a pessoa {i + 1} toma chimarrão? "))

    soma += vezes

    # Define o primeiro valor como maior e menor inicialmente
    if i == 0:
        maior = vezes
        menor = vezes
    else:
        if vezes > maior:
            maior = vezes

        if vezes < menor:
            menor = vezes

    # Conta quem toma 7 vezes ou mais por semana
    if vezes >= 7:
        todos_os_dias += 1

media = soma / 20

print("\n===== RESULTADO =====")
print(f"Média de vezes por semana: {media:.2f}")
print(f"Maior quantidade: {maior}")
print(f"Menor quantidade: {menor}")
print(f"Pessoas que tomam chimarrão todos os dias: {todos_os_dias}")

--------------------------------------
8:producao_a = 5000
producao_b = 8000
meses = 0

while producao_a < producao_b:
    producao_a = producao_a * 1.05
    producao_b = producao_b * 1.01
    meses += 1

print("===== RESULTADO =====")
print(f"Meses necessários: {meses}")
print(f"Produção da primeira empresa: {producao_a:.2f} pacotes")
print(f"Produção da concorrente: {producao_b:.2f} pacotes")

--------------------------------------------
9:numero_secreto = 57
tentativas = 0

while True:
    numero = int(input("Tente descobrir o número secreto (1 a 100): "))
    tentativas += 1

    if numero < numero_secreto:
        print("Tente um número maior!")

    elif numero > numero_secreto:
        print("Tente um número menor!")

    else:
        print("Parabéns! Você encontrou a embalagem premiada!")
        break

print(f"Você precisou de {tentativas} tentativa(s).")

----------------------------------------------
10:preco_pacote = 20.00

quantidade = int(input("Digite a quantidade de pacotes: "))

# Calcula o valor original
valor_original = quantidade * preco_pacote

# Define o percentual de desconto
if quantidade <= 5:
    desconto_percentual = 0
elif quantidade <= 10:
    desconto_percentual = 5
elif quantidade <= 20:
    desconto_percentual = 10
else:
    desconto_percentual = 15

# Calcula o desconto e o valor final
valor_desconto = valor_original * (desconto_percentual / 100)
valor_final = valor_original - valor_desconto

print("\n===== RESUMO DA COMPRA =====")
print(f"Quantidade de pacotes: {quantidade}")
print(f"Valor original: R$ {valor_original:.2f}")
print(f"Desconto: {desconto_percentual}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
