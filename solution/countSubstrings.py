class Solution(object):
    # O(n^2)
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.count = 0
        if s is None or len(s) == 0:
            return 0

        def extendPalindrome(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                self.count += 1
                left -= 1
                right += 1
        
        for i in range(len(s)):
            extendPalindrome(s, i, i)
            extendPalindrome(s, i, i + 1)

        return self.count

    # O(n^2)
    def countSubstrings(self, S):
        def manachers(S):
            A = '@#' + '#'.join(S) + '#$'
            Z = [0] * len(A)
            center = right = 0
            for i in range(1, len(A) - 1):
                if i < right:
                    Z[i] = min(right - i, Z[2 * center - i])
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            return Z

        return sum((v+1)/2 for v in manachers(S))


print(Solution().countSubstrings("aba"))
