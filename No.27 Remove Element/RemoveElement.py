class Solution(object):

    def removeElement(self, nums, val):
        """
        :param   nums:   List[int]
        :param   val:    int
        :return: int
        """
        length = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1
        return length


def main():
    app = Solution()
    nums = [3, 2, 2, 3]
    print(app.removeElement(nums, 3))
    print(nums)


if __name__ == '__main__':
    main()
