#input

num_min = int(input("digite el numero de minutos"))

#processing

if  num_min < 4:
    costo=300

else:
    costo = (num_min * 50) + 300 - 150

    #output
    print("los gastos totales son " + str(costo))