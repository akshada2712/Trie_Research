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

import random
import string

def generate_random_words(lengths, num_words):
    words = []
    for _ in range(num_words):
        length = random.choice(lengths)
        word = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        words.append(word)
    return words

# List of lengths for random words
lengths = [5, 7, 10, 13, 14, 15]

# Number of random words to generate
num_words = 1000000

# Generate random words
random_words = generate_random_words(lengths, num_words)
print(random_words)


## Creating trie 

research_trie = Trie()
for i in random_words:
    research_trie.insert(i)

## testing with trie data structure 

import time
ranges = [10000, 100000, 250000, 500000, 750000, 1000000]
for j in ranges:
  words_subset = random.choices(random_words, k = j)
  prefix_match = [word[0:5] for word in random.choices(random_words, k = j // 100) if len(word) > 5]


  ans = []

  start = time.time()
  for i in words_subset:
    ans.append(research_trie.search(i))
  end = time.time()
  print(f"Time taken for word search of {len(words_subset)} words using trie: " , end - start)



  pref_ans = []
  start = time.time()
  for i in prefix_match:
    pref_ans.append(research_trie.startsWith(i))
  end = time.time()
  print(f"Time taken for prefix-word search of {len(prefix_match)} words using trie: " , end - start)
  print()


## testing using python modules 

for j in ranges:
  words_subset = random.choices(random_words, k = j)
  prefix_match = [word[0:5] for word in random.choices(random_words, k = j // 100) if len(word) > 5]

  ans_py = []
  start = time.time()
  for word in words_subset:
    if word in random_words:
      ans_py.append(True)
    else:
      ans_py.append(False)
  end = time.time()
  print(f"Time taken for word search of {len(words_subset)} words using python modules: " , end - start)

  pref_ans = []
  start = time.time()
  for word in prefix_match:
    for word_parent in random_words:
      if word.startswith(word_parent):
        pref_ans.append(True)

    pref_ans.append(False)
  end = time.time()
  print(f"Time taken for prefix-word search of {len(prefix_match)} words using python modules: " , end - start)
