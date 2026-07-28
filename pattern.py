#row=int(input("Enter row range: "))
#cols=int(input("Enter column range: "))

row=4
for i in range(1,row+1):
    for z in range(1,row-i+1):
        print(" ",end=" ")
    #A
    for j in range(1,i+1):
        print(j,end=" ")
    #B
    for k in range(i-1,0,-1):
        print(k,end=" ")
    print()



row=3
i=row
while(i>=1):
    for z in range(1,row-i+1):
        print(" ",end=" ")
    #A
    for k in range(i-1,0,-1):
        print(k,end=" ")
    #B
    j=i
    while(j>=1):
        print(j,end=" ")
        j-=1
    print()
    i-=1