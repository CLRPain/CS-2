num = input()
date = int(num[:1])
num = int(num[2:])
week = ''
weeks = []
for x in range(date-1):
    week += '    '
print('Sun Mon Tue Wed Thr Fri Sat')
for day in range(num):
    if len(week) > 27:
        weeks.append(week)
        week = ''
    if day < 9:
        week += f'  {day+1} '
    else:
        week += f' {day+1} '
weeks.append(week)
for week in weeks:
    week = week[:len(week)-1]
    print(week)