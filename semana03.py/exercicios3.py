1.Uma equipe de corrida deseja premiar seus treinadores.
Faça um programa que leia o nome do treinador, seu salário atual e o tempo de serviço na equipe (em anos).
Se o treinador tem 5 anos ou mais de experiência e recebe até R$ 2.000,00, ele terá um aumento de 10%.
Nos demais casos, o aumento será de 5%.
Exiba o nome do treinador, o aumento concedido e o novo salário.

# Entrada de dados
nome = input("Digite o nome do treinador: ")
salario_atual = float(input("Digite o salário atual (R$): "))
tempo_servico = int(input("Digite o tempo de serviço (em anos): "))

# Regra para concessão do aumento
if tempo_servico >= 5 and salario_atual <= 2000.00:
    percentual_aumento = 0.10  # 10% de aumento
else:
    percentual_aumento = 0.05  # 5% de aumento

# Cálculos
valor_aumento = salario_atual * percentual_aumento
novo_salario = salario_atual + valor_aumento

# Exibição dos resultados
print(f"\n--- Resumo do Reajuste ---")
print(f"Treinador: {nome}")
print(f"Aumento concedido: {percentual_aumento * 100:.0f}% (R$ {valor_aumento:.2f})")
print(f"Novo salário: R$ {novo_salario:.2f}")

Digite o nome do treinador: rafael
Digite o salário atual (R$): 2000
Digite o tempo de serviço (em anos): 6

--- Resumo do Reajuste ---
Treinador: rafael
Aumento concedido: 10% (R$ 200.00)
Novo salário: R$ 2200.00
---------------------------------------------------------------------------------------
2.Um engenheiro quer verificar se três forças podem manter um corpo em equilíbrio.
Faça um programa que leia três valores correspondentes às forças.
O sistema deve verificar se elas obedecem à condição de equilíbrio (a soma de duas deve ser maior que a terceira). Todas devem ser verdadeiras, A + B > C AND A + C > B AND B + C > A
Caso positivo, classifique o equilíbrio como:
Simétrico → três forças iguais
Parcialmente simétrico → duas forças iguais
Assimétrico → três forças diferentes
Caso contrário, informe que não há equilíbrio.

# Leitura dos valores das três forças
a = float(input("Digite o valor da primeira força (A): "))
b = float(input("Digite o valor da segunda força (B): "))
c = float(input("Digite o valor da terceira força (C): "))

# Verificação da condição de equilíbrio (Desigualdade Triangular)
if (a + b > c) and (a + c > b) and (b + c > a):
    print("\nO sistema está em EQUILÍBRIO.")
    
    # Classificação do tipo de equilíbrio
    if a == b == c:
        print("Classificação: Simétrico (três forças iguais)")
    elif a == b or a == c or b == c:
        print("Classificação: Parcialmente simétrico (duas forças iguais)")
    else:
        print("Classificação: Assimétrico (três forças diferentes)")

else:
    print("\nNão há equilíbrio (as forças não formam um triângulo fechado).")

Digite o valor da primeira força (A): 4
Digite o valor da segunda força (B): 5
Digite o valor da terceira força (C): 6

O sistema está em EQUILÍBRIO.
Classificação: Assimétrico (três forças diferentes)
--------------------------------------------------------------------------------------------------------
3.Um posto de gasolina deseja calcular descontos para seus clientes:
Se o cliente abastecer 20 litros ou mais e o valor total for maior que R$ 100,00, ele recebe 10% de desconto.
Caso abasteça pelo menos 20 litros mas o valor total seja menor ou igual a R$ 100,00, o desconto é de 5%.
Caso contrário, não há desconto.
O programa deve ler a quantidade de litros e o valor total, e informar o desconto aplicado e o valor final.
# Entrada de dados
litros = float(input("Digite a quantidade de litros abastecidos: "))
valor_total = float(input("Digite o valor total da compra (R$): "))

# Verificação das condições de desconto
if litros >= 20 and valor_total > 100.00:
    percentual_desconto = 0.10  # 10% de desconto
elif litros >= 20 and valor_total <= 100.00:
    percentual_desconto = 0.05  # 5% de desconto
else:
    percentual_desconto = 0.00  # Sem desconto

# Cálculos
valor_desconto = valor_total * percentual_desconto
valor_final = valor_total - valor_desconto

# Exibição dos resultados
print(f"\n--- Resumo do Abastecimento ---")
print(f"Desconto aplicado: {percentual_desconto * 100:.0f}% (R$ {valor_desconto:.2f})")
print(f"Valor final a pagar: R$ {valor_final:.2f}")

Digite a quantidade de litros abastecidos: 100
Digite o valor total da compra (R$): 150

--- Resumo do Abastecimento ---
Desconto aplicado: 10% (R$ 15.00)
Valor final a pagar: R$ 135.00
------------------------------------------------------------------------------------------------------
4.Faça um algoritmo que leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
    Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0                      A
      Entre 7.5 e 9.0                        B
      Entre 6.0 e 7.5                        C
      Entre 4.0 e 6.0                        D
      Entre 4.0 e zero                      E
O algoritmo deve mostrar as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

# Entrada das notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média
media = (nota1 + nota2) / 2

# Determinação do conceito
if 9.0 <= media <= 10.0:
    conceito = 'A'
elif 7.5 <= media < 9.0:
    conceito = 'B'
elif 6.0 <= media < 7.5:
    conceito = 'C'
elif 4.0 <= media < 6.0:
    conceito = 'D'
else:
    conceito = 'E'

# Determinação do status de aprovação
if conceito in ['A', 'B', 'C']:
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

# Exibição dos resultados
print("\n--- Relatório Final ---")
print(f"Nota 1: {nota1:.1f}")
print(f"Nota 2: {nota2:.1f}")
print(f"Média de Aproveitamento: {media:.1f}")
print(f"Conceito: {conceito}")
print(f"Situação: {situacao}")

Digite a primeira nota: 6
Digite a segunda nota: 4

--- Relatório Final ---
Nota 1: 6.0
Nota 2: 4.0
Média de Aproveitamento: 5.0
Conceito: D
Situação: REPROVADO
------------------------------------------------------------------------
5.A cidade está prestes a sediar a Corrida Anual dos Campeões, e os organizadores precisam saber se você está preparado para participar.
Um programa fará 5 perguntas sobre sua preparação:
Você treinou regularmente nas últimas semanas?
Participou de treinos longos (acima de 10 km)?
Seguiu uma dieta especial para a corrida?
Já competiu em provas oficiais neste ano?
Conta com acompanhamento de treinador ou equipe?
De acordo com suas respostas "Sim" ou "Não", o sistema deve classificá-lo:
2 respostas positivas → Você é classificado como Participante Casual (ainda precisa de mais treino).
3 ou 4 respostas positivas → Você é classificado como Atleta Competitivo (tem boas chances de se destacar).
5 respostas positivas → Você é classificado como Atleta de Elite (pronto para o pódio!).
Menos de 2 respostas positivas → Você é classificado como Não Preparado (talvez seja melhor assistir da arquibancada este ano).

print("--- Corrida Anual dos Campeões: Questionário de Preparação ---")
print("Responda com 'S' para Sim ou 'N' para Não.\n")

# Lista de perguntas
perguntas = [
    "Você treinou regularmente nas últimas semanas? ",
    "Participou de treinos longos (acima de 10 km)? ",
    "Seguiu uma dieta especial para a corrida? ",
    "Já competiu em provas oficiais neste ano? ",
    "Conta com acompanhamento de treinador ou equipe? "
]

respostas_positivas = 0

# Coleta de respostas
for pergunta in perguntas:
    resposta = input(pergunta).strip().upper()
    if resposta == 'S' or resposta == 'SIM':
        respostas_positivas += 1

# Classificação
print("\n--- Resultado da Avaliação ---")
print(f"Respostas positivas: {respostas_positivas}")

if respostas_positivas == 5:
    print("Classificação: Atleta de Elite (pronto para o pódio!)")
elif 3 <= respostas_positivas <= 4:
    print("Classificação: Atleta Competitivo (tem boas chances de se destacar)")
elif respostas_positivas == 2:
    print("Classificação: Participante Casual (ainda precisa de mais treino)")
else:
    print("Classificação: Não Preparado (talvez seja melhor assistir da arquibancada este ano)")

--- Corrida Anual dos Campeões: Questionário de Preparação ---
Responda com 'S' para Sim ou 'N' para Não.

Você treinou regularmente nas últimas semanas? n
Participou de treinos longos (acima de 10 km)? n
Seguiu uma dieta especial para a corrida? n
Já competiu em provas oficiais neste ano? n
Conta com acompanhamento de treinador ou equipe? n

--- Resultado da Avaliação ---
Respostas positivas: 0
Classificação: Não Preparado (talvez seja melhor assistir da arquibancada este ano)
-----------------------------------------------------------------------------------
6.Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                              Até 5 Kg                 Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã              R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

# Entrada de dados: quantidade em Kg de cada fruta
kg_morangos = float(input("Digite a quantidade de morangos (Kg): "))
kg_macas = float(input("Digite a quantidade de maçãs (Kg): "))

# Cálculo do preço dos morangos
if kg_morangos <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

# Cálculo do preço das maçãs
if kg_macas <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

# Totais parciais e totais gerais sem desconto
total_morango = kg_morangos * preco_morango
total_maca = kg_macas * preco_maca

total_kg = kg_morangos + kg_macas
valor_total = total_morango + total_maca

# Aplicação do desconto de 10% (se peso > 8kg OU valor > R$ 25,00)
if total_kg > 8 or valor_total > 25.00:
    valor_total *= 0.90  # Aplica 10% de desconto

# Exibição do resultado final
print(f"\nTotal de frutas: {total_kg:.2f} Kg")
print(f"Valor a ser pago pelo cliente: R$ {valor_total:.2f}")

Digite a quantidade de morangos (Kg): 2
Digite a quantidade de maçãs (Kg): 3

Total de frutas: 5.00 Kg
Valor a ser pago pelo cliente: R$ 10.40
