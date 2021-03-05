n=int(input("Enter the length of the series "))
x=0
y=1
 for i in range(1,n+1):
        print(x)
        x,y=y,x+y
