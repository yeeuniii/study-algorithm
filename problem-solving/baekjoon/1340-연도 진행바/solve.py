import sys
import datetime

MONTH = 0
DAY = 1
YEAR = 2
HOUR = 3
MINUTE = 4

months = {"January": 1,
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

today = list(sys.stdin.readline().strip().split())
today[MONTH] = months[today[MONTH]]
today[DAY] = int(today[DAY][:2])
today[YEAR] = int(today[YEAR])
today.append(int(today[HOUR][3:]))
today[HOUR] = int(today[HOUR][:2])

current = datetime.datetime(today[YEAR], today[MONTH], today[DAY], today[HOUR], today[MINUTE])
start = datetime.datetime(today[YEAR], 1, 1)
end = datetime.datetime(today[YEAR] + 1, 1, 1)

print((current - start).total_seconds() / (end - start).total_seconds() * 100)
