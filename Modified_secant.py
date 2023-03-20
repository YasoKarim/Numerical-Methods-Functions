import math
import pandas as pd


def root(x):
    r = pow(x,2) - 2 * x - 3
    #r = pow(x,3) + 4 * pow(x,2) - 10
    #r = pow(x,2) - 3
    #r = math.sin(x) - pow(x,3)
    #print(f"r : {r}")
    return r

def cCalculation(a,b,fA,fB):
    c = b - fB * ((b - a) / (fB - fA)) 
    return c   

a = []
b = []


A = float(input("Enter A: "))
B = float(input("Enter B: "))
tolerance = float(input("Enter tolerance: "))


'''
a.append(2)
b.append(5)
tol = 0.01
'''
a.append(A)
b.append(B)

iteration = round(math.log((b[0] - a[0]) / tolerance ,2))

c = []
 
funA = []
funB = []
funC = []

root_bet = []

funA.insert(0,round(root(a[0]) ,4))
funB.insert(0,round(root(b[0]) ,4))

c.insert(0,round(cCalculation(a[0],b[0],funA[0] , funB[0]),4))


funC.insert(0,round(root(c[0]) ,4))

iter = []
iter.insert(0,0)

found = 0 

for i in range(1,iteration + 1):
    iter.insert(i,i)
    if(funA[i - 1] * funC[i - 1]  < 0):
        root_bet.insert(i,"C And A")
        a.insert(i,a[i - 1])
        b.insert(i,c[i - 1]) 
        
        funA.insert(i,funA[i - 1])
        funB.insert(i,funC[i - 1])
    
        c.insert(i , round(cCalculation(a[i],b[i],funA[i],funB[i]),4))
    
        funC.insert(i,round(root(c[i]),4))
   
    else:
        root_bet.insert(i,"C And B")
        a.insert(i,c[i - 1])
        b.insert(i,b[i - 1]) 

        funA.insert(i,funC[i - 1])
        funB.insert(i,funB[i - 1])
    
        c.insert(i , round(cCalculation(a[i],b[i],funA[i],funB[i]),4))
    
        funC.insert(i,round(root(c[i]),4))
    
    if(abs(funC[i]) <= tolerance):
        found = 1
        root_bet.append("-------")
        break
   
Modified_Secant_calculations = {
                    "i" : iter,
                    "a" : a,
                    "b" : b,
                    "c" : c,
                    "F(a)" : funA,
                    "F(b)" : funB,
                    "F(c)" : funC,
                    "Root Between": root_bet}

Modified_Secant_calculations_table = pd.DataFrame(Modified_Secant_calculations)                     

print(Modified_Secant_calculations_table)   

if(found == 1):
    print(f"Root is : {c[i]}")
else:
    print(f"Root not found!")

