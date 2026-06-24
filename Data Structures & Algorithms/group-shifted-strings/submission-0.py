class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def getHash(string: str):
            key = []
            for a, b in zip(string, string[1:]):
                print(a,b)
                key.append(chr((ord(b) - ord(a))% 26  + ord('a')))
            return ''.join(key)
        group = defaultdict(list)
        for string in strings:
            hash_key = getHash(string)
            print(hash_key)
            group[hash_key].append(string)
        return list(group.values())