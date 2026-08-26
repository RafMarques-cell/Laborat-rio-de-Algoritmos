velocidade = float(input("Digite a velocidade:"))

#if 80 >= velocidade <100:
if velocidade >= 80 and velocidade <100:
    print("Multa média - valor de R$138,93")
elif velocidade >=100 and velocidade <120:
    print("Multa grave - Valor de R$568,34")
elif velocidade >=120:
     print("Multa gravissima - valor de R$1200,00")
else:
    print("Velocidade correta")

-----------------------------------------------------------

letra = input("Digite uma letra: "). upper()

if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "u":
    print("VOGAL")
else:
    print("COSOANTE")

-------------------------------------------------------------


idade = int(input("Digite sua idade: "))

if idade >= 18 and idade < 70:
    print("Obrigado a votar")
elif (idade >= 16 and idade < 18) or (idade >= 70):


idade = int(input("Digite sua idade: "))

if idade >= 18 and idade < 70:
    print("Obrigado a votar")
elif idade >= 16:


idade = int(input("Digite sua idade: "))

if idade >= 18 and idade < 70:
    print("Obrigado a votar")
elif idade >= 16:
    print("Voto facultativo")
else:
    print("Você não pode votar!")

