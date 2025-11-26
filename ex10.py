distancia = int(input("Distância em Km: "))
combustivel = float(input("Total de combustível gasto: "))

consumo = distancia / combustivel

print('{:.3f} km/l'.format(consumo))