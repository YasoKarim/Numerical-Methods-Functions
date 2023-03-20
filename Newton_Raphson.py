import pandas as pd
import numpy
import math

def root(x):
   # r = pow(x,2) - 2 * x - 3
    r = pow(x,3) + 4 * pow(x,2) - 10
    #r = pow(x,2) - 3
    #r = math.sin(x) - pow(x,3)
    #print(f"r : {r}")
    return r

def derivative(x):
   # r = 2 * x - 2
    r = 3 * pow(x,2) + 8 * x
    return r


def X_calculation(x,fX,Fx):
    new_x = round(x - (fX / Fx),4)
    return new_x




A = float(input("Enter A: "))
b = float(input("Enter B: "))
tolerance = float(input("Enter tolerance: "))

x = []


x.append(A)
tol = 0.01

iteration = round(math.log((b - x[0]) / tol ,2))

iter = []

funx = []
funx_drev =[]

iter.insert(0,0)
funx.insert(0,round(root(x[0]),4))
funx_drev.insert(0,round(derivative(x[0]),4))

for i in range(1,iteration):
    iter.insert(i,i)
    x.insert(i,X_calculation(x[i -1] ,funx[i -1] , funx_drev[i -1]))
    
    funx.insert(i,round(root(x[i]),4))
    funx_drev.insert(i,round(derivative(x[i]),4))

    if(abs(funx[i]) <= tol):
        found = 1
        break

Newton_Rapshon_calculations = {
                    "i" : iter,
                    "x" : x,
                    "F(x)" : funx,
                    "F`(x)" : funx_drev,
                                }   
Newton_Rapshon_calculations_table = pd.DataFrame(Newton_Rapshon_calculations)                     

print(Newton_Rapshon_calculations_table) 

if(found == 1):
    print(f"Root is : {x[i]}")
else:
    print(f"Root not found!")

'''
print(x)
print(funx)
print(funx_drev)
'''