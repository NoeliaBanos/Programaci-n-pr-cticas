edad = 5
#if else
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    
print("--------------------")
#2 if's
ingreso = 1000000
gastos = 7000
# if anidado y elif
if ingreso > 100000:
    if ingreso - gastos < 0:
        print("Te has quedado en rojo")
    elif ingreso - gastos < 3000:
        print("Vives bien")
    else:
        print("Gastas mucho dinero")
    print("Tienes bastante dinero")
elif ingreso > 1000:
    print("Tienes un buen sueldo")
else:
    print("Tienes poco dinero")