n = int(input("numero que deseja buscar na sequencia de fibonacci: "))
ultimo = 1
penultimo = 1
valor = 0
lista = [0, 1, 1]

while valor < n:
    valor = ultimo + penultimo
    penultimo = ultimo
    ultimo = valor
    lista.append(valor)

print(lista)
if n in lista:
    print("Numero encontrado!")
else:
    print("Numero não encontrado!")
