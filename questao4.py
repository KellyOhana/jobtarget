faturamento = {
    'SP': 67.83643,
    'RJ': 36.67866,
    'MG': 29.22988,
    'ES': 27.16548,
    'Outros': 19.84953
}
faturamentoTotal = sum(faturamento.values())

for e, v in faturamento.items():
    percentual = v / faturamentoTotal * 100
    print(f'percentual de representação do estado: {e} = {percentual} %')
