def analisar_lista(numeros):
    soma_total = sum(numeros)
    maior_numero = max(numeros)
    return (soma_total, maior_numero)

minha_lista = [19, 7, 60, 30, 90, 20]

resultado = analisar_lista(minha_lista)

soma, maior = resultado

print(f"Lista analisada: {minha_lista}")
print("-" * 30)
print(f"Soma de todos os números: {soma}")
print(f"O maior número na lista é: {maior}")
print(f"\nResultado como tupla: {resultado}")