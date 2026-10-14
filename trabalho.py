try:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    resultado = n1 / n2
except ValueError:
    print('Entrada inválida! Digite apenas números')
except ZeroDivisionError:
    print('Erro! Não é possível dividir por zero.')
else:
    print(f'O resultado da divisão é: {resultado}')




def calcular(nota):
    media = sum(nota) / len(nota)
    return media

lst = [8, 9, 7, 10]
r = calcular(lst)
print(f'A média das notas é: {r}')




def verificar(horas):
    if horas >= 40:
        return 'Carga horária completa'
    else:
        return 'Carga horária insuficiente'

aut = int(input('Digite a quantidade de horas trabalhadas: '))
r = verificar(aut)
print(r)




def calcular(saldo, valor, operacao):
    if operacao == 'deposito':
        saldo += valor
    elif operacao == 'saque':
        saldo -= valor
    return saldo

atial = int(input('Digite o saldo atual: '))
valor = int(input('Digite o valor da operação: '))
operacao = input('Digite a operação (deposito/saque): ')
novo_saldo = calcular(atial, valor, operacao)
print(f'O novo saldo é: {novo_saldo}')




def filtrar(notas):
    aprovados = []
    for nota in notas:
        if nota >= 7:
            aprovados.append(nota)
    return aprovados

notas = [8, 9, 7, 10, 6, 8]
aprovados = filtrar(notas)
print(f'Notas aprovadas: {aprovados}')
