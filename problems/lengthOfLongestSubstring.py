# O(kn)
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    map_ = {}
    max_ = 0
    for idx, c in enumerate(s):
        if c in map_:
            i = map_[c]
            map_ = {s[j]: j for j in range(i + 1, idx + 1)}
        else:
            map_[c] = idx
        max_ = max(max_, len(map_))

    return max_


# O(n)
# slide window
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    i = 0
    map_ = {}
    max_ = 0
    for idx, c in enumerate(s):
        if c in map_:
            # can only find key which is larger than i
            i = max(map_[c], i)
        map_[c] = idx + 1
        max_ = max(max_, idx - i + 1)

    return max_


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("s"))
print(lengthOfLongestSubstring(""))
print(lengthOfLongestSubstring("au"))
print(lengthOfLongestSubstring("abba"))