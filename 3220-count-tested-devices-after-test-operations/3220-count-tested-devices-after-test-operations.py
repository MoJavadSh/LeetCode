class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        testedDev = 0
        for i in range(0,len(batteryPercentages)):
            if batteryPercentages[i] > 0 :
                testedDev += 1

                for j in range(i+1, len(batteryPercentages)):
                    if batteryPercentages[j] >= 1:
                        batteryPercentages[j] -= 1
        return testedDev


