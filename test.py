from trie import Trie, build_big_trie, isPresent, make_small_tries

#Example 1: In this example, we are building a trie structure for just one word
word = 'car'
container = list(word)
tries = []
for i in range(len(container)-1):
  holder = Trie(container[i])
  holder.insertChild(Trie(container[i + 1]))
  tries.append(holder)

#Example 2: In this example, we are building a node for each character that is present in the dictionary
dictionary = ["car", "card", "cards", "cot", "cots", "trie", "tried", "tries", "try"]
root = make_small_tries(dictionary)

#Example 3: Finally, we are building the trie data structure based on the words in the dictionary
beginner = build_big_trie(root, dictionary)

#Here we test that our trie is able to recognize the words in our dictionary
print("-----------Testinng the Trie---------------------")
for word in dictionary:
    print("Is", word, "present?", isPresent(root, word))
print("-------------------------------------------------")

#In the following lines, we test what happens when new words are tested against our trie
print("-----------Testinng the Trie against unseen words---------------------")

bad_words = ["cars", "candy", "cott", "triez"]
for words in bad_words:
    print("Is", words, "present?", isPresent(root, words))
print("----------------------------------------------------------------------")

print("-----------Adding unknown word to the trie----------------------------")
#In the following, we will add a word that isn't found in the dictionary
example = "maker"
print(add_char(root, example))
add_branch(root, example)

if isPresent(root, example):
    print(example, "has been added to the trie")
else:
    print("Something went wrong")

print("----------------------------------------------------------------------")
