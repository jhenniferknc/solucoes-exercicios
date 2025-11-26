idadeEmDias = int(input("Quantidade de dias: "))

anos = idadeEmDias // 365
resto = idadeEmDias % 365
meses = resto // 30
dias = resto % 30

print(f"{anos}A{meses}M{dias}D")