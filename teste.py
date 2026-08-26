  n = int(input('digite um número: '))
if (n % 2 == 0):
    print('seu número é par!')
else:
    print('seu número é ímpar!')

 
 n1 = int(input('digite um número: '))
 n2 = int(input('digite outro número: '))
if (n1 >= n2):
    print('n1')
if (n2 >= n1):
    print('n2') 


letra = input('digite uma letra: ')
if letra in "aeiou":
    print('é uma vogal')
else:
    print('é uma consoante')   


nota1 = int(input('qual sua nota: '))  
nota2 = int(input('qual sua outra nota: '))   
m = (nota1 + nota2) / 2
 if (m >= 7 and m < 10):
    print('aprovado!')
 elif (m == 10):
    print('aprovado com distinção!')
 else:
    print('desaprovado!')    


n1 = int(input('primeira nota: ')) 
n2 = int(input('segunda nota: ')) 
n3 = int(input('terceira nota: '))  

maior = max(n1, n2, n3)
print('o maior numero é: ', maior)


turno = input('em que turno você estuda, V, M ou N?')
 if (turno == 'M'):
    print('Bom dia!')
 elif (turno == 'V'):
    print('Boa tarde!')
 elif (turno == 'N'):
    print('Boa noite!') 
 else:
    print("Valor inválido!") 


p1 = input('telefonou para a vitima? ').lower()
p2 = input('esteve no local do crime? ').lower()
p3 = input('mora perto da vitima? ').lower()
p4 = input('devia para a vitima? ').lower()
p5 = input('ja trabalhou com a vitima? ').lower()

resposta = 0
if (p1 == 'sim'):
    resposta = resposta + 1
if (p2 == 'sim'):
    resposta = resposta + 1 
if (p3 == 'sim'):
    resposta = resposta + 1
if (p4 == 'sim'):
    resposta = resposta + 1
if (p5 == 'sim'):
    resposta = resposta + 1   

if (resposta == 5):
    print('Assasino')
elif (resposta == 3 or resposta == 4):
    print('Cúmplice')    
elif (resposta == 2):
    print('Suspeito')
else:
    print('Inocente')    