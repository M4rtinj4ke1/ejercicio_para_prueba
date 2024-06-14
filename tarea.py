import os, time
from funciones import *
while True:
    os.system("cls")
    print("""
            MENU
    1. Registrar trabajadores
    2. Listar todo los trabajadores
    3. Imprimir plantilla de sueldos
    4. Salir del programa""")
    opc = int(input('Ingrese una opcion: '))
    os.system("cls")
    if opc==1:
        registrar_trabajador()
    elif opc==2:
        pass
    elif opc==3:
        pass
    else:
        salir()
    time.sleep(2)