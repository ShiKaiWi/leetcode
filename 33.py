class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.helperSearch(nums, target, 0, len(nums)-1)

    def helperSearch(self, nums, target, s, t):
        if s>t:
            return -1
        elif s==t:
            return -1 if target != nums[s] else s

        l = t - s 
        m = s + l // 2
        sn = nums[s]
        tn = nums[t]
        mn = nums[m]
        if target == sn:
            return s
        elif target == tn:
            return t
        elif target == mn:
            return m

        if mn > tn:
            if target > sn and target < mn:
                return self.helperSearch(nums, target, s+1, m-1)
            elif target > mn:
                return self.helperSearch(nums, target, m+1, t-1)
            elif target < sn and target > tn:
                return -1
            elif target <= tn:
                return self.helperSearch(nums, target, m+1, t-1)
        else:
            if target < mn:
                return self.helperSearch(nums, target, s, m-1)
            elif target > mn and target < tn:
                return self.helperSearch(nums, target, m+1, t-1)
            elif target > tn and target < sn:
                return -1
            elif target > sn:
                return self.helperSearch(nums, target, s+1, m-1) 

nums = [1,3,9,12,-1, 0]
if __name__ == '__main__':
    s = Solution()
    print s.search(nums,-1) 
