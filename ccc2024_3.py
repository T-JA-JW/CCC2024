import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
sorted_set = sorted(set(arr))
val = sorted_set[-3]

print(val, arr.count(val))
