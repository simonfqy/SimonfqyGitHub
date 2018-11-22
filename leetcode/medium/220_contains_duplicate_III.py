"""Link to the question: https://leetcode.com/problems/contains-duplicate-iii/
   This solution is from the discussion pages. It is an elegant solution which uses bucket sort. It utilizes the fact that
   with bucket size t, only the bucket corresponding to the current number or the neighboring buckets can contain the hitting
   number. No real sorting is required, just dictionary data type is used. It satisfies the index difference requirement, 
   in that it would delete the excess entries in the dictionary. It is a bit unconventional. My previous 
   implementation uses insertion sort, which is much longer and less elegant. 
   TAKEAWAY: bucket sort can be useful. We might need to customize it instead of stringently follow the original algorithm."""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int, the maximum difference between indices.
        :type t: int, the maximum difference between values.
        :rtype: bool
        """
        if t < 0:
            return False
        buckets = dict()
        for i, val in enumerate(nums):
            # The hitting one can only be the current bucket, or the neighboring bucket.
            bucket_num, offset = (int(val/t), 1) if t > 0 else (val, 0)
            for bucket_ind in range(bucket_num-offset, bucket_num + offset + 1):
                if bucket_ind in buckets and abs(buckets[bucket_ind] - val) <= t:
                    return True
            buckets[bucket_num] = val
            if len(buckets) > k:
                del buckets[int(nums[i-k]/t) if t > 0 else nums[i-k]]
        return False
