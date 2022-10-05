H, M = map(int, input().split())

miniute = 60 * H + M
alarm = miniute - 45

if alarm < 0:
    alarmHour = 23
else:
    alarmHour = int(alarm / 60)
    
alarmMiniute = alarm % 60

print(alarmHour, alarmMiniute)