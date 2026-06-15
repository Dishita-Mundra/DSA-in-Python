# Linear Time (O(n)) - individual also and add krke bhi

n=10
m=100
x=3

for i in range(n):
    if i==x:
        break
    print(i,end=" ")

for i in range(n/2):
    print(i,end=" ")

for i in range(n+100):
    print(i,end=" ")

for i in range(n*2):
    print(i,end=" ")

for i in range(n+m):
    print(i,end=" ")



# Contant Time (O(1)) - number of ope

for i in range(10):
    print(i,end=" ")



# Quadratic Time (O(n^2))

for i in range(n**2):
    print(i,end=" ")

#overall O(n^2+n) ~ O(n^2)
for i in range(n):
    for j in range(n):
        print(i,j)
for i in range(n):
    print(i,end=" ")



# Logarithmic Time (O(log n))

n = 100
while n>0:
    print(n,end=" ")
    n//=2


i=1
n=100
while i<=n:
    print(1,end=" ")
    i*=2



# Linearithemic Time (O(n log n))

i=1
n=100

for j in range(n):
    while i<=n:
        print(1,end=" ")
        i*=2



n= 100
m= 10
  
list1 = []

for i in range(n):
    list1.append(m)
