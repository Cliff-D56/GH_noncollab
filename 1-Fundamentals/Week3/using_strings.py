my_string = "alpha"
'''
multiline_string = """bravo
charlie"""
print(my_string)
print(multiline_string)
'''

print(my_string[0])
print(my_string[3])

print(my_string[0:3])
print(my_string[:2])
print(my_string[2:])
print(my_string)

for letters in my_string:
    print(letters)

print("pha" in my_string)
print("de" in my_string)
print("gh" not in my_string)