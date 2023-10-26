sleep_time = int(input())
alarm_time = int(input())

if alarm_time > sleep_time:
    sleep_length = alarm_time - sleep_time
else:
    sleep_length = (24 - sleep_time) + alarm_time

print(sleep_length)