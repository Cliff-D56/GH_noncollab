#numbers_set = {1, 2, 3, 4, 4} Duplicate values are deleted
#numbers_set = {1, 2, 3, 4, [5, 6]} Cannot use mutable data types like lists or dictionaries
numbers_set = {1, 2, 3, 4, (5, 6)}
#Tuples are not mutable
print(numbers_set)

words_set = {"Alpha", "Bravo", "Charlie"}
abcd = ""
for word in words_set:
    abcd += word
print(abcd)
if "Alpha" in words_set:
    print("Alpha in set")
else:
    print("My name is Pie Alpha is not in set ")

words_set.add("Delta")
print(words_set)
words_set.discard("Bravo")
print(words_set)

i = 0
while i < 10:
    i += 1
    mytuple1 = "1", "2", "3"
    print(mytuple1)
    mytuple1 = "2", "4", "6"
    print(mytuple1)