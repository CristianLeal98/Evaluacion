import os
os.system("cls")

productos=[]

def registrar_productos():
    print("----Registrar Productos----")
    codigo=input("Ingrese el codigo numerico de 6 digitos ")
    while len (codigo) !=6 or not codigo.isdigit():
        print("El codigo debe tener 6 numeros ")
    nombre=input("ingrese el codigo del producto (entre 2 y 50 caracteres): ")
    while len (nombre) < 2 or len (nombre) > 50:
        print("El nombre del producto debe de tener enntre 2 a 50 caracteres")
        nombre=input("Ingrese el nombre del producto")
    categoria=input("Ingrese la categoria del producto: ")
    precio=int(input("Ingrese el precio del producto:  "))
    stock=int(input("Ingrese la cantidad de stock disponible"))
    while stock <= 0:
        print("La cantidad disponible en stock debe ser un numero entero positivo.")
        stock=int(input("Ingrese la cantidad de stock disponible: "))

    productos.append({
        "codigo":codigo,
        "nombre":nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock })
    print("productos registrados con exito")
    print()

def buscar_producto():
    print("---Buscar Producto---")
    categoria_buscar =input("Ingrese el codigo del producto a buscar:")
    while len(categoria_buscar) !=6 or not categoria_buscar.isdigit():
        print("El codigo numerico debe de tener 6 digitos")
        categoria_buscar= input("Ingrese el codigo del producto: ")
    productos_encontrados=[productos for producto in productos if producto["codigo"][:6] == categoria_buscar]

    if productos_encontrados:
        print("productos encontrados en la categoria", categoria_buscar + ":")
        for productos in productos_encontrados:
            print("codigo",producto["codigo"])
            print("nombre:", producto["nombre"])
            print("categoria",producto["categoria"])
            print("precio", producto["precio"])
            print("stock", producto["stock"])
            print("--------------")
    else:
        print("No se encontraron productos en la categoria", categoria_buscar)
    print()
def listar_producto():
    print("----Lista De Productos----")
    print("{:<10} {:<20}{:<15}{:<10}{:<10}{:<10}".format("codigo","nombre","categoria","precio","stock bajo"))
    for producto in productos:
        codigo = producto["codigo"]
        nombre = producto["nombre"]
        categoria= producto["categoria"]
        precio=producto ["precio"]
        stock=producto["stock"]
        stock_bajo="Si" if stock<5 else "No"
        print("{:<10}{:<20}{:<15}${:<9.2f}{:<10}{:<10}".format(codigo,nombre,categoria,precio,stock,stock_bajo)) 
    cantidad_stock_bajo=sum(1 for producto in productos if producto["stock"]<5)

