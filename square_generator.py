def square(n):
    for s in range(1, n+1):
        yield s*s
        
squ = square(6)
for square in squ:
    print(square)