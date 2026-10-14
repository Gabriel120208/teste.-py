i = 0
while (i <= 100):
    print(i)
    i = i + 1


i = 0
n = int(input('digite um número: '))
while (i <= n):
    print(i)
    i = i + 1    



i = 'sim'
while (i == 'sim'):
    n1 = int(input('digite um número: '))
    n2 = int(input('digite outro número: '))
    s = n1 + n2
    print('a soma é {}!'.format(s))

    i = input('deseja realizar a operação? (sim/não)').lower()
print('fim do programa!')    



a, b = 0, 1
print(a)

while a <= 500:
    print(b)
    a, b = b, a + b



n = int(input("Quantos números deseja digitar? "))

for i in range(n):
    num = float(input(f"Digite o {i+1} número: "))
    numeros.append(num)

menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")    



n = int(input("Quantos números deseja digitar? "))

for i in range(n):
    while True:
        num = float(input(f"Digite o {i+1} número (entre 0 e 1000): "))
        if 0 <= num <= 1000:
            numeros.append(num)
            break
        print("Valor inválido! O número deve estar entre 0 e 1000.")

menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")



while True:
    nome = input("Digite o nome (maior que 3 caracteres): ")
    if len(nome) > 3:
        break
    print("Erro: O nome deve ter mais de 3 caracteres.")

while True:
    idade = int(input("Digite a idade (entre 0 e 150): "))
    if 0 <= (0, idade) <= 150:
        break
    print("Erro: A idade deve ser entre 0 e 150.")

while True:
    salario = float(input("Digite o salário (maior que zero): "))
    if salario > 0:
        break
    print("Erro: O salário deve ser maior que zero.")

while True:
    sexo = input("Digite o sexo ('f' ou 'm'): ").lower()
    if sexo in ['f', 'm']:
        break
    print("Erro: O sexo deve ser 'f' ou 'm'.")

while True:
    estado_civil = input("Digite o estado civil ('s', 'c', 'v', 'd'): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    print("Erro: Estado civil inválido.")

print("Todos os dados foram validados com sucesso!")



num = int(input("Digite um número inteiro: "))

if num <= 1:
    is_primo = False
else:
    is_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_primo = False
            break
    
if is_primo:
    print(f"O número {num} é primo.")
else:
    print(f"O número {num} não é primo.")