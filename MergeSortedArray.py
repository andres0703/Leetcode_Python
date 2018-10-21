def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        else:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1


if __name__ == '__main__':
    a = [1, 2, 3, 7, 10, 15, 0, 0]
    b = [9, 16]
    merge(a, 6, b, 2)
    print(a)