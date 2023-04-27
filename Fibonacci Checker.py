import math
n=int(input("masukkan angka : "))

#Kriteria Gessel untuk bilangan Fibonacci
g1=5*n**2+4
g2=5*n**2-4
if math.floor(math.sqrt(g1))== math.sqrt(g1):
      print(str(n) + " adalah bilangan Fibonacci")
else :
    if math.floor(math.sqrt(g2))== math.sqrt(g2):
        print(str(n) + " adalah bilangan Fibonacci")
    else:
        print(str(n) + " bukan bilangan Fibonacci")
