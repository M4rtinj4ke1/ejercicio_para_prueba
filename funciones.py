trabajadores = []
cargos = ('CEO','DESAROOLADOR','ANALISTA')
def registrar_trabajador():
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

def listar_trabajador():
 pass

def exportar_archivo_txt():
 pass

def salir():
    print ('gracias, adios')
    exit()