class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = [0] * 26
        for char in s:
            count[ord(char)-ord("a")] += 1

        i = 25
        res = []
        while i >= 0:
            if count[i] == 0:
                i -= 1
                continue

            repeat = min(count[i], repeatLimit)
            res.append(chr(i+ord("a")) * repeat)
            count[i] = count[i] - repeat

            if count[i] > 0:
                j = i - 1
                while j >=0 and count[j] == 0:
                    j -= 1
                if j < 0:
                    break
                res.append(chr(j+ord("a")))
                count[j] -= 1
        return "".join(res)

