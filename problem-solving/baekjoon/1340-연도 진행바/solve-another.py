import sys

MONTH = 0
DAY = 1
YEAR = 2
HOUR = 3
MINUTE = 4

MONTHS = {"January": 1,
          "February": 2,
          "March": 3,
          "April": 4,
          "May": 5,
          "June": 6,
          "July": 7,
          "August": 8,
          "September": 9,
          "October": 10,
          "November": 11,
          "December": 12}
DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100)


today = list(sys.stdin.readline().strip().split())
today[MONTH] = MONTHS[today[MONTH]]
today[DAY] = int(today[DAY][:2])
today[YEAR] = int(today[YEAR])
today.append(int(today[HOUR][3:]))
today[HOUR] = int(today[HOUR][:2])


if is_leap_year(today[YEAR]):
    DAYS[1] = 29

total = sum(DAYS) * 24 * 60
current = (((sum(DAYS[:today[MONTH] - 1]) + today[DAY] - 1) * 24) + today[HOUR]) * 60 + today[MINUTE]

print(current / total * 100)
