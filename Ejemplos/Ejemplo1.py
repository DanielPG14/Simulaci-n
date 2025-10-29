import numpy as np
import matplotlib.pyplot as plt

def Grafica(a,b,c):
    fig,ax=plt.subplots()
    AltMax= 2/(b-a)
    ax.plot([a,c],[0,AltMax],color="red")
    ax.plot([c,b],[AltMax,0],color="red")
    """primer punto x1,y1, segundo punto es x2,y2"""
    plt.show()

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
        print("Terminando el programa")
        return op==3
    else:
        print("Opción no válida. Escoja '1' o '2'.\n")

a=float(input("Ingrese el costo minimo: "))
b=float(input("Ingrese el costo maximo: "))
c=float(input("Costo más probable: "))
Grafica(a,b,c)
print("Escoge la opción que deseas:")
op=0
while op!=3:
    op=int(input("1. Determinar la probabilidad de que el numero sea menor o igual a tal numero\n2. Determinar la probabilidad de que el numero este entre tales números\n3. Salir\n"))
    Calcular_DT(op,a,b,c)

