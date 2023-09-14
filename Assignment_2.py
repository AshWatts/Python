class string_operations:
    def __init__(self,s):
        self.s=s

    def long(self,s):
        p = s.find(" ")
        if p == -1:
            return s
        maximum = ""
        mot = ""
        while p != -1:
            mot = s[:p]
            s = s[p + 1:len(s)]
            if len(mot) > len(maximum):
                maximum = mot
            p = s.find(" ")
        f = s
        if len(f) > len(maximum):
            maximum = f
        print("Longest Word : ",maximum)


    def oc(self,s):
        a=input("Enter the Character : ")
        count=0
        for i in s:
            if(a==i):
                count+=1
        print("Occurrence : ",count)


    def pal(self,s):
        a = ""
        n = 0
        for i in s:
            n += 1
        for j in range(n - 1, -1, -1):
            a += s[j]
        if (a == s):
            print("Palindrome")
        else:
            print("Not a Palindrome")


    def di(self,s):
        le = 0
        for x in s:
            le += 1
        y = input("Enter the Substring : ")
        a = 0
        for i in y:
            a += 1

        i = 0
        while i < le:

            flag = True
            if s[i] == y[0]:
                for j in range(a - 1):
                    if s[i + j + 1] != y[j + 1]:
                        flag = False
                        break
            else:
                flag = False
            if flag:
                print("Index of given Substring : ", i)
                break
            i += 1

        return -1


    def co(self,s):
        l = []
        m = ''
        for c in s:
            if c == ' ':
                l.append(m)
                m = ''
            else:
                m += c
        if m:
            l.append(m)
        for x in l:
            count = 0
            for y in l:
                if x == y:
                    count += 1
            print("Occurrence of the Words : ")
            print(x, "=", count)


s=input("Enter a String : ")
t=string_operations(s)
print(""" 
Display Longest Word                  : 1
Determine Occurrence of a Character   : 2
Check for Palindrome                  : 3
Display Index of given Substring      : 4
Count Occurrence of each word         : 5
Exit                                  : 6
""")

while True:
    b=int(input("Enter your Choice : "))
    if(b==1):
        t.long(s)
    elif(b==2):
        t.oc(s)
    elif(b==3):
        t.pal(s)
    elif(b==4):
        t.di(s)
    elif(b==5):
        t.co(s)
    elif(b==6):
        print("Program is Terminated.")
        break
    else:
        print("Enter a Valid Option!")