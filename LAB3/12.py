def function(histogram):
    for i in histogram:
        print("*" * i)

n = int(input("How many?\n"))
histogram = []
for i in range(n):
    m = int(input())
    histogram.append(m)

function(histogram)