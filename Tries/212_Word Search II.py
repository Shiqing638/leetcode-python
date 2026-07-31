class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] =TrieNode()
                node = node.children[ch]
            node.word = word

        m = len(board)
        n = len(board[0])
        res = []

        def dfs(i, j, node):
            if i >= m or j >= n or i < 0 or j < 0:
                return

            ch = board[i][j]

            if ch == "#" or ch not in node.children:
                return 

            node = node.children[ch]

            if node.word:
                res.append(node.word)
                node.word = None

            board[i][j] = "#"

            dfs(i+1, j, node)
            dfs(i-1, j, node)
            dfs(i, j+1, node)
            dfs(i, j-1, node)

            board[i][j] = ch

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return res



            