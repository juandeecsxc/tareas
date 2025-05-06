# # Datos corregidos
# usuarios = [
#     ["antonio", "23", "antonio@gmail.com"],
#     ["juan", "23", "juan@gmail.com"],
#     ["maria", "24", "ria@gmail.com"],
#     ["24", "haol", "ha@gmail.com"],
#     ["sf@gmail.com", "23", "juanss"]
# ]

# # # Clasificar datos
# # datos_clasificados = {"nombres": [], "edades": [], "correos": []}
# # for usuario in usuarios:
# #     for dato in usuario:
# #         if "@" not in dato and "." not in dato and not dato.isnumeric():  # Verifica si el dato es un nombre
# #             datos_clasificados["nombres"].append(dato)
# #         elif dato.isnumeric():  # Verifica si el dato es una edad
# #             datos_clasificados["edades"].append(dato)
# #         elif "@" in dato and "." in dato:  # Verifica si el dato es un correo
# #             datos_clasificados["correos"].append(dato)

# # # Mostrar datos clasificados
# # print("Nombres:", datos_clasificados["nombres"])
# # print("Edades:", datos_clasificados["edades"])
# # print("Correos:", datos_clasificados["correos"])


# #########################################################################
# # Clasificar datos sin segundo for
# datos_clasificados = {"nombres": [], "edades": [], "correos": []}
# for nombre, edad, correo in usuarios:
#     if "@" not in nombre and "." not in nombre and not nombre.isnumeric():
#         datos_clasificados["nombres"].append(nombre)
#     if edad.isnumeric():
#         datos_clasificados["edades"].append(edad)
#     if "@" in correo and "." in correo:
#         datos_clasificados["correos"].append(correo)

# # Mostrar datos clasificados
# print("Nombres:", datos_clasificados["nombres"])
# print("Edades:", datos_clasificados["edades"])
# print("Correos:", datos_clasificados["correos"])

######

# Cajero básico
saldo = 0  # Saldo inicial

while True:
    print("\nBienvenido al cajero automático")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        monto = float(input("Ingrese el monto a depositar: "))
        if monto > 0:
            saldo += monto
            print(f"Has depositado ${monto}. Tu nuevo saldo es ${saldo}.")
        else:
            print("El monto debe ser mayor a 0.")
    elif opcion == "2":
        monto = float(input("Ingrese el monto a retirar: "))
        if 0 < monto <= saldo:
            saldo -= monto
            print(f"Has retirado ${monto}. Tu nuevo saldo es ${saldo}.")
        else:
            print("Fondos insuficientes o monto inválido.")
    elif opcion == "3":
        print(f"Tu saldo actual es ${saldo}.")
    elif opcion == "4":
        print("Gracias por usar el cajero automático. ¡Adiós!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
