from collections import Counter, defaultdict

States = (
('TN', 'Chennai'),
('AP', 'Guntur'),
('TN', 'Madurai'),
('KL', 'Cochin'),
('AP', 'Chithoor'),
('TN', 'Coimbatore'),
)
citylist = defaultdict(list)

for statename, cityname in States:
    citylist[statename].append(cityname)

print(citylist)

citycount= Counter(statename for statename, no in States)
print("Count Citywise : " ,citycount)