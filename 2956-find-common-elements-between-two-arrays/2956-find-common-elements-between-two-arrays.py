class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)

        answer1 = sum(1 for x in nums1 if x in s2)
        answer2 = sum(1 for x in nums2 if x in s1)

        return [answer1, answer2]
                
                    

                


        
        