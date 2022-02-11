velocidad_asteroide = 19
tamano_asteroide = 25

if tamano_asteroide > 25 and velocidad_asteroide > 25:
    print("Alerta! el asteroide viene muy rápido y causará daño por tu tamaño")
elif velocidad_asteroide >= 20:
    print("Alerta! se verá el asteroide en el cielo")
else:
    print("No hay problema, el asteroide no se verá, viene lento y se destruirá en la atmosfera por su tamaño")