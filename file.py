def lsearch(ar,item):
    i=0
    while i<len(ar) and ar[i]!=item:
        i+=1
    if i<len(ar):
        return i
    else:
        return False
n=int(input("enter desired size of list : "))
ar=[0]*n
for i in range(n):
    ar[i]=int(input("element"+str(i)+":"))
item=int(input("\nenter value to be searched"))
index=lsearch(ar,item)
if index:
        print("element found at ",index,"position :",(index+1))
else:
    print("SORRY, given element could not be found")
