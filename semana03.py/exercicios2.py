1:Faça um algoritmo que leia a pontuação de dois times em uma partida. Mostre qual time venceu, qual perdeu ou se houve empate.

# Solicita o nome ou identificação dos times
time1 = input("Digite o nome do primeiro time: ")
pontos1 = int(input(f"Digite a pontuação do {time1}: "))

time2 = input("Digite o nome do segundo time: ")
pontos2 = int(input(f"Digite a pontuação do {time2}: "))

print("\n--- Resultado da Partida ---")

# Compara as pontuações para determinar o resultado
if pontos1 > pontos2:
    print(f"Vencedor: {time1} ({pontos1} pontos)")
    print(f"Perdedor: {time2} ({pontos2} pontos)")
elif pontos2 > pontos1:
    print(f"Vencedor: {time2} ({pontos2} pontos)")
    print(f"Perdedor: {time1} ({pontos1} pontos)")
else:
    print(f"Empate! Ambos os times marcaram {pontos1} ponto(s).")

Digite a pontuação do Águias: 47
Digite o nome do segundo time: Indios
Digite a pontuação do Indios: 78

--- Resultado da Partida ---
Vencedor: Indios (78 pontos)
Perdedor: Águias (47 pontos)

2:Uma organização de corrida de rua está oferecendo inscrições para a prova de 10 km com três opções de pagamento:
À vista.
Em 2 vezes.
Em 3 vezes.

# Solicita o valor base da inscrição
valor_inscricao = float(input("Digite o valor da inscrição (R$): "))

print("\nOpções de Pagamento:")
print("1 - À vista")
print("2 - Em 2x")
print("3 - Em 3x")

opcao = int(input("\nEscolha a opção desejada (1, 2 ou 3): "))

print("\n--- Resumo da Inscrição ---")

if opcao == 1:
    print(f"Forma de pagamento: À vista")
    print(f"Valor total: R$ {valor_inscricao:.2f}")

elif opcao == 2:
    parcela = valor_inscricao / 2
    print(f"Forma de pagamento: Em 2x sem juros")
    print(f"2 parcelas de: R$ {parcela:.2f}")
    print(f"Valor total: R$ {valor_inscricao:.2f}")

elif opcao == 3:
    parcela = valor_inscricao / 3
    print(f"Forma de pagamento: Em 3x sem juros")
    print(f"3 parcelas de: R$ {parcela:.2f}")
    print(f"Valor total: R$ {valor_inscricao:.2f}")

else:
    print("Opção inválida! Escolha entre 1, 2 ou 3.")

Digite o valor da inscrição (R$): 85

Opções de Pagamento:
1 - À vista
2 - Em 2x
3 - Em 3x

Escolha a opção desejada (1, 2 ou 3): 2

--- Resumo da Inscrição ---
Forma de pagamento: Em 2x sem juros
2 parcelas de: R$ 42.50
Valor total: R$ 85.00

3:O sistema deve ler o valor da inscrição, a opção de
pagamento escolhida pelo atleta e apresentar o 
valor de cada parcela (quando houver).

# Entrada do valor da inscrição
valor_inscricao = float(input("Digite o valor da inscrição (R$): "))

# Exibição do menu de opções
print("\nOpções de Pagamento:")
print("1 - À vista")
print("2 - Em 2 vezes")
print("3 - Em 3 vezes")

opcao = int(input("Escolha a opção de pagamento (1, 2 ou 3): "))

print("\n--- Resumo do Pagamento ---")

# Lógica das condições de pagamento
if opcao == 1:
    print(f"Pagamento à vista em parcela única de R$ {valor_inscricao:.2f}")

elif opcao == 2:
    parcela = valor_inscricao / 2
    print(f"Pagamento em 2x de R$ {parcela:.2f}")
    print(f"Valor total: R$ {valor_inscricao:.2f}")

elif opcao == 3:
    parcela = valor_inscricao / 3
    print(f"Pagamento em 3x de R$ {parcela:.2f}")
    print(f"Valor total: R$ {valor_inscricao:.2f}")

else:
    print("Opção inválida! Escolha 1, 2 ou 3.")

Digite o valor da inscrição (R$): 60

Opções de Pagamento:
1 - À vista
2 - Em 2 vezes
3 - Em 3 vezes
Escolha a opção de pagamento (1, 2 ou 3): 3

--- Resumo do Pagamento ---
Pagamento em 3x de R$ 20.00
Valor total: R$ 60.00

4:Durante uma prova de corrida de rua, os atletas responderam a uma pergunta de conhecimento esportivo.
A questão era: “Qual é a distância oficial de uma maratona?”
Alternativas:
A) 21 km
B) 42,195 km
C) 10 km
D) 5 km

print("--- Pergunta de Conhecimento Esportivo ---")
print("Qual é a distância oficial de uma maratona?\n")
print("A) 21 km")
print("B) 42,195 km")
print("C) 10 km")
print("D) 5 km")

# Recebe a alternativa digitada pelo atleta e padroniza para maiúscula
resposta = input("\nDigite a opção correta (A, B, C ou D): ").strip().upper()

# Verifica a resposta
if resposta == 'B':
    print("\nParabéns! Resposta CORRETA. A distância oficial de uma maratona é 42,195 km.")
elif resposta in ['A', 'C', 'D']:
    print("\nResposta INCORRETA. A alternativa certa é a B) 42,195 km.")
else:
    print("\nOpção inválida! Por favor, escolha entre A, B, C ou D.")

Qual é a distância oficial de uma maratona?

A) 21 km
B) 42,195 km
C) 10 km
D) 5 km

Digite a opção correta (A, B, C ou D): c

Resposta INCORRETA. A alternativa certa é a B) 42,195 km.

5:O sistema deve ler a alternativa assinalada e 
informar se o atleta acertou ou errou.
(Resposta correta: letra B)

# Lê a alternativa escolhida pelo atleta
resposta = input("Digite a alternativa assinalada (A, B, C ou D): ").strip().upper()

# Verifica se a resposta está correta
if resposta == 'B':
    print("Você ACERTOU! A resposta correta é a letra B.")
elif resposta in ['A', 'C', 'D']:
    print("Você ERROU! A resposta correta era a letra B.")
else:
    print("Opção inválida! Digite apenas A, B, C ou D.")

Digite a alternativa assinalada (A, B, C ou D): c
Você ERROU! A resposta correta era a letra B.

6:Um cinema está automatizando a venda de ingressos.
O sistema deve ler o valor base do ingresso e a opção escolhida pelo cliente:
Ingresso normal (valor cheio)
Estudante (50% de desconto)
Criança até 12 anos (paga 40% do valor)
Idoso (paga 60% do valor)

# Exibe a tabela de opções
print("\nSelecione o tipo de ingresso:")
print("1 - Normal (Valor cheio)")
print("2 - Estudante (50% de desconto)")
print("3 - Criança até 12 anos (Paga 40% do valor)")
print("4 - Idoso (Paga 60% do valor)")

opcao = int(input("Digite o número da opção desejada: "))

print("\n--- Resumo do Ingresso ---")

# Processa a opção escolhida
if opcao == 1:
    valor_final = valor_base
    categoria = "Normal"
elif opcao == 2:
    valor_final = valor_base * 0.50  # Desconto de 50%
    categoria = "Estudante"
elif opcao == 3:
    valor_final = valor_base * 0.40  # Paga 40%
    categoria = "Criança até 12 anos"
elif opcao == 4:
    valor_final = valor_base * 0.60  # Paga 60%
    categoria = "Idoso"
else:
    categoria = None
    print("Opção inválida! Escolha um número entre 1 e 4.")

# Exibe o resultado se a opção for válida
if categoria:
    print(f"Tipo selecionado: {categoria}")
    print(f"Valor a pagar: R$ {valor_final:.2f}")

Digite o valor base do ingresso (R$): 75

Selecione o tipo de ingresso:
1 - Normal (Valor cheio)
2 - Estudante (50% de desconto)
3 - Criança até 12 anos (Paga 40% do valor)
4 - Idoso (Paga 60% do valor)
Digite o número da opção desejada: 4

--- Resumo do Ingresso ---
Tipo selecionado: Idoso
Valor a pagar: R$ 45.00

7:Durante a inscrição, o atleta pode escolher entre 3 kits diferentes.
Faça um algoritmo que leia a opção escolhida e o valor que o atleta está entregando em R$ e mostre o que ele receberá:
1 → Kit Básico: Número de peito + medalha - R$100,00
2 → Kit Plus: Número de peito + medalha + camiseta - R$120,00
3 → Kit Premium: Número de peito + medalha + camiseta + squeeze + boné - R$150,00

Ao final apresente se o valor foi suficiente, caso foi suficiente, apresente a categoria do atleta e o troco (se houver), caso contrário apresente uma mensagem informando a falta do valor.

  # Tabela de Opções
print("--- Escolha do Kit do Atleta ---")
print("1 -> Kit Básico: Número de peito + medalha (R$ 100,00)")
print("2 -> Kit Plus: Número de peito + medalha + camiseta (R$ 120,00)")
print("3 -> Kit Premium: Número de peito + medalha + camiseta + squeeze + boné (R$ 150,00)")

# Entradas do usuário
opcao = int(input("\nDigite a opção do kit desejado (1, 2 ou 3): "))
valor_pago = float(input("Digite o valor entregue pelo atleta (R$): "))

# Variáveis para armazenar os detalhes da escolha
preco_kit = 0.0
nome_kit = ""
itens_kit = ""

# Identifica o kit selecionado
if opcao == 1:
    nome_kit = "Kit Básico"
    itens_kit = "Número de peito + medalha"
    preco_kit = 100.00
elif opcao == 2:
    nome_kit = "Kit Plus"
    itens_kit = "Número de peito + medalha + camiseta"
    preco_kit = 120.00
elif opcao == 3:
    nome_kit = "Kit Premium"
    itens_kit = "Número de peito + medalha + camiseta + squeeze + boné"
    preco_kit = 150.00
else:
    print("\nOpção de kit inválida! Por favor, escolha 1, 2 ou 3.")

# Valida o pagamento caso a opção de kit tenha sido válida
if preco_kit > 0:
    print("\n--- Resultado da Inscrição ---")
    
    if valor_pago >= preco_kit:
        troco = valor_pago - preco_kit
        print(f"Pagamento APROVADO!")
        print(f"Categoria do Kit: {nome_kit}")
        print(f"Itens que receberá: {itens_kit}")
        print(f"Valor do Kit: R$ {preco_kit:.2f}")
        print(f"Valor pago: R$ {valor_pago:.2f}")
        print(f"Troco: R$ {troco:.2f}")
    else:
        falta = preco_kit - valor_pago
        print("Pagamento RECUSADO! Valor entregue é insuficiente.")
        print(f"Kit escolhido: {nome_kit} (R$ {preco_kit:.2f})")
        print(f"Valor entregue: R$ {valor_pago:.2f}")
        print(f"Faltam: R$ {falta:.2f} para concluir a inscrição.")

  Digite a opção do kit desejado (1, 2 ou 3): 1
Digite o valor entregue pelo atleta (R$): 120

--- Resultado da Inscrição ---
Pagamento APROVADO!
Categoria do Kit: Kit Básico
Itens que receberá: Número de peito + medalha
Valor do Kit: R$ 100.00
Valor pago: R$ 120.00
Troco: R$ 20.00
