import psutil

battery = psutil.sensors_battery()
percent = (battery.percent)

print(f'Процент заряда батареи {percent:.1f} %')