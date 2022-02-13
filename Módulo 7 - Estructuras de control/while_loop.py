# Creamos la variable que almacena el texto
user_input = ''
# Creamos la lista que almacena cada uno de los textos que el usuario ingresa
inputs = []

# Ciclo while
while user_input.lower() != 'done':
    # Verificamos si hay un valor en user_input
    if user_input:
        # Almacenamos ese valor en la lista
        inputs.append(user_input)
    # Capturamos un nuevo valor
    user_input = input('Enter a new value, or done when done: ')
print(inputs)