"""
Link to the problem: https://leetcode.com/problems/maximum-width-ramp/
Solution 1:
stack s contains the indices of the elements. The indices stored in s are increasing, while the elements corresponding to these indices 
are decreasing. It is guaranteed to include A[0], as well as the minimum of A.
In the second for loop, the indices are looped in decreasing order. Whenever an element corresponding to a s stack entry is no larger 
than A[j], it is popped and the differences in indices are calculated. Since j is the largest index with A[j] >= this element (hence 
j - s[-1] being the largest), popping it wouldn't cause any problems.

Q: What if some elements not included in s gives the maximum width ramp, and is the smaller element in the ramp?
A: It is impossible. Because an element not included in s will be larger than or equal to some elements in s, which appear earlier in A. 
Those smaller and earlier elements stored in s will give rise to a bigger width. On the other hand, it is certain that some elements not 
included in s is the larger element in max-width ramp.

Q: Why using a stack with decreasing element?
A: The stack s will only be popped if the last (smallest in A) element is no larger than A[j], which is guaranteed to be the max-width 
ramp (if it is a ramp at all, since j might be smaller than s[-1]) among the ramps with A[s[-1]] being the smaller element. Removing it 
would reduce the workload and not cause harm. The earlier an element is in s, the less likely that A[j] >= A[the element], so the stack 
must be popped from the tail to head.

Q: What is the key in this solution?
A: Constructing a stack and popping it gradually. Popping the stack guarantees that the second for loop has a Time Complexity of O(N), 
escaping the quadratic time complexity a brute-force algorithm will lead to.
Q: Overall, what is the intuition leading to this solution?
A: A max-width ramp should have its smaller element appear as "early" in A and as small as possible. All elements larger than A[0] are 
not possible to be the smaller element in the max-width ramp, hence they shouldn't be considered as the candidate smaller element; the 
same applies to arbitrary A'[0], where A' is a sublist A[i:] in which A[i] < A[0]; constructing a stack of candidate smaller elements in 
max-width ramp, which includes A[0] and all later and smaller elements, becomes natural. Otherwise, we must consider those uninteresting 
elements as candidate smaller element in max-width ramp and compare them, wasting a great deal of time.
"""

def maxWidthRamp(self, A):
        s = []
        res = 0
        for i, a in enumerate(A):
            if not s or A[s[-1]] > a:
                s.append(i)
        for j in range(len(A))[::-1]:
            while s and A[s[-1]] <= A[j]:
                res = max(res, j - s.pop())
        return res
