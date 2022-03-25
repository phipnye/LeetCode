"""
9.
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""

def isPalindrome(x: int) -> bool:

    #If x is negative or positive with a 0 in the ones place
    if x < 0 or (x > 0 and x%10 == 0):
        #Just return False
        return False

    #Declare an integer to hold the value of the reversed integer
    reverse = 0
    
    #While x exceeds the reversed value
    while x > reverse:
        #Multiply reverse by 10 and add the ones digit from x
        reverse = reverse * 10 + x % 10
        #Now shift x down by a factor of 10 (rounding down)
        x = x // 10

    #If reverse and x are equal or x is a rounded down factor of reverse and 10
    #Return True        
    return (x == reverse or x == reverse // 10)

Tests = [
{
    'input' : {
        'x' : 121
    },
    'output' : True
},
{
    'input' : {
        'x' : -121
    },
    'output' : False
},
{
    'input' : {
        'x' : 10
    },
    'output' : False
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

test_cases(isPalindrome, Tests)