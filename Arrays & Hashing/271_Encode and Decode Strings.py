class Codec:
    def encode(self, strs: list[str]) -> str:
        res = []
        for s in strs:
            m = len(s)
            res.append(str(m))
            res.append("#")
            res.append(s)
        return "".join(res)   

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            index = int(s[i:j])
            word = s[j+1: (j+index+1)]
            res.append(word)
            i = j + index + 1
        return res
            


