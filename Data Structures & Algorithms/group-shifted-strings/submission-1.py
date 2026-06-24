class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def getHash(string: str):
            key = []
            for a, b in zip(string, string[1:]):
                key.append(chr((ord(b) - ord(a))% 26  + ord('a')))
            return ''.join(key)
        group = defaultdict(list)

        for string in strings:
            hash_key = getHash(string)
            group[hash_key].append(string)
            
        return list(group.values())