def replace():
    for i in range (len(a)):
        if a[i]<0:
            a[i]=-1
        elif a[i]>0:
            a[i]=1
               
    return (a)

    
a = [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]


print(replace())
print(a)
