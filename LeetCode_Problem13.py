"""
13.
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""

def romanToInt(s: str) -> int:
    #Declare an integer to be returned as the answer
    Ans = 0
    #Initialize a dictionary that maps roman numeral strings to their int values
    roman_numerals = {
        'M' : 1000,
        'CM' : 900,
        'D' : 500,
        'CD' : 400,
        'C' : 100,
        'XC' : 90,
        'L' : 50,
        'XL' : 40,
        'X' : 10,
        'IX' : 9,
        'V' : 5,
        'IV' : 4,
        'I' : 1
    }
    N = len(s)
    #Declare a pointer
    i = 0
    #While the pointer remains in-bounds
    #Note the -1 prevents s[i+1] from pointing out-of-bounds
    while i < (N - 1):
        #If the current and next characters of the string are in the dictionary
        if s[i] + s[i+1] in roman_numerals:
            #Add their mapped value to the answer integer
            Ans += roman_numerals[s[i] + s[i+1]]
            #And increment i by 2
            i += 2
        else:
            #Otherwise, add the mapped value of the current character to the answer integer
            Ans += roman_numerals[s[i]]
            #And increment by 1
            i += 1

    #If i did not increment all the way to N because the previous addition was that of a single character
    if i < N:
        #Add the mapped value of s[i] to the answer before returning it
        Ans += roman_numerals[s[i]]
    return Ans

Tests = [
{
    'input' : {
        's' : "III"
    },
    'output' : 3
},
{
    'input' : {
        's' : "LVIII"
    },
    'output' : 58
},
{
    'input' : {
        'digits' : "MCMXCIV"
    },
    'output' : 1994
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

test_cases(romanToInt, Tests)