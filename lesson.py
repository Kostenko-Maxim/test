cnt = 0
for x in range(10, 100):
    if (not(x % 2 == 0) and not(x % 5 == 0)) == True:
        cnt += 1
print(cnt)