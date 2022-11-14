x=int(input('enter the num'))
for i in range(x):
    a,b=map(int,input().split())
    if a>b:
        print('YES')
    else:
        print('No')