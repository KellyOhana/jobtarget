import json
from statistics import mean

with open("dados.json") as file:
    data = json.load(file)

dias = []

minimo = min(data['valor'] for data in data if data['valor'] != 0)

maximo = max(data['valor'] for data in data)

media = mean(data['valor'] for data in data if data['valor'] != 0)

for data in data:
    if data['valor'] == minimo:
        diaMin = data['dia']
    elif data['valor'] == maximo:
        diaMax = data['dia']
    if data['valor'] > media:
        dias.append(data['dia'])

print(f"O valor minimo é: {minimo} no dia {diaMin}")
print(f"O valor maximo é: {maximo} no dia {diaMax}")
print(f"Dias acima da media:\n{dias}")



