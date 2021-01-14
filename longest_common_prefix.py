"""
Write a function to find the longest common prefix
string amongst an array of strings.  If there
is no common prefix, retun an empty ""
"""

def longestCommonPrefix(strs: list[str]) -> str:
    def prefixUtil(str1: list[str], str2: list[str]):
        result = ""
        i = j = 0

        while i <= len(str1) - 1 and j <= len(str2) - 1:
            if str1[i] != str2[j]:
                break
            result += str1[i]
            i += 1
            j += 1

        return result

    prefix = strs[0]

    for i in range(1, len(strs)):
        prefix = prefixUtil(prefix, strs[i])

    return prefix

print(longestCommonPrefix(["cat", "catch", "catdog"]))