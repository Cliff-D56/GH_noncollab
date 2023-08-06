#This declares the function start
def reverse(str):
#This sets the new variable after intended tasks finishes
    reverse_name = name[::-1]
#This returns the finised task's value to function.
    return reverse_name

#This asks for input to function
name = input("What is your name? ")
#This puts input into the function
print("Your name reversed is:", reverse(name))

