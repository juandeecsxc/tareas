while True :
    try:
## Solicitar datos al usuario

        name =  input(" ingresa nombre de el producto: ")
        precio = float(input("ingresa precio unitario: "))
        cantidad = int(input("ingresa cantidad: "))
        descuento = float(input("ingresa descuento: "))
 # validar datos

        if descuento < 0 or descuento > 100:
            print("El descuento debe estar entre 0 y 100.")
            continue
        if precio < 0:
            print("el precio debe ser positivo")
            continue
        if  cantidad  < 0:
            print(" La cantidad debe ser un número entero positivo.")
            continue
#calculos 

        total = precio * cantidad
        monto_descuento = total * (descuento / 100)
        total_final = total - monto_descuento


        print("\n--- RESUMEN DE COMPRA CAMBIADA ----")
        print(f"Producto: {name}")
        print(f"Precio unitario: {precio: .2f}")
        print(f"Cantidad: {cantidad}")
        print(f"Total sin descuento: ${total:.2f}")
        print(f"Descuento aplicado: {monto_descuento:.2f} ({descuento: .2f}%)")
        print(f"Total final a pagar: ${total_final:.2f}")
        break
    
    except ValueError:
        print("Valores erróneos. Por favor, intente de nuevo")