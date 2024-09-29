import json

def calcular_faturamento(faturamento):
    with open(faturamento) as f:
        dados = json.load(f)
    
    valores = [registro['valor'] 
               for registro in dados['faturamento'] 
               if registro['valor'] > 0]

    if not valores:
        print("Não há faturamento registrado.")
        return

    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    media_faturamento = sum(valores) / len(valores)

    dias_acima_media = len([valor for valor in valores if valor > media_faturamento])

    print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
    print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

calcular_faturamento('faturamento.json')
