class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        write = 0

        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j+=1

            chars[write] = chars[i]
            length = j - i
            write += 1
            for digit in str(length):
                chars[write] = digit
                write += 1

            i = j
        return write
