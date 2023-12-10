# TIME
day = 1
hour = 24
minute = 60
second = 60
conversion = 1000

# HEAVEN TIME
heaven_day = day
heaven_hour = heaven_day * hour
heaven_minute = heaven_hour * minute
heaven_second = heaven_minute * second

# HEAVEN RESULTS
print('Day in heaven: ' + '{:,}'.format(heaven_day))
print('Hours in heaven: ' + '{:,}'.format(heaven_hour))
print('Minutes in heaven: ' + '{:,}'.format(heaven_minute))
print('Seconds in heaven: ' + '{:,}'.format(heaven_second))

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
