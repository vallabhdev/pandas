first = 0
second = 1
num = 10
print(first, second, end=" ")
for x in range(10):
    nex = first + second
    print(nex, end=" ")
    first = second
    second = nex
