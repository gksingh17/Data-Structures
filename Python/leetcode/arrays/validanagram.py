class Solution(object):
    def isAnagram(self, s, t):
        #first check if the length of the string is equal or not. 
        if len(s) != len(t):
            return False
            #create two dicts to keep a count check of each character, character : character count 
        CountS, CountT = {}, {}
        #since both are of equal length we can iterate over any string 
        for i in range(len(s)):
            #counting each character apperance, if the character doesnt exist in the list yet it will put 0 via get method
            CountS[s[i]] = 1 + CountS.get(s[i],0)
            CountT[t[i]] = 1 + CountT.get(t[i],0)
        return CountS == CountT

s = "anagram"
t = "nagaram"
anagram = Solution()
print(anagram.isAnagram(s,t))