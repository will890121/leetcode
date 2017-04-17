class Solution(object):
    def lengthOfLongestSubstring(self, s):
        s_len = len(s)
        if s_len == 0:
            return 0
        start = 0
        maxLen = 1
        for end in range(1, s_len):
            if s[end] in s[start:end]:
                start += s[start:end].index(s[end]) + 1
            else:
                curLen = (end - start + 1)
                maxLen = curLen if curLen > maxLen else maxLen
                if maxLen < (end - start + 1):
                    maxLen = end - start + 1
        return maxLen


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abab'), 2)
    print(Solution().lengthOfLongestSubstring('abacd'), 4)
    print(Solution().lengthOfLongestSubstring('abcabcbb'), 3)
    print(Solution().lengthOfLongestSubstring("pwwkew"), 3)
