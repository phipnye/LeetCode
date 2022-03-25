"""
2.
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional

#Definition for singly-linked list.
class ListNode:
    #Constructor
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    #Equality operator
    def __eq__(self, __o: object) -> bool:
        #while there is another node at self.next and the values of the objects equal
        while self.next and self.val == __o.val:
            #Continue
            self = self.next
            __o = __o.next

        #if the lengths of the compared objects do not match
        if (__o.next and not self.next) or (self.next and not __o.next):
            #Return False
            return False

        #Return whether the current values match
        return self.val == __o.val

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummyhead = ListNode()
    result = dummyhead
    carry = 0
    val = 0
    #While val is not None for l1 or l2
    while l1 or l2:
        #Initialize the sum of vals to 0
        sum = 0
        #if l1.val is not None
        if l1:
            #add its value to the sum
            sum += l1.val
            #Continue to the next ListNode in l1
            l1 = l1.next
        #if l2.val is not None
        if l2:
            #add its value to the sum
            sum += l2.val
            #Continue to the next ListNode in l2
            l2 = l2.next
        
        #carry the previous digit if the previous sum was > 10
        sum += carry

        #carry the tens digit of the current sum to the next sum
        carry = sum // 10

        #Drop the tens digits of the current sum
        val = sum % 10

        #Assign the adjusted sum to the next ListNode
        result.next = ListNode(val)

        #And continue to the next ListNode
        result = result.next
    
    #If the previous sum was > 10
    if carry > 0:
        #Add another ListNode to the list with the carried value
        result.next = ListNode(carry)
    
    return dummyhead.next

Tests = [
{
    'input' : {
        'l1' : ListNode(2, ListNode(4, ListNode(3))),
        'l2' : ListNode(5, ListNode(6, ListNode(4)))
    },
    'output' : ListNode(7, ListNode(0, ListNode(8)))
},
{
    'input' : {
        'l1' : ListNode(0),
        'l2' : ListNode(0)
    },
    'output' : ListNode(0)
},
{
    'input' : {
        'l1' : ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
        'l2' : ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    },
    'output' : ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))))))
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
        if Exp_Output == Act_Output:
            print(f"PASSED in {execution_time}\n")
        else:
            print(f"FAILED in {execution_time}\n")
        case_num += 1

test_cases(addTwoNumbers, Tests)