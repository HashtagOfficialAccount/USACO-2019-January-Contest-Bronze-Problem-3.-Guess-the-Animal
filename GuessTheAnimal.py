import sys
sys.stdin = open("guess.in","r")
sys.stdout = open("guess.out","w")
l = []
N = int(input())
for i in range(N):
    x = [r for r in input().split()]
    l.append(x[1:])
maximum = 0
for i in range(N):
    for y in range(i+1,N):
        counter = 0
        for z in l[i][1:]:
            if z in l[y]:
                counter += 1
        if counter > maximum:
            maximum = counter
print(str(maximum+1))
