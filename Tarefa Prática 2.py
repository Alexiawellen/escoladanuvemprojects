# Atividade Prática 2
# Ativicade 1: Conversor de Moeda

print("~~~~~~~~~~~~~~~~~~~~")
valor_em_reais = 100.00
taxa_dólar = 5.60
taxa_euro = 6.60

valor_em_dolares = valor_em_reais / taxa_dólar
valor_em_euros = valor_em_reais / taxa_euro
print("O valor em dólares é: $", round(valor_em_dolares, 2))
print("O valor em euros é: €", round(valor_em_euros, 2))
print("~~~~~~~~~~~~~~~~~~~~")

# Atividade 2: Calculadora de Descontos

Nome_produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

desconto = (percentual_desconto / 100) * preco_original
preco_com_desconto = preco_original - desconto
print("O preço com desconto é: R$", round(preco_com_desconto, 2))
print("~~~~~~~~~~~~~~~~~~~~")

# Atividade 3: Calculadora de Média Escolar

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3
print("A média escolar é:", round(media, 2))
print("~~~~~~~~~~~~~~~~~~~~")

# Atividade 4: Calculadora de Consumo de Combustível

distancia_percorrida = 300  # em km
combustivel_gasto = 25  # em litros

consumo_medio = distancia_percorrida / combustivel_gasto
print("O consumo médio de combustível é:", round(consumo_medio, 2), "km/l")
print("~~~~~~~~~~~~~~~~~~~~")

# Atividade 5: Calculadora de Soma com Entrada do Usuário

A = int(input("Digite o primeiro valor (A): "))
B = int(input("Digite o segundo valor (B): "))

soma = A + B

print(f"X = {soma}")
print("~~~~~~~~~~~~~~~~~~~~")

# Atividade 6: Calculadora de Salário por Horas Trabalhadas

numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor por hora trabalhada: "))

salario = horas_trabalhadas * valor_hora
print(f"FUNCIONÁRIO = {numero_funcionario}")
print(f"SALÁRIO = R$ {round(salario, 2)}")
print("~~~~~~~~~~~~~~~~~~~~")