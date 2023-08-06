my_tuple = (1, 2, 3, 4 ,5)
print(my_tuple[-1] + my_tuple[-2])
#my_tuple[3] = 1, will not work due to tuples being immutable
my_tuple = (5, 4, 3, 2, 1)
#This assignment will not change the first tuple, just change the variable my_tuple so it will print the new 
# variable but the old tuple is not changed
print(my_tuple)