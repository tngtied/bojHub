def solution(nums):
    hashmap = {}
    answer =0
    for i in range(len(nums)):
        if (nums[i] not in hashmap):
            hashmap[nums[i]] = True
            answer += 1
    return min(answer, len(nums)//2)