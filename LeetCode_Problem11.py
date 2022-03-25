"""
11.
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

def maxArea(height: list[int]) -> int:
    #Store the length of the heights list
    N = len(height)

    #Declare two pointers and a max area var to be returned
    i, j, max_area = 0, N-1, 0

    #While the left pointer is less than the right pointer
    while i < j:
        #Store the max value of the current area and the previous max area
        max_area = max(max_area, (j-i) * min([height[i],height[j]]))
        #If the height on the left exceeds that of the right
        if height[i] > height[j]:
            #Decrement the right pointer
            j -= 1
        #If the height on the right exceeds that of the left
        else:
            #Increment the left pointer
            i += 1
            
    return max_area

Tests = [
{
    'input' : {
    'height' : [1,8,6,2,5,4,8,3,7]
    },
    'output' : 49
},
{
    'input' : {
    'height' : [1,1]
    },
    'output' : 1
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

test_cases(maxArea, Tests)