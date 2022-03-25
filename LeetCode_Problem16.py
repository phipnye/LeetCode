"""
16.
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
"""
def threeSumClosest(nums: list[int], target: int) -> int:
    #Sort the passed list
    nums.sort()
    #Store the length of the passed list
    N = len(nums)
    #Initialize the difference to the some abstractly large value
    #Note: This may have to change to sum(nums[0:3]) for other tests
    min_diff = 999
    #Allow i1 to iterate up to the third to last element
    #So i2 and i3 can point to last and second to last elements
    for i1 in range(N-2):
        #Other than for the first iteration
        #If i1 is now pointing to an element with the same value as the previous one
        #Skip this iteration and continue until it points to a new value
        if i1 > 0 and nums[i1] == nums[i1 - 1]:
            continue
        #Initialize i2 to one greater than i1
        #And initialize i3 to point to the last element in nums
        i2, i3 = i1+1, N-1
        #While the two pointers don't overlap
        while i2 < i3:
            #Caclulate the sum of the currently pointed to elements
            summ = nums[i1] + nums[i2] + nums[i3]
            #If the sum equals the target
            if summ == target:
                #return the sum
                return summ
            #If the sum exceeds the target
            elif summ > target:
                #Save the new min_diff sum if its closer to the target than previous min_diff sum
                if summ - target < abs(min_diff-target):
                    min_diff = summ
                #Decrement i3 to decrease the sum
                i3 -= 1
            #If the sum is exceeded by the target
            else:
                #Save the new min_diff sum if its closer to the target than previous min_diff sum
                if target - summ < abs(min_diff-target):
                    min_diff = summ
                #Increment i2 to increase the sum
                i2 += 1

    return min_diff

Tests = [
{
    'input' : {
        'nums' : [-1,2,1,-4],
        'target' : 1
    },
    'output' : 2
},
{
    'input' : {
        'nums' : [0,0,0],
        'target' : 1
    },
    'output' : 0
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

test_cases(threeSumClosest, Tests)