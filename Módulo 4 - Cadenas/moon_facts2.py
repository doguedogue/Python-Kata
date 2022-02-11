text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

palabras_clave=['average','temperature','distance']

for oracion in text.split('.'):
    # print (oracion)
    for palabra in palabras_clave:
        # print(palabra)
        if palabra in oracion:
            print (oracion.replace('C', 'Celsius'))
            break  