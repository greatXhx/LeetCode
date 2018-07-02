nums = [2,7,11,15]
target = 9
out = []
for i, k in range(len(nums)):
    if nums[i] < target:
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                out.append()
                out.append()
                break
            elif nums[i] + nums[j] > target:
                break
print(out)