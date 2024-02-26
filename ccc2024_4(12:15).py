import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

def replace(x, rep):
    new = []
    for i in range(len(x)):
        if x[i] == 1:
            pass

if len(a) == len(b):
    for i in range(len(a)):
        if a[i] != b[i]:
            print(a[i], b[i])
            break
    print('-')

else:
    candidates = list(set(a) - set(b))
    # print(candidates)
    for i in range(len(candidates)):
        if a.count(candidates[i]) == len(a) - len(b):
            quiet = candidates[i]
            break

    silly = list(set(candidates) - set(quiet))[0]
    # print(silly)

    i = 1
    while i < len(b):
        if a[-i] == silly and b[-i] != silly:
            replaced = b[-i]
            break
        i += 1

    print(silly, replaced)
    print(quiet)
