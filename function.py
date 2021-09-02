import calculation
#function which ask user to input a integer value
#return-type function
output=[0,0,0,0,0,0,0,0]
def NumberInput(userValue):
   
    while ((userValue<0 or userValue>255)):
        print("Not valid ! Inputing Number should be between 0 and 255")
        print("\n")
        userValue = int(input("Enter a number again\n"))
    return(userValue)
# This reverse function takes remainder of the inputed number and stores the value  from last 
def RevDecimalToBinary(num):
	bit=[0,0,0,0,0,0,0,0]
	counter=0
	while counter!=8:
		remainder=num%2
		bit[7-counter]=remainder
		num=num//2
		counter+=1
	return bit

#adding the two inputed values 
def check(x,y):
    if(x+y>255):
        print("The sum excceds 8 bit")
    else:
        # Storing the values into arrayList of 8 bit
        storeForFirst=RevDecimalToBinary(x)
        storeForSecond=RevDecimalToBinary(y)
        print("\n")
        #calling calculation function
        calculation.calculateResult(storeForFirst, storeForSecond,output)
        #printing out the value of result
        calculation.displayResult(x,y,storeForFirst,storeForSecond,output)
