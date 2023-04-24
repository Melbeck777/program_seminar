H, A = map(int, input().split())
count = int(H/A) + (H%A != 0)
print(count)