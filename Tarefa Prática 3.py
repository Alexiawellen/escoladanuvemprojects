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

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"
    
print("IMC: {:.2f}".format(imc))
print("Classificação: {}".format(classificacao))
print("~~~~~~~~~~~~~~~~~~~~")

# Atividade 4: Conversor de Temperatura

# Conversão Celsius
def celsius_to_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    return print(round(fahrenheit, 1))

def celsius_to_kelvin(c):
    kelvin = c + 273.15
    return print(round(kelvin, 2))

# Conversão Fahrenheit
def fahrenheit_to_celsius(f):
    celsius = (f - 32) * 5/9
    return print(round(celsius, 2))

def fahrenheit_to_kelvin(f):
    kelvin = ((f - 32) * 5/9) + 273.15
    return print(round(kelvin, 2))

# Conversão Kelvin
def kelvin_to_celsius(k):
    celsius = k - 273.15
    return print(round(celsius, 2))

def kelvin_to_fahrenheit(k):
    fahrenheit = ((k - 273.15) * 9/5) + 32
    return print(round(fahrenheit, 2))


# Programa principal
temperatura = float(input("Informe a temperatura: "))
unidade_origem = input("Informe a origem: Celsius(1), Fahrenheit(2), Kelvin(3): ")
unidade_destino = input("Informe o destino: Celsius(1), Fahrenheit(2), Kelvin(3): ")
valores_validos = ["1", "2", "3"]

if unidade_origem not in valores_validos or unidade_destino not in valores_validos:
    print("Unidade inválida. Use 1, 2 ou 3")

elif unidade_origem == unidade_destino:
    print("As unidades são iguais. Nenhuma conversão necessária.")

# Celsius
elif unidade_origem == "1":
    if unidade_destino == "2":
        celsius_to_fahrenheit(temperatura)
    elif unidade_destino == "3":
        celsius_to_kelvin(temperatura)

# Fahrenheit
elif unidade_origem == "2":
    if unidade_destino == "1":
        fahrenheit_to_celsius(temperatura)
    elif unidade_destino == "3":
        fahrenheit_to_kelvin(temperatura)

# Kelvin
elif unidade_origem == "3":
    if unidade_destino == "1":
        kelvin_to_celsius(temperatura)
    elif unidade_destino == "2":
        kelvin_to_fahrenheit(temperatura)
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