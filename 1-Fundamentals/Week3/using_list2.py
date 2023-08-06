states = ["Washington", "Texas", "Ohio"]
'''
for state in states:
    state = state.lower()
    print(state)

print("Washington" in states)
print("Tennessee" in states)
print("Washington" not in states)
'''

states2 = ["Arizona", "Kansas", "Nebraska"]
best_states = states + states2
print(best_states)
#Index 1 to 3 not including 3
print(best_states[1:3])
#Index 2 and back
print(best_states[:2])
#Index 4 onward
print(best_states[4:])
#Index 1 and slices off the last 2 
print(best_states[1:-2])
#Index 1 and onward but slices off last 1
print(best_states[1:-1])
#Index from the 1st last index and slices off at 3 index
print(best_states[-5:3])
#Index at start from the 4th last index and onward
print(best_states[-4:])