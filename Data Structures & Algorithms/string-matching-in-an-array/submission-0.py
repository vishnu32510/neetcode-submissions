class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[j] in words[i]:
                    res.add(words[j])
                    continue
        return list(res)