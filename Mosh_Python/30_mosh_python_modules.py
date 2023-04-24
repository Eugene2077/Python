
# When Python hits the line import a module, it tries to find a package or a module by it's name. 
# (A package is a directory containing modules, but we will only consider modules for now). 
# Python has a simple algorithm for finding a module with a given name
# It looks for a file by it's name in the directories listed in the variable "sys.path".
# sys.path is just a Python list, like any other, 
# we can make the import work by appending the code directory to the list. 


import sys

print(type(sys.path))     # let see the type of "sys.path", you can see it is just a "list"

sys.path.append('/Users/eugeneshin/_Programming/Python/Mosh_Python/modules')   
# add the path(folder) of the mudule file you created, need not if the module is in the same folder(the folder in this python file is already in the list of "sys.path")

for path in sys.path:     # you can check what is in the "sys.path" list
    print(path)

from a_module import calc_tax, calc_shipping  # you added your directory to the "sys.path", so you can import it
# when import, using * does not recommended because if there is the same name of function or variable, it will overwrite it.

# another way of importing module
import a_module
cost = a_module.calc_shipping()
print(cost)

total = calc_tax(1000)
shipping_cost = calc_shipping()
print(total, shipping_cost)


# 상기 방법은 : https://bic-berkeley.github.io/psych-214-fall-2016/sys_path.html
# Mosh 가 설명하는 방식은 다음페이지에