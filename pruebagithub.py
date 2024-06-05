#aqui se supone que hay un código xD es solo una prueba
print(""""\tMENU
          1)guardar usuario
          2)eliminar usuario
          3)Cambiar usuario
          4)Salir """)
while True:
    try:
        opc=int(input("ingrese opción: "))
        if opc in (1,2,3):
            break
        else:
            print("ERROR! ingrese una opción valida")
    except:
            print("ERROR! Tiene que ser un número entero")
if opc==1:
    pass
elif opc==2:
    pass
elif opc==3:
     pass
else:
     pass