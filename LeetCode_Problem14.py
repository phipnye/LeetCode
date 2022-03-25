"""
14.
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
def longestCommonPrefix(strs: list[str]) -> str:
    #Declare a string to be returned
    prefix = ''
    #Store the length of the shortest string
    len_smallest_str = len(min(strs, key=len))
    #Iterate through the strings until there's an inequality in the characters
    for i in range(len_smallest_str):
        #If the charracters match in each string
        if all([(strs[0][i] == strs[j][i]) for j in range(1, len(strs))]):
            #Add the common character to the answer string
            prefix += strs[0][i]
            #And continue to the next iteration of the string
            continue
        #Otherwise return the common prefix
        return prefix

    return prefix

Tests = [
{
    'input' : {
        'strs' : ["flower","flow","flight"]
    },
    'output' : 'fl'
},
{
    'input' : {
        'strs' : ["dog","racecar","car"]
    },
    'output' : ""
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

test_cases(longestCommonPrefix, Tests)