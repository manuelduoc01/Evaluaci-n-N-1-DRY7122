import xml.etree.ElementTree as ET

# Pedir el nombre y apellido del usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

# Crear el elemento raíz
root = ET.Element("persona")

# Crear los elementos de nombre y apellido
nombre_elem = ET.SubElement(root, "nombre")
apellido_elem = ET.SubElement(root, "apellido")

# Agregar el texto del nombre y apellido a los elementos correspondientes
nombre_elem.text = nombre
apellido_elem.text = apellido

# Crear el árbol XML y escribirlo a un archivo
tree = ET.ElementTree(root)
tree.write("informacion.xml")

