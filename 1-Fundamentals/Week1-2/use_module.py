#This imports entire module
import my_module
#This imports only sections of module that is specified
from my_module import greet, flavor 

my_module.greet("Albert Einstein")
print("My favorite ice cream flavor is", my_module.flavor)
