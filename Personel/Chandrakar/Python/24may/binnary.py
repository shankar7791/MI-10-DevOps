def binsearch (a,start,end):
    while(start<= end):
        mid =(start+end)//2
        if (n==a[mid]):
            return mid
        elif(n<a[mid]):
            end = mid-1
        elif(n>a[mid]):
            start = mid+1
    return -1
l = [20,30,40,50,60,70,80,90,100]  
n = int(input(f"{l}\nChoise the search of this array ="))  
  
ind = binsearch(l,0,len(l)-1)        
if(ind==-1):
    print("Element not found ")
else:
    print(f"element found in  index = {ind}")    