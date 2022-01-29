from collections import defaultdict

class Trie:
  def __init__(self, char):
    self.value = char
    self.children = defaultdict()
  
  def getValue(self):
    return self.value

  def get_children(self):
    return self.children

  def hasChild(self, char):
    if char in self.children.keys():
      return True
    else:
      return False
    
  def insertChild(self, other_trie):
    self.children[other_trie.getValue()] = other_trie

def isPresent(starter, example):
  for character in example:
    #resulting = isPresent(starter, character)
    if not character in starter.get_children().keys():
      return False
    else:
      noder = starter.get_children()[character]
      starter = noder
  return True

def make_small_tries(list_of_words):
  starter = Trie(" ")
  mega_string = list(set("".join(list_of_words)))
  #First step: Make a trie for all of the chars in our dictionary
  for i in mega_string:
    starter.insertChild(Trie(i))
  return starter

#Second Step: Iterate through our original dictionary
def build_big_trie(starter, list_of_words):
  for word in list_of_words:
    for i in range(len(word)-1):
      holder = starter.get_children()[word[i]]
      if holder.hasChild(word[i]):
        continue
      else:
        holder.insertChild(starter.get_children()[word[i + 1]])
  return starter

#At this point, we should have theoretically have built the trie

#Now the extra challenge: What if someone wants to add words to the dictionary?
def add_char(starter, word):
  container = set(word)
  current_chars = set(starter.get_children().keys())
  actual = container.difference(current_chars)
  if len(actual) == 0:
    return False
  else:
    for i in actual:
      starter.insertChild(Trie(i))
  print(starter.get_children().keys())

def add_branch(starter, word):
  for i in range(len(word)-1):
    trie_ = starter.get_children()[word[i]]
    trie_.insertChild(starter.get_children()[word[i+1]])
  return

