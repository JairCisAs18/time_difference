import datetime as dt

actual = dt.datetime.now()
#start_time = dt.datetime(year=actual.year, month=actual.month, day=actual.day, hour=7, minute=0, second=0)
# start_time = input('Ingresa la hora (en formato HH:MM:SS):')
# start_time = dt.datetime.strptime(start_time, '%H:%M:%S')
start = input('Ingresa la hora de inicio (de forma %H:%M:%S):')
#end = input('Ingresa la hora de fin:')
start_values = start.split(':')
#end_values = end.split(':')
start_hour = int(start_values[0])
start_min = int(start_values[1])
start_sec = int(start_values[2])
#end_hour = int(end_values[0])
#end_min = int(end_values[1])
#end_sec = int(end_values[2])
print(start_hour)
print(actual)
start_time = dt.datetime(year=actual.year, month=actual.month, day=actual.day, hour=start_hour,  minute=start_min, second=start_sec)
#end_time = dt.datetime(year=actual.year, month=actual.month, day=actual.day, hour=end_hour,  minute=end_min, second=end_sec)
#actual_time = dt.datetime(year=actual.year, month=actual.month, day=actual.day)
takt_time = 24.9
delta = actual - start_time
print(delta)
diff = round(delta.total_seconds())
print(diff)
target = round(diff / takt_time)
print(target)
