class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        result = ""
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if i == j or j == k or k == i: continue
                    hh = str(A[i]) + str(A[j])
                    mm = str(A[k]) + str(A[6-i-j-k])
                    _time = hh + ":" + mm
                    if hh < "24" and mm < "60" and _time > result: result = _time
        return result