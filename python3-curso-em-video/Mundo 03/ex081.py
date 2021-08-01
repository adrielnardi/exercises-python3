'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.

Create a program that will read multiple numbers and put them in a list. After that, show:
A) How many numbers were entered.
B) The list of values, sorted in descending order.
C) If the value 5 was entered and you are not in the list.
'''
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar [S/N]? '))[0].strip()
    if r in 'Nn':
        break
print('~' * 50)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}.')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')