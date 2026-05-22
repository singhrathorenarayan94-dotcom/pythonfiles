n = int(input("enter the no"))
for i in range(2,n+1):
    if n%i==0:
        print(f"the smallest divisior is : {i}")
        break
    
