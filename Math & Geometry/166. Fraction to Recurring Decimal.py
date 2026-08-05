class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []

        if (numerator < 0) != (denominator < 0):
            res.append("-")

        dividend = abs(numerator)
        divisor = abs(denominator)

        frac = dividend // divisor
        res.append(str(frac))

        remainder = dividend % divisor
        if remainder == 0:
            return "".join(frac)

        res.append(".")
        lookup = {}

        while remainder != 0:
            if remainder in lookup:
                res.insert(lookup[remainder], "(")
                res.append(")")
                break

            lookup[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // divisor))
            remainder %= divisor
        return "".join(res)





