def currency():
    print("Enter $ for Doller , # for pound ,R for rayal  D for darham Ran for ringet ") 
    x= input("Enter the  type of currency u have : ").lower() 

    y = float(input("Enter your amount : "))
    
    if x== "$":
        amount= y*250
    
    elif x== "p":
        amount= y*300
    elif x=="r":
        amount= y*70
    elif x=="d":
        amount= y*75
    elif x=="ran":
        amount= y*100
    else:
        return " Wrong currency"
    
    print(f"The total amount is {amount}")  
while(True):
        currency()
        again=input("Do u want to exchange any other type of curency y/n  ? ")
        if again !="y":
            break