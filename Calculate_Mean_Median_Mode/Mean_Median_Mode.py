# Calculate Mean, Median & Mode using Python

# Mean
# ****
# It is the average value of all the values in a dataset.

list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
mean = sum(list1) / len(list1)
print(f"Mean: {mean}")  # 20.2
print('\n')

# Median
# ******
# It is the middle value among all values in sorted order.
# 1st we need to arrange the values in sorted order.
# 2 ways to calculate Median
# if total no. of values is even: Median  = [(n/2)th term + {(n/2)+1}th]/2
# if total no.of values is odd: Median = {(n+1)/2}th term

list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list1.sort()

if len(list1) % 2 == 0:
    m1 = list1[len(list1) // 2]
    m2 = list1[len(list1) // 2 - 1]
    median = (m1 + m2) / 2
else:
    median = list1[len(list1) // 2]

print(list1)
print(f"Median: {median}")  # 20.0

# Mode
# ****
# Mode is the most frequently occurring value among all the values.
# from collections import  Counter

list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}

for i in list1:
    frequency.setdefault(i, 0)
    frequency[i] += 1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
        print('\n')
        print(f"Mode: {mode}")  # 20
