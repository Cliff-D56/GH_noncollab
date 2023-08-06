states_capitals = {"Washington": "Olympia","Oregon": "Salem", "California": "Sacramento"}
#Prints keys
for state in states_capitals:
    print(state)

#Prints literal values
for city in states_capitals.values():
    print(city)

#Allows to print both items (keys and values)
for state, city in states_capitals.items():
    print(city, "is the capital of",state)