N=int(input("enter the number "))
# for i in range(1,n+1):
#     if range(2,6):
#         print("Weird")
#     else :
#         print("even")

if N % 2== 0:
    print ("Weird")
else:
    if N >= 2 and N <= 5:
        print("Not Weird")
    elif N >= 6 and N <= 20:
        print ("Weird")
    elif N < 20:
        print ("Not Weird")
# x = range(2, 5)
# for p in x:
#     if n%2==0:
#         print("Weird")
#     elif p:
#         print(" not Weird")
    
    