class Matrix:
    def bldm(self,row,col):
        self.__M=[]
        for i in range(row):
            C=[]
            for j in range(col):
                C.append(int(input("Enter Value : ")))
            self.__M.append(C)

    def printMatrix(self):
         for r in self.__M:
             for c in r:
                 print(c,end=' ')
             print()

    def add(self, T,row,col):
        R=Matrix()
        R.__M=[]
        for i in range(row):
            C=[]
            for j in range(col):
                C.append(self.__M[i][j]+T.__M[i][j])
            R.__M.append(C)
        print(R.__M)

    def diff(self,T,row,col):
        R = Matrix()
        R.__M = []
        for i in range(row):
            C = []
            for j in range(col):
                C.append(self.__M[i][j] - T.__M[i][j])
            R.__M.append(C)
        print(R.__M)

    def transpose(self,row,col):

        result=[]
        for x in range(col):
            r = []
            for y in range(row):
                r.append(0)
            result.append(r)
        print (result)

        for i in range(row):
            for j in range(col):
                result[j][i] = self.__M[i][j]

        for r in result:
            print(r)

    def multiply(self,T,row,col,row2):
        result = []
        for x in range(row):
            r = []
            for y in range(col):
                r.append(0)
            result.append(r)

        for i in range(row):
            for j in range(col):
                for k in range(row2):
                    result[i][j] += self.__M[i][k] * T.__M[k][j]

        for r in result:
            print(r)


print("Matrix 1 :- ")
r1=int(input("Enter Number of Rows : "))
c1=int(input("Enter Number of Columns : "))
mat1 = Matrix()
mat1.bldm(r1,c1)
mat1.printMatrix()

print("Matrix 2 :- ")
r2=int(input("Enter Number of Rows : "))
c2=int(input("Enter Number of Columns : "))
mat2 = Matrix()
mat2.bldm(r2,c2)
mat2.printMatrix()

i=1
while i==1:
    print('''
MENU:
1.Addition of the two Matrices
2.Subtraction of the two Matrices
3.Multiplication of the two Matrices
4.Transpose of a Matrix
5.EXIT''')
    op=int(input("Enter your Choice : "))
    if op==1:
        if r1 == r2 and (c1 == c2):
            mat3 = mat1.add(mat2,r1,c1)
        else:
            print("This Operation cannot be performed as the Matrices are Unequal!")
    elif op==2:
        if r1 == r2 and (c1 == c2):
            mat3 = mat1.diff(mat2,r1,c1)
        else:
            print("This Operation cannot be performed as the Matrices are Unequal!")
    elif op==3:
        if r1 == r2 and (c1 == c2):
            mat3 = mat1.multiply(mat2,r1,c1,r2)
        else:
            print("This Operation cannot be performed as the Matrices are Unequal!")
    elif op==4:
        print("Transpose of Whcih Matrix : ")
        print("Matrix A:")
        mat1.printMatrix()
        print("Matrix B:")
        mat2.printMatrix()
        op2=input("Enter your Choice (A/B):")
        if op2=="A" or op2=="a":
            mat3 = mat1.transpose(r1, c1)
        elif op2=="B" or op2=="b":
            mat3 = mat2.transpose(r2, c2)
        else:
            print("Invalid Input!")
    elif op==5:
        i=0
    else:
        print("Invalid Input!")