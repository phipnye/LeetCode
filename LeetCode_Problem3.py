"""
3. 
Given a string s, find the length of the longest substring without repeating characters.
"""

def lengthOfLongestSubstring(s: str) -> int:
    N = len(s)
    max_len, j, i = 0, 0, 0
    curr = ''

    #for indices of the list less than the length of the string
    while j < N:
        #if the current character isn't in the currently "highlighted" string
        if s[j] not in curr:
            #append the current character to the "highlighted" string
            curr += s[j]
            #and slide the right pointer to the right
            j += 1
            #store the length of the currently "highlighted" substring if its length is the
            #longest thus far
            max_len = max(max_len, len(curr))
        #if the current character is in the currently "highlighted" string
        else:
            #calculate the maximum length of substrings thus far and store it
            max_len = max(max_len, len(curr))
            #move the left pointer to the left
            i += 1
            #and adjust the "highlighted" string
            curr = s[i:j]
    return max_len

Tests = [
{
    'input' : {
        's' : "abcabcbb"
    },
    'output' : 3
},
{
    'input' : {
        's' : "bbbbb"
    },
    'output' : 1
},
{
    'input' : {
        's' : "pwwkew"
    },
    'output' : 3
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

test_cases(lengthOfLongestSubstring, Tests)