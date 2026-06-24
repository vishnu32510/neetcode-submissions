class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        for i in range(len(arr) - 1, -1 ,-1):
            if greatest == -1:
                greatest = arr[i]
                arr[i] = -1
            else:
                temp = greatest
                if greatest < arr[i]:
                    greatest = arr[i]
                arr[i] = temp
        return arr