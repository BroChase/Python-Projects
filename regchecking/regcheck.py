import re


date = "Friday, April 14th, 2017"
n = re.search('(?P<day>\d+)', date)
print(n.group('day'))
n = re.search('(?P<year>\d{4})', date)
print(n.group('year'))
n = re.search('(?P<month>( )\S+)', date)
m = str(n.group('month'))
m = m.strip()
print(m)

