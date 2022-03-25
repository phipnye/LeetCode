"""
8.

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

1) Read in and ignore any leading whitespace.
2) Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
3) Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
4) Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
5) If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
6) Return the integer as the final result.
"""

def myAtoi(s: str) -> int:
    #Remove any leading whitespace
    s = s.lstrip()
    #If s is now empty, return 0
    if not s:
        return 0
    
    #Declare a string to be returned
    result = ''

    #Store the new length of the string
    N = len(s)

    #Declare and initialize an iterator
    i = 0
    #If the first element of the string is a positive sign
    if s[0] == '+':
        #Just increment i and move on
        i += 1
    #If the first element of the string is a negative sign
    elif s[0] == '-':
        #Add the negative sign as the first element of the string
        result += '-'
        #And then increment i
        i += 1
    
    #While i is less than the length of the string and the current char is a number
    while i != N and s[i].isdigit():
        #append the current char to the result string
        result += s[i]
        #and increment i
        i += 1
    
    #if the result string is empty or only contains the negative sign
    if not result or result == '-':
        #just return 0
        return 0
    
    #cast the result to an integer
    result = int(result)

    #If the integer is out of the 32-bit signed integer range
    #Then clamp the integer so that it remains in the range.
    if result < -2 ** 31:
        return -2 ** 31
    elif result > 2 ** 31 - 1:
        return 2 ** 31 - 1
    
    return result

Tests = [
{
    'input': {
    's' : "42"
    },
    'output' : 42
},
{
    'input': {
    's' : "   -42"
    },
    'output' : -42
},
{
    'input': {
    's' : "4193 with words"
    },
    'output' : 4193
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

test_cases(myAtoi, Tests)