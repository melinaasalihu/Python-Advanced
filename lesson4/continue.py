scores = [32,45,67,98,23,14]
total = 0
count = 0

for score in scores:
    if score < 50:
        continue

    total += score
    count += 1

    print("the total is",total)
    print("the amount of scores",count)


