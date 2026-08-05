class TimeMap:
    def __init__(self):
        self.key_TimeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_TimeMap[key][timestamp] = value

    def get(self, key: str, timestamp) -> str:
        if key not in self.key_TimeMap:
            return ""
        l = 0
        r = len(self.key_TimeMap[key])-1

        while l <= r:
            mid = (l + r) // 2
            if self.key_TimeMap[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return "" if right < 0 else self.key_TimeMap[key][right][1]

