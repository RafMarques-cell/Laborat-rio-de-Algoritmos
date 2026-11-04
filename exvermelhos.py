def menu():
     print("1 - Inserir kg de azeitonas armazenados")
     print("2 - Inserir kg de azeitona foram produzidos")
     print("3 - Inserir kg de azeitona foram perdidos")
     print("4 - Inserir kg de azeitona foram vendidos")
     print("5 - Inserir kg de azeitona foram plantados")
     print("6 - Mostrar valores na ordem inversa")
     print("0 - Sair")
     opcao = int(input("Digite a opção: "))
     return opcao

def inserir_armazena(armazena):
    valor = float(input("Digite um valor armazenado: "))
    armazena.append(valor)
    return armazena


def inserir_produzidos(produzidos):
    valor = float(input("Digite um valor produzido: "))
    produzidos.append(valor)
    return produzidos


def inserir_perdidos(perdidos):
    valor = float(input("Digite um valor perdido: "))
    perdidos.append(valor)
    return perdidos


def inserir_vendidos(vendidos):
    valor = float(input("Digite um valor vendido: "))
    vendidos.append(valor)
    return vendidos


def inserir_plantados(plantados):
    valor = float(input("Digite um valor plantado: "))
    plantados.append(valor)
    return plantados

def mostrar_produzidos(produzidos):
    produzidos.reverse()
    print("Valores produzidos na ordem inversa:")
    print(produzidos)

def main():
    armazena = []
    produzidos = []
    perdidos = []
    vendidos = []
    plantados = []

    opcao = 1

    while opcao != 0:
        opcao = menu()

        if opcao == 1:
            inserir_armazena(armazena)

        elif opcao == 2:
            inserir_produzidos(produzidos)

        elif opcao == 3:
            inserir_perdidos(perdidos)

        elif opcao == 4:
            inserir_vendidos(vendidos)

        elif opcao == 5:
            inserir_plantados(plantados)

        elif opcao == 6:
            print("Armazenados:", armazena[::-1])
            print("Produzidos:", produzidos[::-1])
            print("Perdidos:", perdidos[::-1])
            print("Vendidos:", vendidos[::-1])
            print("Plantados:", plantados[::-1])

        elif opcao == 0:
            print("Programa encerrado!")

        else:
            print("Opção inválida!")

main()
------------------------------------------------------------------------------
def menu():
     print("1 - Inserir quantos kg foram produzidos na fazenda A:")
     print("2 - Inserir quantos kg foram produzidos na fazenda B:")
     print("3 - Mostrar soma da produção")
     opcao = int(input("Digite a opção: "))
     return opcao

def inserir_armazena(armazena):
    valor = float(input("Digite um valor armazenado: "))
    armazena.append(valor)
    return armazena

def inserir_produzidos(produzidos):
    valor = float(input("Digite um valor produzido: "))
    produzidos.append(valor)
    return produzidos

def main():
    armazena = []
    produzidos = []

    opcao = 1

    while opcao != 0:
        opcao = menu()

        if opcao == 1:
            inserir_armazena(armazena)

        elif opcao == 2:
            inserir_produzidos(produzidos)

        elif opcao == 3:
            soma = sum(armazena) + sum(produzidos)
            print("Total produzido nas duas fazendas:", soma)

        elif opcao == 0:
            print("Programa encerrado!")

        else:
            print("Opção inválida!")

main()
------------------------------------------------------------------------
def menu():
    print("1 - Inserir código de lote")
    print("2 - Verificar código de lote")
    print("0 - Sair")

    opcao = int(input("Digite a opção: "))
    return opcao

def inserir_lote(lotes):
    valor = int(input("Digite o código do lote: "))
    lotes.append(valor)
    return lotes

def verificar_lote(lotes):
    codigo = int(input("Digite o código que deseja procurar: "))

    if codigo in lotes:
        print("Código encontrado!")
    else:
        print("Código não encontrado!")

def main():
    lotes = []

    opcao = 1

    while opcao != 0:
        opcao = menu()

        if opcao == 1:
            if len(lotes) < 5:
                inserir_lote(lotes)
            else:
                print("Limite de 5 lotes atingido!")

        elif opcao == 2:
            verificar_lote(lotes)

        elif opcao == 0:
            print("Programa encerrado!")

        else:
            print("Opção inválida!")

main()
------------------------------------------------------------------------
def menu():
    print("1 - Valor por árvore")
    print("2 - Produção por árvore")
    print("3 - Mostrar valor total")
    print("0 - Sair")

    opcao = int(input("Digite a opção: "))
    return opcao

def inserir_valor(valor):
    numero = int(input("Digite o valor por árvore: "))
    valor.append(numero)
    return valor

def inserir_produçao(produçao):
    numero = int(input("Digite o valor por árvore: "))
    produçao.append(numero)
    return produçao

def main():
    valor = []
    produçao = []

    opcao = 1

    while opcao != 0:
        opcao = menu()

        if opcao == 1:
            inserir_valor(valor)

        elif opcao == 2:
            inserir_produçao(produçao)

        elif opcao == 3:
            soma = sum(valor) * sum(produçao)
            print("Total da multiplicação de elemento a elemento:", soma)

        elif opcao == 0:
            print("Programa encerrado!")

        else:
            print("Opção inválida!")

main()
-----------------------------------------------------------------
def menu():
    print("1 - Inserir lote")
    print("2 - Listar lotes")
    print("3 - Retirar um lote")
    print("4 - Limpar todos os lotes")
    print("5 - Contar lotes com produção maior que X")
    print("6 - Verificar se um código está presente")
    print("7 - Encontrar maior e menor código")
    print("0 - Sair")

    opcao = int(input("Digite a opção: "))
    return opcao


def inserir_lote(lotes):
    valor = int(input("Digite o código do lote: "))

    if valor % 2 == 0:
        lotes.append(valor)
        print("Lote inserido com sucesso!")
    else:
        print("Erro! Só são permitidos códigos pares.")

    return lotes


def listar_lotes(lotes):
    print("Lotes cadastrados:", lotes)


def retirar_lote(lotes):
    valor = int(input("Digite o lote que deseja retirar: "))

    if valor in lotes:
        lotes.remove(valor)
        print("Lote retirado!")
    else:
        print("Lote não encontrado!")


def limpar_lotes(lotes):
    lotes.clear()
    print("Todos os lotes foram removidos!")


def contar_lotes(lotes):
    x = int(input("Digite o valor de X: "))
    contador = 0

    for valor in lotes:
        if valor > x:
            contador += 1

    print("Quantidade de lotes maiores que X:", contador)


def verificar_lote(lotes):
    codigo = int(input("Digite o código que deseja procurar: "))

    if codigo in lotes:
        print("Código encontrado!")
    else:
        print("Código não encontrado!")


def maior_menor(lotes):
    if len(lotes) > 0:
        print("Maior código:", max(lotes))
        print("Menor código:", min(lotes))
    else:
        print("Não existem lotes cadastrados!")


def main():
    lotes = []
    opcao = 1

    while opcao != 0:
        opcao = menu()

        if opcao == 1:
            inserir_lote(lotes)

        elif opcao == 2:
            listar_lotes(lotes)

        elif opcao == 3:
            retirar_lote(lotes)

        elif opcao == 4:
            limpar_lotes(lotes)

        elif opcao == 5:
            contar_lotes(lotes)

        elif opcao == 6:
            verificar_lote(lotes)

        elif opcao == 7:
            maior_menor(lotes)

        elif opcao == 0:
            print("Programa encerrado!")

        else:
            print("Opção inválida!")


main()
