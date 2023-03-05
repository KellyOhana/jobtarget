inverterStr = (input("Entre com a string que deseja inverter: "))
# metodo mais simples
Strinvertida = inverterStr[::-1]

# segundo metodo, com loop decrescente
Strinvertida2 = ""
test = ""
for i in range(len(inverterStr)-1, -1, -1):
    Strinvertida2 += inverterStr[i]

print(Strinvertida2)

