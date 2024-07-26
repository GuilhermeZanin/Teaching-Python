from collections import deque

def ladder_length(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return None
    
    if beginWord == endWord:
        return 0
    
    queue = deque([(beginWord, 1)])
    
    while queue:
        current_word, current_depth = queue.popleft()
        
        for i in range(len(current_word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                new_word = current_word[:i] + char + current_word[i + 1:]
                
                if new_word == endWord:
                    return current_depth + 1
                
                if new_word in word_set:
                    queue.append((new_word, current_depth + 1))
                    word_set.remove(new_word)
    
    return None

# Example test cases
print(ladder_length('hit', 'cog', ["hit", "hot", "dot", "dog", "cog"]))