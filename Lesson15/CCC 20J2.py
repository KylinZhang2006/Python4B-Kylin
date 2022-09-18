"""https://dmoj.ca/problem/ccc20j2"""

P = int(input())  # total number
N = int(input())  # people affected on the Day 0
R = int(input())  # the number of people can be infected by 1 person

day = 0
infected_previous_day = N
infected = infected_previous_day
while infected <= P:
    day += 1
    infected += infected_previous_day * R
    infected_previous_day = infected_previous_day * R

print(day)













