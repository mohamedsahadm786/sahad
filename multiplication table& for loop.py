j=int(input("enter the number, that you want to calculate the multiplication table"))
i=int(input("enter the limit"))
c=1

for x in range(1,i+1):
    e=x*j
    print(str(c)+"x"+str(j)+"="+str(e))
    c=c+1

print(__name__)