#Input
n=int(input("Enter number of Elements : "))
l=[]
for i in range(n):
    ele=int(input("Element : "))
    l.append(ele)
print(l)


# Bubble Sorts
for i in range(n):
    a=False
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
            a=True

    if(a==False):
        break
print("Bubble Sort : ",l)


# Selection Sort
for i in range(n):
    min=i
    for j in range(i+1,n):
        if(l[min]>l[j]):
            min=j
    l[i], l[min] = l[min], l[i]

print("Selection Sort : ",l)


# Insertion Sort
for i in range(1,n-1):
    temp = l[i]
    j=i-1
    while(j>=0 and temp<=l[j]):
        l[j+1]=l[j]
        j=j-1
    l[j+1]=temp

print("Insertion Sort : ",l)


# Shell Sort
gap = n//2
while gap>0:
    j=gap

    while j<n:
        i=j-gap

        while i>=0:
            if l[i+gap]>l[i]:
                break
            else:
                l[i+gap],l[i]=l[i],l[i+gap]
            i=i-gap
        j=j+1
    gap=gap//2

print("Shell Sort : ",l)