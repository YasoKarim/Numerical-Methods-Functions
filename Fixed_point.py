import pandas as pd
import numpy
import math

def root(x):
    r = math.exp(-x) -x
    return r

def Funcg(x):
    r = math.exp(-x)  
    return  r

x = []
funcx = []
funcg = []

'''
n = 5
x.append(0.5)
tol = 0.01
'''

N = int(input("Enter number of iterattions: "))
x = float(input("Enter x: "))
tolerance = float(input("Enter tolerance: "))

funcx.insert(0,round(root(x[0]),4))

funcg.insert(0,round(Funcg(x[0]),4))

iter = []
iter.insert(0,0)

found = 0 

for i in range(1,n):
    iter.insert(i,i)
    
    x.insert(i,funcg[i -1])
    
    funcx.insert(i,round(root(x[i]),4))
    funcg.insert(i,round(Funcg(x[i]),4))

    if(abs(funcg[i]) <= tol):
        found = 1
        break

Fixed_point_calculations = {
                    "i" : iter,
                    "x" : x,
                    "F(xi)" : funcx,
                    "G(xi)" : funcg,
                                }   
Fixed_point_calculations_table = pd.DataFrame(Fixed_point_calculations)                     

print(Fixed_point_calculations_table)   

if(found == 1):
    print(f"Root is : {x[i]}")
else:
    print(f"Root not found!")