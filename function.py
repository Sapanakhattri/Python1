# def sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# sum(2,3)
# sum(5,10)
# sum(15,10)

# #WAP to find average of three numbers using function
# def ave(a,b,c):
#     sum=a+b+c
#     ave=sum/3
#     print(ave)
#     return ave
# ave(2,3,3.5)

# def sum(a=1,b=2): #default value
#     sum=a+b
#     print(sum)
#     return sum
# sum()

#WAF to print the length of the list
# cities=["ktm","pokhara","butwal","biratnagar"]
# a=len(cities)
# print(a)

#using function
# cities=["ktm","pokhara","butwal","biratnagar"]
# def print_cities(city):
#     print(len(city))
# #     return cities
# print_cities(cities)

# print("hello",end=" ") #prints in same line
# print("sapana")

#WAF to find the factorial of n
# def fac(a):
#     i=1
#     p=1
#     while i<=a:
#         p=p*i
#         i=i+1
#     print(p)
# fac(8)
a=int(input("enter any number"))

def fac(a):
    i=1
    p=1
    while i<=a:
        p=p*i
        i=i+1
    print(p)
result =fac(a)
print(result)