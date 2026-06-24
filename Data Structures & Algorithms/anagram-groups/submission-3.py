class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anags = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            anags[tuple(count)].append(s)
        return list(anags.values())

        # anags = defaultdict(list)

        # for s in strs:
        #     srted = "".join(sorted(s))
        #     anags[srted].append(s)

        # return list(anags.values())