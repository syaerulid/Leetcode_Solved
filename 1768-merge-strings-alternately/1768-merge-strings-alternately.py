class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        list1 = list(word1)
        list2 = list(word2)
        n = len(list1)
        m = len(list2)
        
        list_baru = []
        
        if m >= n:
            for i in range(n):
                list_baru.extend([list1[i],list2[i]])
            list_baru.extend(list2[n:])
        else:
            for i in range(m):
                list_baru.extend([list1[i],list2[i]])
            list_baru.extend(list1[m:])
            
        return ''.join(list_baru)