##################       Recursion in python    ############

####### Recursion is simply can describe as if a func is calling itself 
# ##### within its body

import sys
print(sys.getrecursionlimit()) ### this will tell us by default recursion limit in python i.e__ 1000
sys.setrecursionlimit(20)
def greet():
    print("Hello World")
    greet()    ######## So this is basically recursion

greet() 