class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def removeHelper(s, output, iStart, jStart, openParen, closedParen):
            numOpenParen, numClosedParen = 0, 0
            for i in range(iStart, len(s)):
                if s[i] == openParen:
                    numOpenParen += 1
                if s[i] == closedParen:
                    numClosedParen += 1
                # We have only ONE extra closed paren we need to remove
                if numClosedParen > numOpenParen:
                    print(s)
                    if openParen == '(':
                        print("positive")
                    elif openParen == ')':
                        print('negative')
                    print("i=", i, numOpenParen, numClosedParen)
                    # Try removing this ONE closed paren at each position, skipping duplicates
                    print(jStart, i)
                    # jStart: always to search the first closedParen which can be removed
                    for j in range(jStart, i+1):  # <=
                        # can be the first char,
                        # or the char which previous char isn't closedParen, removing each one of the consequtive closedParen actually is the same
                        if s[j] == closedParen and (j == jStart or s[j-1] != closedParen): # since when j == jStart, there isn't j-1
                            # Recursion: iStart = i since we now have valid # closed parenthesis thru i. jStart = j prevents duplicates
                            # at the next recursion, we only need to search the iStart from the current i, and search the jStart from the current j
                            # since we found the first invalid closedParen at the i, and we have removed a closedParen at j
                            print("remove, j=", j, s[j])
                            removeHelper(s[:j]+s[j+1:], output,
                                         i, j, openParen, closedParen)
                    return
            reversed = s[::-1]
            print(reversed, "now out of the loop")
            if openParen == '(':
                removeHelper(reversed, output, 0, 0, ')', '(')
            else:
                output.append(reversed)

        output = []
        removeHelper(s, output, 0, 0, '(', ')')
        return output


# print(Solution().removeInvalidParentheses('(((()())'))
# print(Solution().removeInvalidParentheses(')('))
# print(Solution().removeInvalidParentheses('(a)())()'))
# print(Solution().removeInvalidParentheses(')()('))
print(Solution().removeInvalidParentheses('x)('))
