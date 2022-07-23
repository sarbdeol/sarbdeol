while True:    
    num = int(input("Enter number"))
    prime = True
    for i in range(2,num):
        if (num%i == 0):
            prime = False
            break
    if prime:
        print("prime number") 
    else:
        print("not prime")  
    Q=input("want to continue type y \n")
    if Q=="y" or Q=='Y':
        continue
    else:
        exit(0)