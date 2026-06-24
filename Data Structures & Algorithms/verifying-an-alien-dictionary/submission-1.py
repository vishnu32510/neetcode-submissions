class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {char: index for index, char in enumerate(order)}

        transformed_words = []
        for word in words:
            word_ranks = [order_map[char] for char in word]
            transformed_words.append(word_ranks)

        for i in range(len(transformed_words) - 1):
            if transformed_words[i] > transformed_words[i + 1]:
                return False
        return True