tempo = int(input("Duração em segundos do evento na fábrica: "))

horas = tempo // 3600
tempo = tempo % 3600
minutos = tempo // 60
segundos = tempo % 60

print(f"{horas}:{minutos}:{segundos}")
