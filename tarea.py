import os, time
trabajadores = []
cargos = ('CEO','DESAROOLADOR','ANALISTA')
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
        print ('Registro de trabajadores')
        nombre_apellido = input('Ingrese nombre y apellido')
        cargo = int(input('Ingrese cargo(1:CEO, 2:DESSARROLADOR, 3:ANALISTA): '))
        sueldo_bruto = int(input('Ingrese sueldo bruto'))
        salud = int(7/100 * sueldo_bruto)
        afp = int(0.12 * sueldo_bruto)
        sueldo_liquido = sueldo_bruto-(salud+afp)
        trabajador = [nombre_apellido,cargos[cargo-1],sueldo_bruto,salud,afp,sueldo_liquido]
        trabajadores.append(trabajador)
        print('Trabajador registrado')
    elif opc==2:
        pass
    elif opc==3:
        pass
    else:
        print ('gracias, adios')
        break
    time.sleep(2)