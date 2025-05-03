class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        top = (0, tops.count(1), tops.count(2), tops.count(3), tops.count(4), tops.count(5),tops.count(6))
        bott = (0, bottoms.count(1), bottoms.count(2), bottoms.count(3), bottoms.count(4), bottoms.count(5), bottoms.count(6))
        
        ln = len(tops)

        # check if there is no condition 
        if not ((bott[1] + top[1] >= ln) or (bott[2] + top[2] >= ln) or (bott[3] + top[3] >= ln) or (bott[4] + top[4] >= ln) or (bott[5] + top[5] >= ln) or (bott[6] + top[6] >= ln)) :
            return -1
        
        # check if that all the values are same
        if (top[1] == ln) or (top[2] == ln) or (top[3] == ln) or (top[4] == ln) or (top[5] == ln) or (top[6] == ln) or (bott[1] == ln) or (bott[2] == ln) or (bott[3] == ln) or (bott[4] == ln) or (bott[5] == ln) or (bott[1] == ln) :
            return 0

        # check for every number (1,6) 
        rotates = []
        for i in range(1,7) :
            if not (bott[i] + top[i] >= ln) :
                continue
            
            two = [0,0]
            flag = True

            for j in range(ln):
                if tops[j] != i and bottoms[j] != i:
                    flag = False
                    break
                elif tops[j] != i:
                    two[0] += 1
                elif bottoms[j] != i:
                    two[1] += 1

            if flag:
                rotates.append(min(two))

        return min(rotates) if rotates else -1

        #     for j in range(ln):
        #         if tops[j] == i :
        #             continue
        #         if bottoms[j] == i :
        #             two[0] += 1
        #         else:
        #             flag = False
        #             break
        #     if not flag :
        #         return -1
        #     for j in range(0,ln):
        #         if bottoms[j] == i :
        #             continue
        #         if tops[j] == i :
        #             two[1] += 1
        #         else:
        #             flag = False
        #             break
        #     rotates.append(min(two))
        
        # return min(rotates)

