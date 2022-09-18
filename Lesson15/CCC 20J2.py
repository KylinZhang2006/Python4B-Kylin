"""https://dmoj.ca/problem/ccc20j2"""

P = int(input())
N = int(input())
R = int(input())

day = N
while day < P:
    day += (N * R * R)

print(day)













