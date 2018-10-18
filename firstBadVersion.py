class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        min = 1
        max = n
        while min<=max:
            mid = min+(max-min)//2
            if isBadVersion(mid):
                max = mid-1
            else:
                min = mid+1
        return min