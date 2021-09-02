import function
import greeting

greeting.greetingAtBeginning() 

#asking input user two values a and b and passing the value to the function
Loop=True
inputNum=False
while Loop==True:
    while inputNum==False:
        try:
            FirstNum = int(input("Enter a first number\n"))
            FirstNum=function.NumberInput(FirstNum)
            inputNum=True
        except:
            print("Invalid data!!!")
            print("\n")
            continue
        while inputNum==True:
            try:
                SecondNum = int(input("Enter a second number\n"))
                SecondNum=function.NumberInput(SecondNum)
                break
            except:
                print("Invalid data!!!")
                print("\n")    
    function.check(FirstNum,SecondNum)
    q=input("Do you want to continue? '(Y/N)':\n").lower()
    if q == "n":
        break
    else:
        inputNum=False
    print("\n")
    
print("\n")
greeting.GreetingAtEnd()


