class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = [0] * 26
        windowCount = [0] * 26

        for i in range (len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            windowCount[ord(s2[i]) - ord("a")] += 1
        
        if s1Count == windowCount:
            return True
        
        l = 0
        
        for r in range(len(s1), len(s2)):
            windowCount[ord(s2[r]) - ord("a")] += 1
            windowCount[ord(s2[l]) - ord("a")] -= 1
            l += 1

            if s1Count == windowCount:
                return True

        return False
