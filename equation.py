# TIME
day = 1
hour = 24
minute = 60
second = 60
conversion = 1000

# HEAVEN TIME
time_day = day
time_hour = time_day * hour
time_minute = time_hour * minute
time_second = time_minute * second

# HEAVEN RESULTS
print('Day: ' + '{:,}'.format(time_day))
print('Hours: ' + '{:,}'.format(time_hour))
print('Minutes: ' + '{:,}'.format(time_minute))
print('Seconds: ' + '{:,}'.format(time_second))

# EARTH TIME
earth_day = (day * 365) * conversion
earth_hour = (earth_day * hour) * conversion
earth_minute = (earth_hour * minute) * conversion
earth_second = (earth_minute * second) * conversion

# EARTH RESULTS
print('Days on earth: ' + '{:,}'.format(earth_day))
print('Hours on earth: ' + '{:,}'.format(earth_hour))
print('Minutes on earth: ' + '{:,}'.format(earth_minute))
print('Seconds on earth: ' + '{:,}'.format(earth_second))
