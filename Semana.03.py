Operador: ==; !=; >; <; >=; <=
Função: Iguladade;Diferente;Maior;Menor;Maior ou igual que; menor ou igual que

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Pode Dirigir")
else:
    print("Não pode dirigir")

    print("Depois do IF")

valor = float(input("Digite uma valor:"))

#> 1000: 5% de juros e 2x
#<= 1000: 2% de desconto a vista

#if valor <= 1000:
if valor > 1000:
    novo_valor + valor * 1.05
    parcela = novo_valor / 2
    print("Novo valor: ", novo_valor)
    print("Valor de parcelas: ", parcela)
else:
    novo_valor = valor * 0.98
    print("Valor a vista:", novo_valor)

