def operations(a,b,c):
    if x ==1 :
        return a+b
    elif x ==2 :
        return a-b
    elif x==3:
        return a*b
    elif x==4:
        return a/b
    else:
        return "invalid"


a = int(input("enter a number"))
b = int(input("enter a secound number"))
x = int(input("enter what operation you want to do?  \n addition enter : 1 \n substraction enter : 2 \n multiplication enter : 3\n division enter : 4\n "))

print(operations(a,b,x))