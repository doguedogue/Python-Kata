name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

gravity_facts_title = """
Gravity Facts about %s
-------------------------------------------------------------------------------"""
print(gravity_facts_title %name)

gravity_facts = """
Planet Name: %s
Gravity on %s: %s m/s2"""
print(gravity_facts %(planet,name,round(gravity*1000,2)))

union = ''.join([gravity_facts_title, gravity_facts])
print(union % (name, planet,name,round(gravity*1000,2)))

planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'
print(union % (nombre, planeta,nombre,round(gravedad*1000,2)))

plantilla = """
Gravity Facts about {0}
-------------------------------------------------------------------------------
Planet Name: {1}
Gravity on {0}: {2} m/s2"""
print(plantilla.format(nombre,planeta,round(gravedad*1000,2)))

graveda_ms = round(gravedad*1000,2)
print(plantilla.format(nombre,planeta,graveda_ms))
