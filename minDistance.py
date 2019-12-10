class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # word1 is larger than word2
        if len(word2) > len(word1):
            word2, word1 = word1, word2

        def recursive(word1, word2):
            if not word1 and not word2:
                return 0
            if not word1:
                return len(word2)
            if not word2:
                return len(word1)
            if word1[0] == word2[0]:
                return recursive(word1[1:], word2[1:])
            insert = 1 + recursive(word1, word2[1:])
            delete = 1 + recursive(word1[1:], word2)
            replace = 1 + recursive(word1[1:], word2[1:])
            return min(insert, delete, replace)
        return recursive(word1, word2)

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # word1 is larger than word2
        if len(word2) > len(word1):
            word2, word1 = word1, word2
        memo = [[-1 for j in range(len(word2))] for i in range(len(word1))]

        def recursive(word1, word2, i, j, memo):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2)-j
            if j == len(word2):
                return len(word1)-i
            if memo[i][j] == -1:
                if word1[i] == word2[j]:
                    ans = recursive(word1, word2, i+1, j+1, memo)
                else:
                    insert = 1 + recursive(word1, word2, i, j+1, memo)
                    delete = 1 + recursive(word1, word2, i+1, j, memo)
                    replace = 1 + recursive(word1, word2, i+1, j+1, memo)
                    ans = min(insert, delete, replace)
                memo[i][j] = ans
            return memo[i][j]
        return recursive(word1, word2, 0, 0, memo)


print(Solution().minDistance('horse', 'ros'))
# print(Solution().minDistance('intention', 'execution'))
