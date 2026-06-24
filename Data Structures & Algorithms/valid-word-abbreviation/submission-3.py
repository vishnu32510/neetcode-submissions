class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word == abbr:
            return True
        i = 0
        j = 0
        m = len(abbr)
        n = len(word)

        while i < len(word) and j < len(abbr):
            if abbr[j] == "0":
                return False
            if word[i] == abbr[j]:
                i, j = i + 1, j + 1
            elif abbr[j].isalpha():
                return False
            else:
                subLen = 0
                while j < m and abbr[j].isdigit():
                    subLen = subLen * 10 + int(abbr[j])
                    j += 1
                i += subLen
        return i == n and j== m