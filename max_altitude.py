class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        altitude = 0

        for i in range(len(gain)):
            altitude += gain[i]

            if altitude > max_alt:
                max_alt = altitude

        return max_alt