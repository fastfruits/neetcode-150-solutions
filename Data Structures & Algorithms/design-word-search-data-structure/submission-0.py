class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.isEnd
            
            c = word[index]
            if c == ".":
                for children in node.children.values():
                    if dfs(children, index + 1):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(node.children[c], index + 1)

        return dfs(self.root, 0)