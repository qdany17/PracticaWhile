#ejer1
numviajes=int(input("ingrese numero de veces que viaja diariamente"))
bssintarj=float(input("ingrese el costo del pasaje sin tarjeta"))
bscontarj=float(input("ingrese el costo del pasaje con tarjeta"))
bstarj=float(input("ingrese el costo con el que compro la tarjeta"))
monttarj=float(input("ingrese el monto con el que venia la tarjeta"))
print ("***************************************************************************")
gastocontarj = numviajes*5*bscontarj
print ("el monto que gastara semanalmente con tarjeta en pasajes es: ", gastocontarj)
print ("***************************************************************************")
tiemenrectarj=bstarj/gastocontarj
print (" el tiempo en recuperar el monto de la tajeta sera en semanas: ")
print(round(tiemenrectarj))
print ("***************************************************************************")
if tiemenrectarj * gastocontarj >= bstarj:
    print("se recupera el monto de la tarjeta")
else:
    print("no se recupera el monto de la tarjeta")
print ("***************************************************************************")