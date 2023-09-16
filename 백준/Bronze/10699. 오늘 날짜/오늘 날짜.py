from datetime import datetime
if datetime.today().month < 10: m = '0' + str(datetime.today().month)
else: m = str(datetime.today().month)
if datetime.today().day < 10: d = '0' + str(datetime.today().day)
else: d = str(datetime.today().day)
print(f'{datetime.today().year}-{m}-{d}')