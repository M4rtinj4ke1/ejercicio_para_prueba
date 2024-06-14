trabajadores = []
cargos = ('CEO','DESAROOLADOR','ANALISTA')
def registrar_trabajador():
    print ('Registro de trabajadores')
    nombre_apellido =  input('Ingrese nombre y apellido')
    cargo = int(input('Ingrese cargo(1:CEO, 2:DESSARROLADOR, 3:ANALISTA): '))
    sueldo_bruto = int(input('Ingrese sueldo bruto'))
    salud = int(7/100 * sueldo_bruto)
    afp = int(0.12 * sueldo_bruto)
    sueldo_liquido = sueldo_bruto-(salud+afp)
    trabajador = [nombre_apellido,cargos[cargo-1],sueldo_bruto,salud,afp,sueldo_liquido]
    trabajadores.append(trabajador)
    print('Trabajador registrado')

def listar_trabajadores():
    if len(trabajadores)==0:
      print('Lista vacia, registre un trbajador en la opcion 1')
    else:
      print('\tLista de trabajadores')
      for t in trabajadores:
         print(f'NOMBRE: {t[0]}\nCARGO: {t[1]}\nBRUTO: {t[2]}\nSALUD: {t[3]}\nAFP: {t[4]}\nLIQUIDO: {t[5]}')

def exportar_archivo_txt():
 pass

def salir():
    print ('gracias, adios')
    exit()