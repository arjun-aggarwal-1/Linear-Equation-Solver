import csv
import random as rnd

def main():
    head,mx,constants=input_()
    EquationPrint(head,mx,constants)
    determinant = det(mx)
    if(determinant==0):
        print('Given system has either infinite solutions or no solutions.')
    else:
        mx1=invert(mx,determinant)
        newm=multiply(mx1,constants)
        print('The solution is: ')
        for i in range(len(newm)):
            temp=round(newm[i],0)
            if(abs(temp-newm[i])<0.0000000001):
                newm[i]=temp
            print(head[i],':',round(newm[i],4))

def input_():
    var=int(input('Enter the number of variables to solve (Enter a number less than equal to 7): '))
    type_=input('Enter your method of file input (r for Random generation), (c for Console), (f for File): ')
    if(type_=='f'):
        return FileInput(var)
    elif(type_=='r'):
        return RandomGenerator(var)
    elif(type_=='c'):
        return ConsoleInput(var)
    else:
        print('Invalid Input! Run the program again.')

def submx(mx,r,c):
    x=[]
    for i in mx:
        x.append(i[:c]+i[c+1:])
    x.pop(r)
    return x

def det(mx):
    temp=len(mx)
    if(temp==1):
        return mx[0][0]
    d=0
    for j in range(temp):
        d+=det(submx(mx,0,j))*mx[0][j]*((-1)**j)
    return d

def adj(mx):
    temp=len(mx)
    l=[]
    for i in range(temp):
        x=[0]*temp
        for j in range(temp):
            x[j]=det(submx(mx,i,j))*((-1)**(i+j))
        l.append(x)
    y=[[l[j][i] for j in range(temp)] for i in range(temp)]
    return y

def invert(mx,d):
    m=adj(mx)
    for i in range(len(m)):
        for j in range(len(m)):
            m[i][j]/=d
    return m

def multiply(mx,altm):
    newm=[]
    for i in mx:
        sum_=0
        for j in range(len(i)):
            sum_+=i[j]*altm[j]
        newm.append(sum_)
    return newm

def FileInput(var):
    f=input('Enter file name (CSV file): ')
    with open(f,'r') as file:
        obj=csv.reader(file)
        obj=list(obj)
        # print(obj)
        # headings=obj[0]
        mx=[]
        constants=[]
        for i in range(len(obj)):
            mx.append([int(obj[i][j]) for j in range(len(obj))])
            constants.append(int(obj[i][-1]))
    return headings(var), mx, constants
    
def ConsoleInput(var):
    mx=[]
    constants=[]
    for i in range(var):
        temp=list(map(int,input(f'Enter row number {i+1} (less than 20) of variables (1 space character between them): ').split()))
        mx.append(temp)
        temp=int(input(f'Enter value of equation number {i+1}: '))
        constants.append(temp)
    return headings(var),mx,constants
    
def RandomGenerator(var):
    mx=[]
    for i in range(var):
        mx.append(list(rnd.sample(range(20), var)))
    constants=list(rnd.sample(range(1000), var))
    return headings(var),mx,constants

def EquationPrint(head,mx,constants):
    for i in range(len(mx)):
        for j in range(len(mx)):
            if(j==0):
                print(str(mx[i][j]),head[j],end='')
            else:
                print(' +',str(mx[i][j]),head[j],end='')
        print(' =',str(constants[i]))
    print()

def headings(var):
    temp=[0]*var
    for i in range(var):
        temp[i]='X'+str(i+1)
    return temp

main()
