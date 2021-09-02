def calculateResult(a,b,c):
    carryIn=0
    for i in range(7,-1,-1):
        A=a[i]
        B=b[i]
        andGate_1=(A&B)
        xorGate_1=(A^B)
        Sum=(xorGate_1^carryIn)
        andGate_2=(xorGate_1&carryIn)
        carryOut=(andGate_1 | andGate_2)
        carryIn=carryOut
        c[i]=Sum
        
def displayResult(x,y,a,b,c):
        
    Value=""
    Value1=""
    Value2=""
    for value in a:
        Value1=Value1+str(value)
    for value in b:
        Value2=Value2+str(value)
    for i in range(len(c)):
        Value=Value+str(c[i])
    print(f"The binary addition of {Value1} and {Value2} is: ",Value)



    




