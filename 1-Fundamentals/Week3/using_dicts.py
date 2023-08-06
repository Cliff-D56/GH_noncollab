states_capitals = {"Washington": "Olympia","Oregon": "Salem", "California": "Sacramento"}
print(len(states_capitals))
print(states_capitals["Washington"])
states_capitals["Washington"] = "Aberdeen"
states_capitals["Texas"] = "Austin"
print(states_capitals)
del states_capitals["California"]
print(states_capitals)
#Does not save variable
#states_capitals.pop("Oregon")
#Saves Variable
#removed_capital = states_capitals.pop("Oregon")
print(states_capitals)