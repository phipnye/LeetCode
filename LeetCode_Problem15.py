"""
15.
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
def threeSum(nums: list[int]):
    #Sort the passed list
    nums.sort()
    #Declare a list of triplets to be returned
    triplets = []
    #Store the length of the passed list
    N = len(nums)

    #Using three pointers, iterate through the passed list
    #i1 iterates up to N-2 so that i2 and i3 can point to the last elements of the list
    #Also, prevent i1 from pointing from a number greater than 0 since nums[i1] <= nums[i2] <= nums[i3]
    i1 = 0
    while i1 < N-2 and nums[i1] <= 0:
        #Other than for the first iteration
        #If i1 is pointing to the same value as the previous element's value
        #Increment i1 and try again
        #This prevents duplicate answers
        if i1 > 0 and nums[i1] == nums[i1 - 1]:
            i1 += 1
            continue
        #Initialize i2 to one greater than i1
        #Initialize i3 to point to the last element
        i2, i3 = i1+1, N-1
        #While the second and third pointer do not overlap
        while i2 < i3:
            #Store the sum of the currently pointed to elements
            sum = nums[i1] + nums[i2] + nums[i3]

            #If the some of pointed to values equals 0
            if sum == 0:
                #Add the elements as a tuple to the returned list
                triplets.append((nums[i1],nums[i2],nums[i3]))
                i3 -= 1
                #Then, decrement i3 until its no longer pointing to the same value
                while i3 > i2 and nums[i3+1] == nums[i3]:
                    i3 -= 1
                #And finally, increment i2
                i2 += 1
            #If the sum was greater than 0
            elif sum > 0:
                #Decrement i3
                i3 -= 1
            #If the sum was less than 0
            else:
                #Increment i2
                i2 += 1
        #Finally, increment i1 and repeat
        i1 += 1

    return triplets

Tests = [
{
    'input' : {
        'nums' : [-1,0,1,2,-1,-4]
    },
    'output' : [(-1,-1,2),(-1,0,1)]
},
{
    'input' : {
        'nums' : []
    },
    'output' : []
},
{
    'input' : {
        'nums' : [0]
    },
    'output' : []
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

test_cases(threeSum, Tests)