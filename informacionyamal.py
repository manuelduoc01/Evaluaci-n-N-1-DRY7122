import yaml

# Pedir al usuario que ingrese su nombre y apellido
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

# Crear un diccionario con los datos ingresados
datos = {"nombre": nombre, "apellido": apellido}

# Convertir el diccionario a formato YAML
yaml_data = yaml.dump(datos)

# Imprimir el resultado en consola
print(yaml_data)

