b1=int(input("Nota B1"))
b2=int(input("Nota B2"))
b3=int(input("Nota B3"))
b4= input("Nota B4 *").split()

peso1e2=2
peso3e4=3
peso_total=10

calculo = (peso1e2*(b1 + b2) + peso3e4*(b3 + (sum([int(x) for x in b4])/4))) / peso_total
print(calculo)