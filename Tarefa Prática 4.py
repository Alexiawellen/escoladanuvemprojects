# Atividade Prática 4
# Atividade 1: Calculadora básico com tratamento de erros
print("~~~~~~~~~~~~~~~~~~~~")

while True:
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        operador = input("Digite o operador (+, -, *, /): ").strip()

        if operador not in ['+', '-', '*', '/']:
            raise ValueError("Operação inválida. Use +, -, *, ou /.")
        
        if operador == '+':
            resultado = n1 + n2
        elif operador == '-':
            resultado = n1 - n2
        elif operador == '*':
            resultado = n1 * n2
        elif operador == '/':
            if n2 == 0:
                raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
            resultado = n1 / n2

        print(f"O resultado de {n1} {operador} {n2} é: {resultado}")
        break # operação concluída com sucesso - encerra o loop

    except ValueError as e:
        print(f"Entrada inválida: {e}. Tente novamente.")
    except ZeroDivisionError as e:
        print(f"Entrada inválida: {e}. Tente novamente.")
print("~~~~~~~~~~~~~~~~~~~~")

# Atividade 2: Registro de notas e cálculo da média
print("~~~~~~~~~~~~~~~~~~~~")
notas = []
print("Digite as notas (0 a 10). Digite 'fim' para encerrar.")

while True:
    entrada = input("Nota: ").strip().lower()
    if entrada == "fim":
        break

    # aceita vírgula ou ponto
    entrada_norm = entrada.replace(",", ".")

    try:
        nota = float(entrada_norm)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Valor fora do intervalo. Use 0 a 10.")
    except ValueError:
        print("Entrada inválida. Digite um número (ex.: 8,5) ou 'fim'.")

if notas:
    media = sum(notas) / len(notas)
    print(f"\nQuantidade de notas: {len(notas)}")
    print(f"Média da turma: {media:.2f}")
else:
    print("\nNenhuma nota válida informada.")
print("~~~~~~~~~~~~~~~~~~~~")

# Atividade 3: Verificador de Senha Forte

# Senha forte: pelo menos 8 caracteres e pelo menos 1 número.
# Continua pedindo até ter uma senha válida ou o usuário digitar 'sair'.
print("~~~~~~~~~~~~~~~~~~~~")

def tem_numero(texto: str) -> bool:
    for ch in texto:
        if ch.isdigit():
            return True
    return False

print("Crie uma senha (mín. 8 caracteres e pelo menos 1 número). Digite 'sair' para encerrar.")

while True:
    senha = input("Senha: ").strip()
    if senha.lower() == 'sair':
        print("Encerrando sem validar senha.")
        break

    if len(senha) < 8:
        print("Senha fraca: deve ter pelo menos 8 caracteres.")
        continue

    if not tem_numero(senha):
        print("Senha fraca: deve conter pelo menos 1 número.")
        continue

    print("Senha forte criada com sucesso!")
    break
print("~~~~~~~~~~~~~~~~~~~~")

# Atividade 4: Par ou ímpar com contagem final
print("~~~~~~~~~~~~~~~~~~~~")

pares = impares = 0

print("Digite números inteiros ou 'fim' para encerrar:")

while True:
    n = input("Número: ").strip().lower()
    if n == "fim":
        break
    if not n.lstrip("-").isdigit():
        print("Entrada inválida.")
        continue
    n = int(n)
    if n % 2 == 0:
        print(f"{n} é par.")
        pares += 1
    else:
        print(f"{n} é ímpar.")
        impares += 1

print(f"Pares: {pares} | Ímpares: {impares}")
print("~~~~~~~~~~~~~~~~~~~~")