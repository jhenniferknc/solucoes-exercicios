import math

x1 = float(input("Valor x do primeiro par ordenado: "))
y1 = float(input("Valor y do primeiro par ordenado: "))

x2 = float(input("Valor x do segundo par ordenado: "))
y2 = float(input("Valor y do segundo par ordenado: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print('{:.4f}'.format(distancia))