import math
import cmath

#---------------------------------------
a=complex(input("a="))
b=complex(input("b="))
print("Somma=",type(a+b),a+b)
#---------------------------------------
r=float(input("Raggio="))
def perimetrocir(r):
  per=2*math.pi*r
  print("Perimetro=",per)
perimetrocir(r)
#---------------------------------------
print(math.tan(math.pi/4))
print(math.cos(math.pi))
#---------------------------------------
c1=True
c2=False

if(c1 and not c2):
  print("c1 and not c2 = True, so b^2=",b**2)
#---------------------------------------
p1="ciao, "
p2="come va?"
print(p1+p2)
#---------------------------------------
vec=[1,2,3]
if(2 in vec):
  print("yes")
else:
  print("no")
  