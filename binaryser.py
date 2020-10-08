a=[22,34,5,6,3,4,22,78]
a.sort()
print(a)
x=int(input("Enter the no."))
low=0
high=len(a)
pos=-1
while(low<=high):
    mid=int((low+high)/2)
    if(x==a[mid]):
        pos=mid+1
        break;
    if(x<a[mid]):
        high=mid-1
    if(x>a[mid]):
        low=mid+1
if(pos==-1):
    print("not found")
else:
    print("Element at ",pos,"position")
