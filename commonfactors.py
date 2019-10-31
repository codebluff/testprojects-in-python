inpt = input().split()
x = int(inpt[0])
y = int(inpt[1])

count = 0
for i in range(1,  x ):
    for j in range(1,  y ):
        if i == j:
            if x % i == 0:
                if y % i == 0:
                    count += 1
print(str(count))
