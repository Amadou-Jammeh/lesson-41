def sum(n1,n2):
    return n1+n2

def diff(n1,n2):
    return n1-n2

def product(n1,n2):
    return n1*n2

def quo(n1,n2):
    return n1/n2

num1=int(input("Enter first number"))
num2=int(input("Enter second number"))

print("sum of {} and {} is {}".format(num1,num2,sum(num1,num2)))
print("Difference of {} and {} is {}".format(num1,num2,diff(num1,num2)))
print("product of of {} and {} is {}".format(num1,num2,product(num1,num2)))
print("quotient of {} and {} is {}".format(num1,num2,quo(num1,num2)))




