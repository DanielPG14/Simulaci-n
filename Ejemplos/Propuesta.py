import random
def PuntoDeCorte(a,b,c):
    fc=(c-a)/(b-a)
    return fc

def Probabilidad(var,a,b,c,x):
    if var==1:
        """CDF Ascendente"""
        CDF_Asd=(x-a)**2/((b-a)*(c-a))
        return CDF_Asd
    elif var==2:
        """CDF Descendente"""
        CDF_Des=1-((b-x)**2/((b-a)*(b-c)))
        return CDF_Des
    else:
        print("Error: Ingrese un numero valido")

def Calcular_DT(op,a,b,c):
    fc=PuntoDeCorte(a,b,c)
    if op==1:
        try:
            x=float(input("Ingrese el numero del punto de interés: "))
            if x<=c:
                Prob=Probabilidad(1,a,b,c,x)
                print(f"La probabilidad de que el costo sea menor o igual al numero {x} es: {Prob}")
            elif x>c:
                Prob=Probabilidad(2,a,b,c,x)
                print(f"La probabilidad de que el costo sea mayor o igual al numero {x} es: {Prob}")
        except ValueError:
            print("Error: Ingrese un numero")
    elif op==2:
        try:
            x=float(input("Ingrese el numero minimo: "))
            y=float(input("Ingrese el numero maximo: "))
            if x>y:
                print("Error: Ingrese un numero valido")
            if x<=c:
                Probx=Probabilidad(1,a,b,c,x)
            elif x>c:
                Probx=Probabilidad(2,a,b,c,x)
            if y<=c:
                Proby=Probabilidad(1,a,b,c,y)
            elif y>c:
                Proby=Probabilidad(2,a,b,c,y)
            print(f"La probabilidad de que el costo este entre {x} y {y} es: {Proby-Probx}")
        except ValueError:
            print("Error: Ingrese un numero")
    elif op==3:
        return op==3
    else:
        print("Opción no válida. Escoja '1' o '2'.\n")

def FuncionInversaAsc(a,b,c,i):
    FIA1=a+((i*(b-a)*(c-a))**0.5)
    FIA=round(FIA1,3)
    return FIA

def FuncionInversaDesc(a,b,c,i):
    FID1=b-(((1-i)*(b-a)*(b-c))**0.5)
    FID=round(FID1,3)
    return FID

def SimTriang(op,a,b,c):
    arrayNums=[]
    arrayResultados=[]
    for i in range(op):
        numAleatorio=random.random()
        numRedondeado=round(numAleatorio,3)
        arrayNums.append(numRedondeado)
    for i in arrayNums:
        print("R=",i)
    fc=PuntoDeCorte(a,b,c)
    print("El punto de corte es:",fc)
    for i in arrayNums:
        if i<=fc:
            NumSim=FuncionInversaAsc(a,b,c,i)
        elif i>fc:
            NumSim=FuncionInversaDesc(a,b,c,i)
        arrayResultados.append((NumSim,i))
    for i,j in arrayResultados:
        print("número generado=",i," a partir de R =",j)

def menu1():
    a=float(input("Ingrese el costo minimo: "))
    b=float(input("Ingrese el costo maximo: "))
    c=float(input("Costo más probable: "))
    print("Escoge la opción que deseas:")
    op=0
    while op!=3:
        op=int(input("1. Determinar la probabilidad de que el numero sea menor o igual a tal numero\n2. Determinar la probabilidad de que el numero este entre tales números\n3. Regresar\n"))
        Calcular_DT(op,a,b,c)

def menu2():
    a=float(input("Ingrese el tiempo minimo: "))
    b=float(input("Ingrese el tiempo maximo: "))
    c=float(input("Tiempo más probable: "))
    op=int(input("Escoge las veces que desea simular: "))
    SimTriang(op,a,b,c)

bs=0
while bs!=3:
    bs=int(input("Escoja una opción:\n1. Calculo de probabilidad\n2. Simulación de números aleatorios\n3. Cerrar aplicación\n"))
    if bs==1:
        menu1()
    elif bs==2:
        menu2()
    else:
        print("Opción no válida. Escoja '1' o '2'.\n")