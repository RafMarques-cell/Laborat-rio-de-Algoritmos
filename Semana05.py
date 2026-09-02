valor = 0
print("- ", valor)
valor = valor + 1 # valor += 1
print("- ", valor)
valor = valor + 1 # valor += 1
print("- ", valor)
print = valor + 1 # valor += 1
------------------------------------------------
valor = 10
while valor > 5:
    print("- ", valor)
    valor = valor + 1 # valor +=1
print ("FORA DO WHILE:", valor)

----------------------------------------------
operador = int(input("Qual tabuada:"))
multiplicador = 1

while multiplicador <=  10:
    resultado = operador * multiplicador
    print(operador, "x", multiplicador, "=", resultado)
    multiplicador += 1

--------------------------------------------------
opcao = 0
saldo = float(input("Digite o saldo inicial:"))
while saldo < 0:
    print("Saldo inválida")
    saldo = float(input("Digite o saldo inicial:"))

while opcao != 4:
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Saldo")
    print("4 - Sair")
    try:
       opcao = int(input("Digite uma opção:"))
    except:
        print("Digite um valor inteiro")

    if opcao == 1:
        valor = float(input("Digite o valor para sacar:"))
        if valor <= saldo:
            saldo -= valor
            print("Novo saldo: ",saldo)
        else:
            print("Saldo Insuficiente")

    elif opcao == 2:
        valor = float(input("Digite o valor para depositar:"))
        saldo += valor
    elif opcao == 3:
        print("Saldo atual: ", saldo)
    else:
        print("Opção inválida")

  ---------------------------------------------------------------

valor = 456948

if valor % 2 == 0:
    print("É divisivel")
elif valor % 2 != 0:
    print("Não é divisivel")
