#Faça um algoritmo para calcular a média entre duas notas de um aluno. O algoritmo deve conter:
#Uma função que recebe dois valores e retorna a média
#E uma função que recebe a média e apresente se o aluno foi ou não aprovado.


def pedir_notas():
        n1 = float(input("Digite a primeira nota:"))
        n2 = float(input("Digite a segunda nota:"))
        return n1, n2

def calcular_media(n1, n2):
    valor = (n1 + n2) / 2
    return valor
   
def main():
    nota1, nota2 = pedir_notas()
    resultado = calcular_media(nota1, nota2)
    print(f"Resultado da média: {resultado:.2f}" )
    if resultado <= 5:
        print("Atenção: Média abaixo ou igual a 5. Aluno em recuperação/reprovado.")
    else:
        print("Parabéns! Média acima de 5.")


main()



