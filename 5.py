n=int(input("enter the number "))
for i in range(1,n+1):
    if i%3==0:
        print("Devided By 3")
    elif i%5==0:
        print("Devided By 5")
    else: 
        print(i)