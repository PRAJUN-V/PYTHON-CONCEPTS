class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        a = []
        b = []
        def hello():
            c = list(set(nums))
            for i in c:
                nums.remove(i)
            return c


        while True:
            if nums != []:
                b.append(hello())
            else:
                break


        return b

s = Solution()
print(s.findMatrix(nums = [1,3,4,1,2,3,1]))
