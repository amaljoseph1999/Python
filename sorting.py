a=[]  
len=int(input("How many elements are in list : "))
for i in range(len):  
    a.append(int(input())) 
for i in range(len):
    for j in range(0,len-i-1):
                   if(a[j]>a[j+1]):
                         a[j],a[j+1]=a[j+1],a[j]

print(a)
