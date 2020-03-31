ficha = [4.00, 4.50, 5.00, 2.00, 1.50]
cod, quant = map(int, input().split())

preco = ficha[cod-1] * quant

print(f'Total: R$ {preco:.2f}')
