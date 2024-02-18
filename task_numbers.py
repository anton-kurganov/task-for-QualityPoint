
x = (0, 0)
while True:
    num = int(input())
    if num == 0:
        print(x[0])
        break
    numsum = sum(map(int, (' '.join(str(num)).split())))
    if numsum > x[1]:
        x = (num, numsum)
