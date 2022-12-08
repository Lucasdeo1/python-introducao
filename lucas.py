print("hello word")


l = "lucazada"

print(l)

c =  4

d = 5

print( d-c )


x = "incrivel" #variavel global

def funcao():
  x = "fantastico"
  print("isso é " + x)

funcao()

print("Python is " + x)

s = 5.0

print(type(s)) #conferir tipo de dado da variavel



import random #gerrador randomico

print(random.randrange(1, 10)) #imprimir variaveis aleatorias de 1 a 9

h = "lucas"
print(h[4])

for h in "lucas": #para o for exige recuo pois esta dentro do loop
    print(h)