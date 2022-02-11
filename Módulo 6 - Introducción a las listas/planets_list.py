planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print('There are:',len(planets),'planets, which are:',planets)

planets.append('Pluto')
print('There are:',len(planets),'planets, the last planet is:',planets[-1])
planet_out = planets.pop()
print('Now, there are:',len(planets),'planets, which are:',planets)

planet_input = input('Please enter the name of a planet (capitalize it): ')
index = planets.index(planet_input)

print('This is the ',index+1,' planet')

near_planets_to_sun = planets[0:index]
print('Near planets to sun', near_planets_to_sun)

far_planets_to_sun = planets[index+1:]
print('Far planets to sun', far_planets_to_sun)
