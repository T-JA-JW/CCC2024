import sys

n = int(input())

while 1:
    try:
        a = int(input())
        if n > a:
            n += a
        else:
            break
    except:
        break

print(n)
