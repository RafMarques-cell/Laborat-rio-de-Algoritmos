
def ola():
    valor = 5
    print("Valor:", valor)
    print("Olá dentro da função")


def media(numero1, numero2):
    media = (numero1 + numero2) / 2
    print("Média:", media)


def calcular_media(numero1, numero2):
  media = (numero1 + numero2)
  return media




def main ():
    n1 = 5
    n2 = 9
    print ("Dentro do main")
    media_notas = calcular_media(n1,n2)
    print("Dentro do main")

main()
main()

------------------------------------------------------------------
def menu():
        print("1 - Sacar")
        print("2 - Depositar")
        print("3 - Saldo")
        print("4 - Sair")
        opc = int(input("Digite a opção:"))
        return opc

def mostrar_saldo(saldo):
      print("Saldo atual: ", valor)
def sacar(saldo):
     valor = float(input("Digite o valor para sacar:"))
     if valor <= saldo:
           saldo = saldo - valor
           mostrar_saldo(saldo)
     else:
           print("Saldo imsuficiente")
           mostrar_saldo(saldo)
     return saldo    

def depositar(saldo):
      valor = float(input("Digite o valor para depositar:"))
      saldo = saldo + valor
      mostrar_saldo(saldo)
      return saldo
    
    
def main():
      saldo = 0
      opcao = 0


      while opcao != 4:
          opcao = menu()
          if opcao == 1:
                saldo = sacar(saldo)
          elif opcao == 2:
              saldo = depositar(saldo)
          elif opcao == 3:
                mostrar_saldo(saldo)


main()
