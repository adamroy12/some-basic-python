def greeting(name):
    print('Hello', name) #variables defined within functions can only be used within that function - Local Scope.

input_name = input("What's your name?\n")    

greeting(input_name)

#print('Thanks', name) 
#Here, the variable name throws an error because it isn't defined outside the function.

#Variables written outside a local scope (in the main body of code) are global variables, and can be referenced from anywhere.
#Using global scope can get messy, local scope allows use to more easily use different functions with different values - we can pass it a value for name.
#rather than having to constantly redefine a name variable like this:
# def greeting():
#   print('Hello', name) < this 'name' references the global variable name below, rather than any value passed to the function. There is no value passed to the function.

# name = input("What's your name?\n")
# greeting(name)
# name2 = input("What's your name?\n")
# greeting(name2)
