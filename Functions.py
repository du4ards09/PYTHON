#1.Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta do garçom,
# considerando 10% do valor da conta.

def calcularGorjeta():
    valorDaconta = float(input("Digite o valor da conta: "))

    gorjeta = valorDaconta * 0.10
    print(f"A gorjeta que o garçom ganhou é de : R$ {gorjeta:.2f}")

# Colocando o número já aqui :<
calcularGorjeta()

print()

#2.Elabore uma função para calcular o salário final de um funcionário de acordo com as seguintes informações:
#a) se o salário for maior que >=2000 reajuste de 20%.
#b) se o salário for menor que <2000 reajuste de 15%.
#O programa deve solicitar o nome do funcionário e o salário do funcionário.
#Ao término deve exibir: Nome do funcionário, salário antigo, faixa de reajuste, valor do reajuste e salário final.

def salarioFinal():
    nome = input("Digite o seu nome ai por favor: ")
    salario = float(input("Digite o seu money recebido : "))

    if salario >= 2000:
        reajuste = 0.20
        faixa = "20%"
    else:
        reajuste = 0.15
        faixa = "15%"

    valorReajuste = salario * reajuste
    salarioFinal = salario + valorReajuste

    print("\nResumo:")
    print(f"Nome do funcionário: {nome}")
    print(f"Salário antigo: R$ {salario:.2f}")
    print(f"Faixa de reajuste: {faixa}")
    print(f"Valor do reajuste: R$ {valorReajuste:.2f}")
    print(f"Salário final: R$ {salarioFinal:.2f}")

salarioFinal()

print()

#3.Desenvolva uma função para solicitar dois números e realizar as 4 operações matemáticas básicas:
# soma, subtração, divisão e multiplicação.

def operacoesMatematicas():
    numero1 = float(input("Digite o número 1: "))
    numero2 = float(input("Digite o número 2: "))

    print(f"Soma: {numero1 + numero2}")
    print(f"Subtração: {numero1 - numero2}")
    print(f"Multiplicação: {numero1 * numero2}")
    print(f"Divisão: {numero1 / numero2}" if numero2 != 0 else "Divisão: Indefinida (divisão por zero)")

operacoesMatematicas()

print()

#Construa uma função para a seguinte situação que o usuário deve digitar uma opção:
#1 – Calculo da Area do Trapézio.
#2 – Calculo da Area do Círculo.
#3 – Calculo da Area do Triangulo.
#4 – Calculo da Area do Retângulo.
#5 – Calculo da Area do Losango.
#0 – Sair do Programa.

import math
def Geometria(opcao):
    if opcao == 1:
        print("Area do Trapezio:")
        baseMaior = int(input("Digite a Base Maior: "))
        baseMenor = int(input("Digite a Base Menor: "))
        h = int(input("Digite a Altura: "))

        Resultado = (baseMaior + baseMenor) * h / 2

    elif opcao == 2:
        print("Area do Circulo")
        raio = int(input("Digite o raio: "))
        raio * 2

        Resultado = math.pi


    elif opcao == 3:
        print("Area do Triangulo")
        base = int(input("Digite a Base : "))
        h = int(input("Digite a Altura: "))

        Resultado = base * h / 2

    elif opcao == 4:
        print("Retangulo")
        base = int(input("Digite a Base : "))
        h = int(input("Digite a Altura: "))

        Resultado = base * h
    else:
        print("Area do Losangolo")
        DiagonalMaior = int(input("Digite a Diagonal Maior: "))
        DiagonalMenor = int(input("Digite a Diagonal Menor: "))
        Resultado = DiagonalMaior * DiagonalMenor / 2

    print(f"Resultado: {Resultado}")


opcao = int(input(
    "Digite a opcao que deseja Calcular a Area: 1 - Trapezio, 2 - Circulo, 3 - Triangulo, 4 - Retangulo, 5 - Losangulo e 0 se deseja sair "))

while opcao != 0:
    i = opcao

    if opcao == 0:
        i == 0
    else:
        Geometria(opcao)
        i += 1
        opcao = int(input(
            "Digite a opcao que deseja Calcular a Area: 1 - Trapezio, 2 - Circulo, 3 - Triangulo, 4 - Retangulo, 5 - Losangulo e 0 se deseja sair "))

print("sessao terminada!")


print()

#5 - Escreva um programa que leia três números e que imprima o maior e menor.

def maiorOuMenor():
    # Leia os números
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    numero3 = float(input("Digite o terceiro número: "))

    maior = max(numero1, numero2, numero3)
    menor = min(numero1, numero2, numero3)

    print(f"\nO maior número é: {maior}")
    print(f"O menor número é: {menor}")

maiorOuMenor()

print()

#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação:
# R para residências,
# I para indústrias e C para comércios.
# Calcule o preço a pagar de acordo com a tabela a seguir.

def calcularEnergia(kwh, instalacao):
    if instalacao == 'R':
        if kwh <= 500:
            preco = kwh * 0.40
        else:
            preco = kwh * 0.65
    elif instalacao == 'C':
        if kwh <= 1000:
            preco = kwh * 0.55
        else:
            preco = kwh * 0.60
    else:
        if kwh <= 5000:
            preco = kwh * 0.55
        else:
            preco = kwh * 0.60

    print(f"O preço a pagar é: R${preco}")


kwh = float(input("Digite a quantidade de kWh consumidos: "))
instalacao = input("Digite o tipo de instalação (R, C ou I): ").upper()

preco = calcularEnergia(kwh, instalacao)
