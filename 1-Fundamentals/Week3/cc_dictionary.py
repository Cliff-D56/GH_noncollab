inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}
for inches in inches_snow.values():
    total_inches = sum(inches_snow.values())
print("Total snowfall in inches: ",total_inches)
Thursday = input("How many inches of snow fell on Thursday?")
inches_snow[Thursday] = int(Thursday)

def print_total_snowfall(inches_snow):
    total_inches = 0
    for inches in inches_snow.values():
        total_inches += inches
    print("Total snowfall in inches: ",total_inches)

print_total_snowfall(inches_snow)
