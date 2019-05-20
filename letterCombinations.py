class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) ==0:
            return []
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        ret = []
        def recursion(combinatin, next_digits):
            if len(next_digits) == 0:
                ret.append(combinatin)
                return
            for char in phone[next_digits[0]]:
                recursion(combinatin + char, next_digits[1:])
        recursion("", digits)
        return ret

Solution().letterCombinations("23")
        