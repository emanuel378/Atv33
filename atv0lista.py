lista =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(lista[:10])
print(lista[8:14])
print(lista[0:16:2])
print(lista[1:16:2])
print("os multiplos de 2 e {}".format(lista[0:16:2]))
print("Os multiplos de 3 e {}".format(lista[0:16:3]))
print("Os multiplos de 4 e {}".format(lista[0:16:4]))
lista.reverse()
print(lista)
