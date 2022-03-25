"""
7.
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""
def reverse(x: int) -> int:
    #If x is 0
    if not x:
        #return 0
        return x

    #Hold the sign of x and store it
    sign = x // abs(x)
    #Take the absolute value of x
    x = abs(x)

    #Declare an integer to be returned
    result = 0

    #Declare an integer to hold the greatest power of ten <= x
    i = 1

    #Find the greatest power of ten <= x (i.e., if x = 102, i = 100)
    while i <= (x/10):
        i *= 10
    
    #while x is positive
    while x > 0:
        #take the current digit of x and multiply it by i so as to flip its order
        result += (x % 10) * i
        #Now drop the current digit by dividing x by 10 and rounding down
        x //= 10
        #And now decrement i back down
        i //= 10

    #Now, replace the sign of the initial value of x
    result *= sign

    #If the value for result goes outside the signed 32-bit integer range
    if -2**31 > result or result > 2**31+1:
        #just return 0
        return 0
    
    #Otherwise, return the value
    return result

Tests = [
{
    'input': {
        'x' : 123
    },
    'output' : 321
},
{
    'input': {
        'x' : -123
    },
    'output' : -321
},
{
    'input': {
        'x' : 120
    },
    'output' : 21
}]

def test_cases(function, tests):
    import time
    case_num = 0
    for test in tests:
        Input = test['input']
        Exp_Output = test['output']
        
        start = time.time()
        Act_Output = function(*Input.values())
        end = time.time()
        
        execution_time = end - start

        print(f"TEST NUMBER {case_num}:\n")
        print(f"Input:\n{Input}\n")
        print(f"Expected Output:\n{Exp_Output}\n")
        print(f"Actual Output:\n{Act_Output}\n")
        if Exp_Output == Act_Output:
            print(f"PASSED in {execution_time}\n")
        else:
            print(f"FAILED in {execution_time}\n")
        case_num += 1

test_cases(reverse, Tests)