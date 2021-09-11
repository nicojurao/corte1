"""
CRUD > CREATE READ UPDATE DELETE

crear un contacto
leer todos los contactos
actualizar un contacto
eliminar un contacto

nombre,apellido,celular,email
"""

opcion=1
contactos = []


while opcion != 0:
    print("1-crear un contacto")
    print("2-leer todos los contactos")
    print("3-actualizar un contacto")
    print("4-eliminar un contacto")
    print("0-salir")

    opcion=int(input())

    if opcion==1:
        nombre=input("ingrese el nombre")
        apellido=input("ingrese apellido")
        celular=input("ingrese celular")
        email=input("ingrese email")

        contactos.append({
            "nombre":nombre,
            "apellido":apellido,
            "celular":celular,
            "correo":email,
        })

        input("contacto guardado presione una tecla para continuar")

    elif opcion==2:
        print(contactos)

    elif opcion==3:
        
        contactos.remove()


"""
def crear():
    nombre=input("ingrese el nombre")
    apellido=input("ingrese apellido")
    celular=input("ingrese celular")
    email=input("ingrese email")
    contacto=[nombre,apellido,celular,email]
    return contacto

"""