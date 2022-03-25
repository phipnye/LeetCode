"""
4.
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    #sort the combined list of integers
    nums = sorted(nums1 + nums2)
    #store the length of the combined lists
    N = len(nums)

    #if the length is odd
    if N % 2:
        #return the middle element
        return nums[N//2]
    #if the length is even
    else:
        #return the average of the two "middle" elements
        med = (nums[N//2 - 1] + nums[N//2]) / 2
        return med

Tests = [
{
    'input' : {
        'nums1' : [1,3],
        'nums2' : [2]
    },
    'output' : 2.00000
},
{
    'input' : {
        'nums1' : [1,2],
        'nums2' : [3,4]
    },
    'output' : 2.50000
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

test_cases(findMedianSortedArrays, Tests)