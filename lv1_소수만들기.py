from collections import defaultdict
def solution(nums):
    answer = 0
    check = defaultdict(bool)
    for i in range(2,3000):
        for j in range(i*2,3000,i):
            check[j] = True
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                if check[sum] == False:
                    answer += 1
    return answer