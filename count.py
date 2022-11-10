n = 1743
rate = []
all = 0
for i in range(1743):
    r, p = input().split()
    r, p = float(r), float(p)
    if p > r:
        continue
    rate.append(p / r)
    all += p

print(rate)
print(sum(rate) / len(rate))
