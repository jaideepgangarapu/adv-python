def febser(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
for num in febser(10):
    print(num)
