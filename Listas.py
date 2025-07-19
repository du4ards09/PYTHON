#1.Apresente o total de itens da lista exibida abaixo com os meses do ano.Retorno de um número inteiro.

listaMeses  =  ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
print(len(listaMeses))

#2.Junte as duas listas em uma terceira lista vazia. Concatene as duas listas
primeiroSemestre = ['Jan','Fev','Mar','Abr','Mai','Jun']
segundoSemestre = ['Jul','Ago','Set','Out','Nov','Dez']
todosSemestres = primeiroSemestre + segundoSemestre

print(todosSemestres)

#3.imprima de maneira separada o primeiro e último iten da lista.
ListaValores = [2200, 3400, 5750,800,2000,1350]

print('Primeiro Item da Lista ', ListaValores[0])
print('Ultimo Item da Lista ',ListaValores[-1])

#4.Adicione o nome Paula Fernandes na posição 2.

Nomes = [ 'Suzy', 'Janaina', 'Claudevan', 'Maria Clara']

Nomes.insert(2,'Paula Fernandes')

print(Nomes)

#5.Alter o nome Sony para Sony Vaio. Remova o nome Compaq da lista.

Nomes2 = ['Dell', 'Apple', 'Sony', 'Acer', 'Compaq', 'Positivo', 'Lenovo']

Nomes2[2] = 'Sony Vaio'
Nomes2.remove('Compaq')

print(Nomes2)

#6.Imprima em ordem numérica crescente (do menor para o maior) a lista exibida

listadeNumeros =[ 230,430,100,2,670,1212,321,89,6,34,20,9,99,710 ]
listadeNumeros.sort(reverse=False)

print(listadeNumeros)

#7.Imprima em ordem numérica decrescente (do maior para o menor) a lista exibida abaixo.

listadeNumeros =[ 230,430,100,2,670,1212,321,89,6,34,20,9,99,710 ]
listadeNumeros.sort(reverse=True)

print(listadeNumeros)

#8.Escreva um programa que leia uma lista(10 valores) de números inteiros e imprima a soma de todos os números pares da lista. A entrada dos valores deve ser informada pelo usuário.

Numeros = []
for i in range (0, 10):
 Numeros.append(int(input('digite um valor:')))

if(Numeros[i] % 2==0):
    print(sum(Numeros))

print(Numeros)