class TwoSum:
    def find_pair(self, numbers, target):
        index_map = {}

        for i, num in enumerate(numbers):
            diff = target - num
            if diff in index_map:
                return index_map[diff], i
            index_map[num] = i

        return None


numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target sum: "))

obj = TwoSum()
result = obj.find_pair(numbers, target)

if result:
    print(result[0], result[1])
else:
    print("No pair found")
