"""
6.
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""
def convert(s: str, numRows: int) -> str:
    #store the length of the string
    N = len(s)
    #if the string is one letter or the length exceeds the number of rows
    if numRows == 1 or N <= numRows:
        #just return the string
        return s
    #declare a list to hold other lists, it'll appear as if its a matrix with nonuniform row lengths
    word_matrix = []
    
    #add 'numRows' lists to the matrix which will represent rows
    for i in range(numRows):
        word_matrix.append([])

    #there will be N-numRows number of 'whole' columns
    #and there elements differ by a factor of 2*numRows-2
    for i in range(0, N-numRows, 2*numRows-2):
        #Go down the whole columns and add their respective elements
        for  j in range(numRows):
            word_matrix[j].append(s[i+j])

        #Initialize k to 1
        k = 1
        #Now go back through the elements that are between the 'whole' columns
        #and add the respective elements
        while k < (numRows - 1) and (i+j+numRows-1-k) < N:
            word_matrix[k].append(s[i+j+numRows-1-k])
            k += 1

    #For the last column, if the first element is a factor of the jumps
    #Move down the column in a vertical fashion and append their respective elements
    if (i+j+k) % (2*numRows-2):
        m = numRows - 2
        for l in range(i+j+k, N):
            word_matrix[m].append(s[l])
            m -= 1 
    #Otherwise, move in a diagonal fashion as we did for in between the 'whole' columns
    else:
        m = 0
        for l in range(i+j+k, N):
            word_matrix[m].append(s[l])
            m += 1
    
    #declare a string to be returned
    result = ""

    #iterate through the rows of the matrix and concatentate their elements into a single string
    for rows in word_matrix:
        result += ''.join(rows)
    return result

Tests = [
{
    'input' : {
        's' : "PAYPALISHIRING",
        'numRows' : 3
    },
    'output' : "PAHNAPLSIIGYIR"
},
{
    'input' : {
        's' : "PAYPALISHIRING",
        'numRows' : 4
    },
    'output' : "PINALSIGYAHRPI"
},
{
    'input' : {
        's' : "A",
        'numRows' : 1
    },
    'output' : "A"
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

test_cases(convert, Tests)