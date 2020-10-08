#Linear searching
ar=(22,43,56,43,78,23)
l=len(ar)
pos=-1
x=int(input("Enter the No. "))
for i in range(0,l):
    if (x==ar[i]):
       pos=i+1
       break;
if(pos==-1):
    print("Not found")
else:
    print("The element ",x,"at",pos," th position")
     
    
