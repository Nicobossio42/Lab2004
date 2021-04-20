#def coordenadaZ(x, y):
    #x = x + 10
    #y = y + 15
    #return x + y


# programa principal
x = int(input("Coordenada eje x: "))#se introduce el primer valor requerido por el usuario
y = int(input("Coordenada eje y: "))#se introduce el segundo valor requerido por el usuario
for i in range(3):
    x = x + 1
    y = y + 1
print(x, " . ", y)
