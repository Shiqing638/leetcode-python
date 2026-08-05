class Solution:
    def multiply(self, nums1: str, nums2: str) -> str:
        if nums1 == "0" or nums2 == "0":
            return "0"

        m = len(nums1)
        n = len(nums2)

        res = [0] * (m+n)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mu1 = int(nums1[i]) * int(nums2[j])

                ptr2 = j + i + 1
                ptr1 = j + i

                new = mu1 + res[ptr2]
                res[ptr2] = new % 10
                res[ptr1] += new // 10

        return "".join(map(str, res)).lstrip("0")

