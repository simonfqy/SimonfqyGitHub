'''
Link: https://www.lintcode.com/problem/401/
'''

# My own solution, using heap and a set of visited coordinates. Has very good performance. Time complexity is O(klogn),
# where n is the maximum of the width and height of the matrix.
import heapq
class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        if not matrix or k < 1 or not matrix[0]:
            return None
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        counter = 0
        heap = [(matrix[0][0], 0, 0)]
        visited_coords = set([(0, 0)])
        while heap:
            val, row, col = heapq.heappop(heap)
            counter += 1            
            if counter == k:
                return val
            if row + 1 < num_rows and (row + 1, col) not in visited_coords:
                visited_coords.add((row + 1, col))
                heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))
            if col + 1 < num_cols and (row, col + 1) not in visited_coords:
                visited_coords.add((row, col + 1))
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))

        return None
    
    
# A solution from jiuzhang.com, I translated it from Java to Python. Uses binary search of values rather than indices, similar to
# https://github.com/simonfqy/SimonfqyGitHub/blob/379a222c43118293b8ed48cda1547296a3b2d756/lintcode/hard/65_median_of_two_sorted_arrays.py#L292.
# time complexity is O(nlog(range)), where n is the maximum of the width and height of the matrix, and range is the difference between
# max and min values in the matrix.
class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        if not matrix or not matrix[0] or k < 0:
            return None
        n_row, n_col = len(matrix), len(matrix[0])
        low, high = matrix[0][0], matrix[n_row - 1][n_col - 1]
        while low <= high:
            mid = (low + high) // 2
            # Note that smaller_count contains equal count.
            exists, smaller_count = self.find_num_order_in_matrix(matrix, mid)
            if exists and smaller_count == k:
                return mid
            elif smaller_count < k:
                # Note that it is not using mid directly, but mid + 1. Similarly for high, see below.
                low = mid + 1
            else:
                high = mid - 1
        # We have to use low, rather than high here. That's because when we exited the while loop without returning, it is
        # due to low value reassigned as mid + 1. So now low carries the right number we're seeking. Try to go through an
        # example where matrix is [[998,1002],[998,1003],[999,1003],[1000,1003],[1000,1004]], and k is 7, you'll see how it goes.
        return low
        
    # Returns the tuple of whether val exists, and the number of elements smaller than or equal to val in the matrix.
    def find_num_order_in_matrix(self, matrix, val):
        n_row, n_col = len(matrix), len(matrix[0])
        exists = False
        i, j = n_row - 1, 0
        smaller_count = 0
        while i >= 0 and j < n_col:
            if matrix[i][j] == val:
                exists = True
            if matrix[i][j] <= val:
                smaller_count += i + 1
                j += 1
            else:
                i -= 1

        return exists, smaller_count
    
    # This is a slightly modified kthSmallest() function. Here we're no longer returning low outside of the while loop. We determine whether
    # mid has that situation within the while loop and return it if we find it matches. Also passes all test cases.
    def kthSmallest2(self, matrix, k):
        if not matrix or not matrix[0] or k < 0:
            return None
        n_row, n_col = len(matrix), len(matrix[0])
        low, high = matrix[0][0], matrix[n_row - 1][n_col - 1]
        while low <= high:
            mid = (low + high) // 2
            exists, smaller_count = self.find_num_order_in_matrix(matrix, mid)
            if exists: 
                # The modification can be seen here.
                if smaller_count == k:
                    return mid
                if smaller_count > k:
                    _, smaller_for_smaller = self.find_num_order_in_matrix(matrix, mid - 1)
                    if smaller_for_smaller < k:
                        return mid
            if smaller_count < k:
                low = mid + 1
            else:
                high = mid - 1
                
               
    # Another variant of kthSmallest() function, following the solution of 
    # https://github.com/simonfqy/SimonfqyGitHub/blob/379a222c43118293b8ed48cda1547296a3b2d756/lintcode/hard/65_median_of_two_sorted_arrays.py#L292,
    # where the condition of the while statement changes to low + 1 < high, and assigning mid values to low and high, instead of mid + 1 or mid - 1.
    def kthSmallest3(self, matrix, k):
        if not matrix or not matrix[0] or k < 0:
            return None
        n_row, n_col = len(matrix), len(matrix[0])
        low, high = matrix[0][0], matrix[n_row - 1][n_col - 1]
        # The while condition is the classical low + 1 < high, not low <= high
        while low + 1 < high:
            mid = (low + high) // 2
            exists, smaller_count = self.find_num_order_in_matrix(matrix, mid)
            if exists and smaller_count == k:
                return mid
            elif smaller_count < k:
                # Note that it is using mid directly, not mid + 1. Similarly for high, see below.
                low = mid
            else:
                high = mid
        # We first decide whether low is the number we want. If not, then return high. It is similar to the solution (linked above) for question 65.
        # Without this determination, we'll return wrong result.
        _, smaller_count_for_low = self.find_num_order_in_matrix(matrix, low)
        if smaller_count_for_low >= k:
            return low
        return high    
    
