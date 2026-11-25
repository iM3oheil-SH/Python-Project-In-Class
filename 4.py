Equipment = {
    ("Lab-A", "Sensor"): ["S1", "S2"],
    ("Lab-B", "Sensor"): ["S3"],
}

def Make_Report(Equipment):
    Report = {}
    
    for Key, Values in Equipment.items():
        Report[Key] = tuple(Values)
        
    return Report

#Report At 9
Report_9 = Make_Report(Equipment)

#Change
Equipment[("Lab-A", "Sensor")].append("S4")
Equipment[("Lab-B", "Sensor")] = ["S5"]

#Report At 10
Report_10 = Make_Report(Equipment)

print("Report 9 : ")
print(Report_9)

print("Report 10 : ")
print(Report_10)

print("Changes : ")

for Key in set(Report_9) | set(Report_10):
    
    Old = set(Report_9.get(Key, ()))
    New = set(Report_10.get(Key, ()))
    
    Added = New - Old
    Removed = Old - New
    
    print(Key)
    print("Added : ", Added)
    print("Removed : ", Removed)
    