def twoSum(nums, target):
        sol = []
        l = 1
        f = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > target :
                l = i - 1 
                break
        print(nums)
        print(l)
        if l == 1 :
            l +=1
        for i in range(int((l+1)/2)):
            if nums[f] + nums[l] == target:
                sol.append(f)
                sol.append(l)
                return sol
            f += 1
            l -= 1
        return []


nums = [2,7,11,15]
target = 9
print(twoSum(nums = [3, 2, 4], target = 6))