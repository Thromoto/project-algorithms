def find_duplicate(nums):
    nums_ordenado = sorted(nums)
    n = len(nums_ordenado)

    if (len(nums) <= 1
            or any(type(num) == str for num in nums)
            or any(num < 0 for num in nums)):
        return False
    if len(nums) == 2 and nums[0] != nums[1]:
        return False

    for i in range(1, n):
        if nums_ordenado[i] == nums_ordenado[i - 1]:
            return nums_ordenado[i]


# nums = [1, 3, 4, 2, 2]
# nums = [1, 3, -4, 2, 2]
# numeros = find_duplicate(nums)
# print(numeros)
