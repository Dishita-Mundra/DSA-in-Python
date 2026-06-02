# n = 5
# i = 1
# while i<=n:
#     print(i,end=" ")
#     i+=1


# TIME COMPLEXITY(O(n))

# def printNumbers(i,n):
#     # base case
#     if i>n:
#         return
#     # recursive case
#     print(i,end=" ")
#     printNumbers(i+1,n)
# printNumbers(1,5)



# FACTORIAL (O(n))
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# print(fact(4))



# def fun(n):
#     if n==0:
#         return
#     print(n,end=" ")
#     fun(n-1)
# fun(3)                    # OUTPUT:3 2 1


# def fun(n):
#     if n==0:
#         return
#     fun(n-1)
#     print(n,end=" ")
# fun(3)


def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return a*b//gcd(a,b)

print(gcd(15,50))
print(lcm(15,50))