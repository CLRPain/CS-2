import os

stat = os.stat('ghost.jpg')
stat.st_mode
print(stat.st_type)