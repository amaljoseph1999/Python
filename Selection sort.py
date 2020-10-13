arr=[]  
len1=int(input("How many elements are in list : "))
for i in range(len1):  
    arr.append(int(input())) 
for i in range(len1):
    min_idx = i 
    for j in range(i+1, len1): 
        if arr[min_idx] > arr[j]: 
            min_idx = j 
    arr[min_idx],arr[i]=arr[i],arr[min_idx]
    
print(arr)
