def addition( a, b ):
    return a + b   #return keyword returns a value or a series of values from a function. The value of the function will be what it returns when called.

num1 = float(input('Enter your 1st number:\n'))
num2 = float(input('Enter your 2nd number:\n'))

result = addition(num1, num2)
print('The result is', result)

#We could move the main body of code itself to a function. This means it's possible to call functions from within other functions.

def main():
    num1 = float(input('Enter your 1st number:\n'))
    num2 = float(input('Enter your 2nd number:\n'))

    result = addition(num1, num2)
    print('The result is', result)

main()

#This code will run the same thing twice over, once as main code before the the function main() is defined, which contains the main code.
#Then main() is called, running the main code within it.