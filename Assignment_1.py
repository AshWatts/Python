se=[]
c=[]
b=[]
f=[]
n=int(input("Enter total number of Students : "))
for i in range(0,n):
    ele=input("Enter Name : ")
    if ele in se:
        continue
    else:
        se.append(ele)
        x = input("Likes Cricket ?  (y/n)   : ")
        if x == "y":
            c.append(ele)

        y = input("Likes Badminton ?   (y/n)    : ")
        if y == "y":
            b.append(ele)

        z = input("Likes Football ?    (y/n)    : ")
        if z == "y":
            f.append(ele)


def inter(lista,listb):
    list2=[]
    for g in lista:
        for h in listb:
            if g==h:
                list2.append(g)
    return list2

def union(listc,listd):
    list3=[]
    for i in listc:
        list3.append(i)
    for j in listd:
        flag=0
        for k in list3:
            if j==k:
                flag+=1
                break
        if flag==0:
                list3.append(j)
    return list3

def differ(listm,listn):
    list4=[]
    for x in listm:
        flag=0
        for y in listn:
            if x==y:
                flag+=1
                break
        if flag==0:
            list4.append(x)

    return list4

def cob(liste,listf):
    l1=union(liste,listf)
    l2=inter(liste,listf)
    l3=differ(l1,l2)
    print(l3)
    return l3

def ncob(y1,y2):
    l1=se
    l2=union(y1,y2)
    l3=differ(l1,l2)
    print(l3)
    return l3

def cfnb(z1,z2):
    l1=inter(z1,z2)
    l2=b
    l3=differ(l1,l2)
    print(l3)
    return l3

print("")
print("""Choose one of the Options : 
Likes Cricket and Badminton                    : 1
Likes Either Cricket or Badminton but not both : 2
Likes Neither Cricket nor Badminton            : 3
Likes Cricket and Football but not Badminton   : 4 
Exit                                           : 5
""")
while True:
    n=int(input("Enter Operation to be Performed : "))
    if(n==1):
        inter(c,b)
    elif(n==2):
        cob(c,b)
    elif(n==3):
        ncob(c,b)
    elif(n==4):
        cfnb(c,f)
    elif(n==5):
        print("Terminated.")
        break
    else:
        print("Enter a Valid Option!")

