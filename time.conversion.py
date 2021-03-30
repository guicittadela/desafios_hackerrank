s='07:05:45PM'
time = s.split(':')
print(time)
if s[-2:] == 'PM':
    if time[0] != 12:
        
        time[0] = str(int(time[0])+12)
        
    else:
        if time[0] == "12":
            time[0] == "00"
    newtime = ':'.join(time)
print(str(newtime[:-2]))
