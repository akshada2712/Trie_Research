class TrieNode:
  def __init__(self):
    self.children = {}
    self.end = False

class Trie:

  def __init__(self):
    self.root = TrieNode()

  def insert(self, word: str):

    curr = self.root

    for i in word:
      if i not in curr.children:
        curr.children[i] = TrieNode()
      curr = curr.children[i]

    curr.end = True

  def search(self, word: str):
    curr = self.root
    for char in word:
      if char not in curr.children:
        return False
      curr = curr.children[char]
    return curr.end

  def startsWith(self, prefix: str):
    curr = self.root
    for char in prefix:
      if char not in curr.children:
        return False
      curr = curr.children[char]

    return True

