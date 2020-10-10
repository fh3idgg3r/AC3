limite = 600
c = 1
p = 0

for numero in range(2, limite+1):
    for i in range(2,numero):
        if numero % i == 0: break
        c += 1
    else:
        print (numero,)
        p += 1

return ("\n\nEncontramos %d números primos hihi." %p)
