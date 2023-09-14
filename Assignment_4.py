class Search:

    def __init__(self):
        self.l1=[]
        n=int(input("Enter the Number of Elements : "))
        self.n=n
        for i in range(n):
            ele=int(input("Enter the Element : "))
            self.l1.append(ele)
        print("Entered Elements : ",self.l1)


    def key(self):
        a = int(input("Enter the Element to be Searched : "))
        self.a=a


    def linear_s(self):
        flag = False
        for i in range(self.n):
            if(self.l1[i]==self.a):
                print("Element is at Position ",i+1)
                flag = True
                break

        if(flag == False):
            print("Element does not exists.")


    def sentinel_s(self):
        last = self.l1[self.n - 1]
        self.l1[self.n - 1] = self.a
        i = 0

        while (self.l1[i] != self.a):
            i += 1
        self.l1[self.n - 1] = last

        if ((i < self.n - 1) or (self.l1[self.n - 1] == self.a)):
            print("Element is at position ", i + 1)
        else:
            print("Element not found.")


    def binary_s(self):
        low=0;
        high=self.n - 1
        mid=0

        while(low<=high):
            mid = (low + high) // 2
            if(self.a==self.l1[mid]):
                print("Element is at position ",mid+1)
                break
            elif(self.a>self.l1[mid]):
                high=mid-1
            else:
                low=mid+1

        else:
            print("Element not found!")


    def fibonacci_s(self):
        self.l1.sort()
        print("Sorted List : ",self.l1)
        fm2=0
        fm1=1
        m=fm2+fm1
        flag = False

        while(m<=self.n):
            fm2=fm1
            fm1=m
            m=fm1+fm2

        offset=0
        i = min(offset + fm2 , self.n-1)

        if(self.a == self.l1[i]):
            print("Element is at position ",i+1)
            flag = True

        elif(self.a > self.l1[i]):
            offset = i
            m=fm1
            fm1=fm2
            fm2=m-fm1

        else:
            offset = i
            m=fm2
            fm1=fm1-m
            fm2=m-fm1

        if(self.a == self.l1[0]):
            print("Element is at position 1")
            flag = True

        if(self.a == self.l1[self.n-1]):
            print("Element is at position ",self.n)
            flag = True

        if(flag == False):
            print("Element does not exists.")











a=Search()
a.key()

print("""
Choose a way of Searching : 
Linear Search : 1
Sentinel Search : 2
Binary Search : 3
Fibonacci Search : 4
""")

b=int(input("Enter your choice : "))
if(b==1):
    a.linear_s()
elif(b==2):
    a.sentinel_s()
elif(b==3):
    a.binary_s()
elif(b==4):
    a.fibonacci_s()
else:
    print("Enter a Valid Option")

