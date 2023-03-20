import math
import pandas as pd


def root(x):
    # a = 2 , b = 5 tol = 0.01 
    # r = pow(x,2) - 2 * x - 3
    # a = 1, b = 2 tol = 0.01 
    # r = pow(x,3) + 4 * pow(x,2) - 10
    r = pow(x,2) - 3
    return r

def cCalculation(a,b,fA,fB):
    c = b - fB * ((b - a) / (fB - fA)) 
    return c   

a = []
b = []
A = float(input("Enter A: "))
B = float(input("Enter B: "))
tolerance = float(input("Enter tolerance: "))


a.append(A)
b.append(B)
tol = 0.01

iteration = round(math.log((b[0] - a[0]) / tol ,2))

c = []
 
funA = []
funB = []
funC = []

found = 0

funA.insert(0,round(root(a[0]) ,4))
funB.insert(0,round(root(b[0]) ,4))

c.insert(0,round(cCalculation(a[0],b[0],funA[0] , funB[0]),4))

funC.insert(0,round(root(c[0]) ,4))

iter = []
iter.insert(0,0)
for i in range(1,iteration + 1):
    
    iter.insert(i,i)
    a.insert(i,b[i - 1])
    b.insert(i,c[i - 1]) 

    funA.insert(i,funB[i - 1])
    funB.insert(i,funC[i - 1])
    
    c.insert(i,round(cCalculation(a[i],b[i],funA[i],funB[i]),4))
    
    funA[i] = round(root(a[i]),4)
    funB[i] = round(root(b[i]),4)
    
    funC.insert(i,round(root(c[i]),4))

    if(abs(funC[i]) <= tol):
        found = 1
        break
 #   print(f"a: {a} , b : {b} , c: {c} , funA : {funA} , funB: {funB} ,  funC: {funC}")

Secant_calculations = {
                    "i" : iter,
                    "a" : a,
                    "b" : b,
                    "c" : c,
                    "F(a)" : funA,
                    "F(b)" : funB,
                    "F(c)" : funC}

Secant_calculations_table = pd.DataFrame(Secant_calculations)                     
print(Secant_calculations_table)   

if(found == 1):
    print(f"Root is : {c[i]}")
else:
    print(f"Root not found!")


