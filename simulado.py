1:numero = int(input("Digite um número inteiro positivo: "))

while numero < 0:
    print("Valor inválido! Digite um número positivo.")
    numero = int(input("Digite um número inteiro positivo: "))

while numero >= 0:
    print(numero)
    numero -= 1

--------------------------------
2:elevador_a = 0
elevador_b = 0
elevador_c = 0

for i in range(10):
    elevador = input(f"Morador {i + 1}, qual elevador você utiliza? (A, B ou C): ").upper()

    while elevador not in ["A", "B", "C"]:
        print("Opção inválida! Digite A, B ou C.")
        elevador = input("Digite novamente: ").upper()

    if elevador == "A":
        elevador_a += 1
    elif elevador == "B":
        elevador_b += 1
    else:
        elevador_c += 1

# Calcula as porcentagens
porcentagem_a = (elevador_a / 10) * 100
porcentagem_b = (elevador_b / 10) * 100
porcentagem_c = (elevador_c / 10) * 100

print("\n===== RESULTADO =====")
print(f"Elevador A: {elevador_a} pessoas - {porcentagem_a:.2f}%")
print(f"Elevador B: {elevador_b} pessoas - {porcentagem_b:.2f}%")
print(f"Elevador C: {elevador_c} pessoas - {porcentagem_c:.2f}%")

-----------------------------------
3:# Preços dos combustíveis
preco_gasolina = 6.89
preco_diesel = 4.80

# Totais vendidos em litros
total_gasolina = 0
total_diesel = 0

while True:
    print("\n===== POSTO DE GASOLINA =====")
    print("1 - Vender combustível")
    print("2 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        print("\n===== COMBUSTÍVEL =====")
        print("1 - Gasolina (R$ 6,89)")
        print("2 - Diesel    (R$ 4,80)")

        combustivel = int(input("Escolha o combustível: "))

        if combustivel == 1:
            preco = preco_gasolina
            nome = "Gasolina"

        elif combustivel == 2:
            preco = preco_diesel
            nome = "Diesel"

        else:
            print("Erro! Opção de combustível inválida.")
            continue

        litros = float(input("Digite a quantidade de litros abastecidos: "))
        valor_pago = float(input("Digite o valor pago: R$ "))

        # Calcula o valor do abastecimento
        valor_abastecimento = litros * preco

        print("\n===== ABASTECIMENTO =====")
        print(f"Combustível: {nome}")
        print(f"Litros abastecidos: {litros:.2f} L")
        print(f"Valor total: R$ {valor_abastecimento:.2f}")

        # Verifica pagamento
        if valor_pago >= valor_abastecimento:
            troco = valor_pago - valor_abastecimento
            print(f"Troco: R$ {troco:.2f}")

        else:
            faltou = valor_abastecimento - valor_pago
            print(f"Valor que faltou: R$ {faltou:.2f}")

        # Atualiza o total vendido
        if combustivel == 1:
            total_gasolina += litros
        else:
            total_diesel += litros

    elif opcao == 2:
        print("\n===== TOTAL DE VENDAS =====")
        print(f"Total de gasolina vendido: {total_gasolina:.2f} litros")
        print(f"Total de diesel vendido: {total_diesel:.2f} litros")
        print("Programa encerrado!")
        break

    else:
        print("Erro! Opção inválida.")

  --------------------------------------
4:n1 = 3
n2 = 11
n = n1 - 2

Então:

n = 3 - 2
n = 1

Agora entra no while:

while n < n2:   # 1 < 11 → verdadeiro

Dentro do while:

n = n % 12

Como 1 % 12 = 1:

n = 1

Depois:

n = n + 2

Logo:

n = 3

Verificamos:

if n % 5 == 2:

3 % 5 = 3, então não entra no break.

O while continua:

n = 3 % 12 = 3
n = 3 + 2 = 5
5 % 5 = 0 → não quebra

Novamente:

n = 5 % 12 = 5
n = 5 + 2 = 7
7 % 5 = 2 → break

Portanto, o while é interrompido quando n vale 7.
Saída:

7
