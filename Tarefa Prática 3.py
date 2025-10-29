# Atividade Prática 3
# Atividade 1: Área da Circunferência

print("~~~~~~~~~~~~~~~~~~~~")
π = 3.14159265 # define o valor de pi
raio = float(input("Digite o valor do raio: ")) # lê o raio como número decimal
area = π * (raio ** 2) # calcula a área da circunferência (π * r²)
print("A =", round(area, 4)) # imprime o resultado arredondado a 4 casas decimais
print("~~~~~~~~~~~~~~~~~~~~")

# Atividade 2: Classificação de Idade

crianca = 0 - 12
adolescente = 13 - 17
adulto = 18 - 59
idoso = 60

idade = int(input("Digite a idade: ")) # lê a idade como número inteiro

if idade <= 12:
    print("Classificação: Criança")
elif 13 <= idade <= 17:
    print("Classificação: Adolescente")
elif 18 <= idade <= 59:
    print("Classificação: Adulto")
else:
    print("Classificação: Idoso")
print("~~~~~~~~~~~~~~~~~~~~")

# Atividade 3: Calculadora de IMC

peso = float(input("Digite o peso em kg: ")) # lê o peso como número decimal
altura = float(input("Digite a altura em metros: ")) # lê a altura como número decimal

imc = peso / (altura ** 2) # calcula o IMC

print("IMC =", round(imc, 2)) # imprime o resultado com 2 casas decimais
print("~~~~~~~~~~~~~~~~~~~~")

# Atividade 4: Conversor de Temperatura

celsius = float(input("Digite a temperatura em Celsius: ")) # lê a temperatura em Celsius
fahrenheit = (celsius * 9/5) + 32 # converte para Fahrenheit
kelvin = celsius + 273.15 # converte para Kelvin

print("Fahrenheit =", round(fahrenheit, 2)) # imprime Fahrenheit
print("Kelvin =", round(kelvin, 2)) # imprime Kelvin
print("~~~~~~~~~~~~~~~~~~~~")

# Atividade 5: Verificador de Ano Bissexto

ano = int(input("Digite o ano: ")) # lê o ano como número inteiro
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")
print("~~~~~~~~~~~~~~~~~~~~")

# Atividade 6: Calculadora de Comissão de Vendas

nome_vendedor = input("Digite o nome do vendedor: ") # lê o nome do vendedor
salario_fixo = float(input("Digite o salário fixo: ")) # lê o salário
total_vendas = float(input("Digite o total de vendas: ")) # lê o total de vendas
comissao = 0.15 * total_vendas # calcula a comissão (15% das vendas)
salario_total = salario_fixo + comissao # calcula o salário total

print("Salário total de", nome_vendedor, "é: R$", round(salario_total, 2)) # imprime o salário total
print("~~~~~~~~~~~~~~~~~~~~")

# Atividade 7: Calculadora da Média

n1, n2, n3, n4 = map(float, input("Digite quatro números separados por espaço: ").split()) # lê quatro números
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10 # calcula a média
print("Média =", round(media, 1)) # imprime a média com 1 casa decimal

if media >= 7.0:
    print("Aluno aprovado.")
elif 5.0 <= media < 7.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input("Digite a nota do exame: ")) # lê a nota do exame
    print("Nota do exame =", round(exame, 1)) # imprime a nota do exame

    media_final = (media + exame) / 2 # calcula a média final

    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print("Média final =", round(media_final, 1)) # imprime a média final
print("~~~~~~~~~~~~~~~~~~~~")