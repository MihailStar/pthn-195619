# 1
print(all("A" in word.upper() for word in input().split(" ")))


# 2
nums = [int(digit) for digit in input().split(" ")]

print(any(nums[i - 1] <= nums[i] for i in range(1, len(nums) - 1)))


# 3
print(any(word.upper().endswith("OUGHT") for word in input().split(" ")))
