import random
def PuntoDeCorte(a,b,c):
    if b - a == 0:
        return 0
    fc=(c-a)/(b-a)
    return fc

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

a=float(input("Ingrese el tiempo minimo: "))
b=float(input("Ingrese el tiempo maximo: "))
c=float(input("Tiempo más probable: "))
op=int(input("Escoge las veces que desea simular: "))
SimTriang(op,a,b,c)
