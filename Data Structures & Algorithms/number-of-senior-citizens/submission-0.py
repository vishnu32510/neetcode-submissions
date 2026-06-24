class Solution:
    def countSeniors(self, details: List[str]) -> int:
        above_sixty = 0

        for det in details:
            if int(det[11:13]) > 60:
                above_sixty += 1
            
        return above_sixty