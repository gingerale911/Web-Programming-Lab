class Subsets:
    def get_subsets(self, nums):
        result = [[]]

        for num in nums:
            result += [subset + [num] for subset in result]

        return result


nums = list(map(int, input("Enter distinct integers: ").split()))

obj = Subsets()
subsets = obj.get_subsets(nums)

print(subsets)
