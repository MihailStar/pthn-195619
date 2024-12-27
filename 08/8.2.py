# 1
from_10_to_20 = iter(range(10, 20 + 1))

print(next(from_10_to_20))
print(next(from_10_to_20))
print(next(from_10_to_20))

for num in from_10_to_20:
    print(num)


# 2
words = [
    "feel",
    "graduate",
    "movie",
    "fashionable",
    "bacon",
    "drop",
    "produce",
    "acquisition",
    "cheap",
    "strength",
    "master",
    "perception",
    "noise",
    "strange",
    "am",
]

lens = (len(word) for word in words)

for i in lens:
    print(i)


# 3
from itertools import cycle

days_of_week = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

days = (
    pair for pair in zip(range(1, 77 + 1), cycle(days_of_week[5:] + days_of_week[:5]))
)

for day in days:
    print(day)
