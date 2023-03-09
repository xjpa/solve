# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        have a hashset to store ints
        loop through
        check if current integer is already in hashset
            if yes, return contains duplicate
            if no, add it to hashset
        '''
        store = set()
        for i in nums:
            if i in store:
                return True
            else:
                store.add(i)
        return False