class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        l = []
        count = 0
        for i in word:
          if i not in l:
            l.append(i)
        for i in range(len(l)):
          if l[i].islower():
            if l[i].capitalize() in l[i+1:]:
              count+= 1

        return count

s = Solution()
a = s.numberOfSpecialChars("AbBCab")
print(a)
