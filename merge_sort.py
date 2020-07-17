def merge(a,b,s,mid,e):
    s1=s
    s2=mid+1
    e1=mid
    e2=e
    index=s1
    while e1>=s1 and e2>=s2:
        if a[s1]<=a[s2]:
            b[index]=a[s1]
            index+=1
            s1+=1
        else:
            b[index]=a[s2]
            index+=1
            s2+=1
    while e1>=s1:
        b[index]=a[s1]
        s1+=1
        index+=1
    while e2>=s2:
        b[index]=a[s2]
        s2+=1
        index+=1
    for i in range(s,e+1):
        a[i]=b[i]

def mergesort(a,b,s,e):
    if s<e:
        mid=(s+e)//2
        mergesort(a,b,s,mid)
        mergesort(a,b,mid+1,e)
        merge(a,b,s,mid,e)

a=[50,25,92,16,76,30,43,54,19]
b=[-1]*9
mergesort(a,b,0,8)
print(a)
