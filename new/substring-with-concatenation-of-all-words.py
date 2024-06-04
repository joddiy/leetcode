import pprint

from tools import *


class Solution(object):
    @print_
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        wordLength = len(words[0])
        substrLength = wordLength * len(words)
        expectedWordCounts = collections.Counter(words)
        # print('expectedWordCounts ', expectedWordCounts)
        result = []

        # Trying each way to split `s`
        # into consecutive words of length `substrLength`
        for offset in range(wordLength):
            wordCounts = {word: 0 for word in expectedWordCounts.keys()}
            # print('wordCounts ', wordCounts)
            # print('type of jawn', type(wordCounts))
            # Start with counting words in the first substring
            for i in range(offset, substrLength + offset, wordLength):
                word = s[i: i + wordLength]
                if word in wordCounts:
                    wordCounts[word] += 1

            if wordCounts == expectedWordCounts:
                result.append(offset)

            # Then iterate the other substrings
            # by adding a word at the end and removing the first word
            for start in range(
                    offset + wordLength,
                    len(s) - substrLength + 1,
                    wordLength,
            ):
                removedWord = s[start - wordLength: start]
                addedWord = s[
                            start + substrLength - wordLength:
                            start + substrLength
                            ]
                if removedWord in wordCounts:
                    wordCounts[removedWord] -= 1
                if addedWord in wordCounts:
                    wordCounts[addedWord] += 1

                if wordCounts == expectedWordCounts:
                    result.append(start)

        return result


solution = Solution().findSubstring

solution(s="barfoothefoobarman", words=["foo", "bar"])
solution(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"])
solution(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"])
