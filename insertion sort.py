arr=[]  
len1=int(input("How many elements are in list : "))
for i in range(len1):  
    arr.append(int(input())) 
for i in range(1, len1):
    key = arr[i]
    j = i-1
    while j >=0 and key < arr[j]:
         arr[j+1] = arr[j] 
         j -= 1
    arr[j+1] = key 
    
print(arr)
