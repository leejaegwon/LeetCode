class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        # 합쳐서 -가 되는 시작을 하면 안됨.
        # 그전까지의 최신sum을 maxsum에 최신화
        #  -가 나오면 그다음 +일 경우 -보다 +가 크면 계쏙나가고 아니면 -를 멈춰야함.
        lastsum = 0
        maxsum = float('-inf')
        for num in nums:
            lastsum += num
            if lastsum > maxsum:
                maxsum = lastsum
            if lastsum < 0:
                lastsum = 0

        return maxsum
          
