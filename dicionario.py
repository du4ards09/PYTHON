meuDicionario = {"chave01": 30, 'chave02': 'Texto Puro', 'chave03': 5.1, 'chave04': True}

valorChave02 = meuDicionario.get("chave02")

print(valorChave02)

meuDicionario['chave05'] = 2023
meuDicionario['chave06'] = False

i = 1
while i < 5:
    meuDicionario[i] = input("Digite")
    i + 1

print(meuDicionario)

novoDicionario = {}

for i in range(1,10):
    novoDicionario[i] = i*i

    print(novoDicionario)