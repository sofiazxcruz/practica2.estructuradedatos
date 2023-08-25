#Ejercicio1
continuar = True
totalVenta = 0
cantidadVenta = 0

def inputNumber(mensaje, isFloat = False):
    while True:
        try:
            if isFloat:
                return float(input(mensaje))
            return int(input(mensaje))
        except ValueError:
            print("Opss!! no es una entrada valida bro, pli intenta nuevamente")

while continuar == True:
    cantidad = inputNumber("Ingresar la cantidad del producto: ")
    precio = inputNumber("Ingrese el precio por unidad: ", True)
    
    totalSinDescuento = cantidad * precio
    
    if cantidad >= 5 and cantidad <= 10:
        totalVenta += totalSinDescuento - ((totalSinDescuento) * 0.5)
    elif cantidad >= 11 and cantidad <= 20:
        totalVenta += totalSinDescuento - ((totalSinDescuento) * 0.10)
    elif cantidad > 20:
        totalVenta += totalSinDescuento - ((totalSinDescuento) * 0.15)
    else: totalVenta += (cantidad*precio)
    
    cantidadVenta += cantidad 
    
    opcion = input("Continuar? S/N") 
    if opcion.upper() == "N":
        continuar    = False
        print("Gracias por comprar!!")
    
print (f"El total fue ${totalSinDescuento}".format(totalSinDescuento))
print (f"Total de la venta con descuento es de ${totalVenta}")
print ("Unidades totales {0}".format(cantidadVenta))