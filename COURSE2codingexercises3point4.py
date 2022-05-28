import statistics

test = [89,90,91,90,85,91,88,80,77,81,76,85,87,88,83,95,88,82,85,84]

mean = statistics.mean(test)
mode = statistics.mode(test)
median = statistics.median(test)

print("Mean:",mean)
print("Mode:",mode)
print("Median:",median)
