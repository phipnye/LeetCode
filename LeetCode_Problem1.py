"""
1.
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    #create an empty dicitionary to store the values of nums mapped to their index
    mapped_vals = {}
    for i,n in enumerate(nums):
        #calculate the current difference between the target and the current list value
        difference = target - n
        #if the value was a previous value of the list
        if difference in mapped_vals:
            #return the indices of those values
            return [mapped_vals[difference], i]
        #otherwise, store the value as a key in the dict mapped to the index as its value
        #and continue iterating over the loop
        mapped_vals[n] = i

Tests = [
{
    'input' : {
        'nums' : [2,7,11,15],
        'target' : 9
    },
    'output' : [0,1]
},
{
    'input' : {
        'nums' : [3,2,4],
        'target' : 6
    },
    'output' : [1,2]
},
{
    'input' : {
        'nums' : [3,3],
        'target' : 6
    },
    'output' : [0,1]
}
]
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

test_cases(twoSum, Tests)