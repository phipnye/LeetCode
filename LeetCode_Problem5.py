"""
5.
Given a string s, return the longest palindromic substring in s.
"""
def longestPalindrome(S: str) -> str:
    S_prime = "|" + "|".join(S) + "|"
    # S' = S with a bogus character (eg. '|') inserted between each character (including outer boundaries)
    PalindromeRadii = [0] * len(S_prime)
    Palindromes = []
    # The radius of the longest palindrome centered on each place in S_prime
    # note: length(S_prime) = length(PalindromeRadii) = 2 × length(S) + 1

    Center = 0
    Radius = 0
    
    while Center < len(S_prime):
        # At the start of the loop, Radius is already set to a lower-bound for the longest radius.
        # In the first iteration, Radius is 0, but it can be higher.
        
        # Determine the longest palindrome starting at Center-Radius and going to Center+Radius
        while Center-(Radius+1) >= 0 and Center+(Radius+1) < len(S_prime) and S_prime[Center-(Radius+1)] == S_prime[Center+(Radius+1)]:
            Radius = Radius+1
    
        # Save the radius of the longest palindrome in the array
        PalindromeRadii[Center] = Radius
        Palindromes.append(S_prime[Center-Radius:Center+Radius])
        
        # Below, Center is incremented.
        # If any precomputed values can be reused, they are.
        # Also, Radius may be set to a value greater than 0
        
        OldCenter = Center
        OldRadius = Radius
        Center = Center+1
        # Radius' default value will be 0, if we reach the end of the following loop. 
        Radius = 0 
        while Center <= OldCenter + OldRadius:
            # Because Center lies inside the old palindrome and every character inside
            # a palindrome has a "mirrored" character reflected across its center, we
            # can use the data that was precomputed for the Center's mirrored point. 
            MirroredCenter = OldCenter - (Center - OldCenter)
            MaxMirroredRadius = OldCenter + OldRadius - Center
            if PalindromeRadii[MirroredCenter] < MaxMirroredRadius:
                PalindromeRadii[Center] = PalindromeRadii[MirroredCenter]
                Center = Center+1
            
            elif PalindromeRadii[MirroredCenter] > MaxMirroredRadius:
                PalindromeRadii[Center] = MaxMirroredRadius
                Center = Center+1
                
            else: # PalindromeRadii[MirroredCenter] = MaxMirroredRadius
                Radius = MaxMirroredRadius
                break  # exit while loop early
    
    longest_palindrome_in_S = max(Palindromes, key=len)[1::2]
    return longest_palindrome_in_S

Tests = [
{
    'input' : {
        'S' : "babad"
    },
    'output' : "bab"
},
{
    'input' : {
        'S' : "cbbd"
    },
    'output' : "bb"
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

test_cases(longestPalindrome, Tests)