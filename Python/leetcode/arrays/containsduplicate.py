nums =  [1, 2, 3, 1]
nums1 = [1, 2, 3, 4]
class solution(object):

    def containsduplicate(self, nums):
        hashset = set()                    #extra memonry  but O(n) time complexity 
        for i in nums:
            if i in hashset:
                return True 
            hashset.add(i) #revisit 
        return False

    def containsduplicatesort(self, nums):
        nums.sort()                          #o(nlogn) sorting
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False


sort = solution()
print(sort.containsduplicate(nums))
print(sort.containsduplicatesort(nums))
    

