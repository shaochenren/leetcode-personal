from collections import deque
def word_ladder(self,start, end,dict):
    dict.add(end)
    queue = deque([start])
    vistied = set([start])

    distance = 0

    while queue:
        distance +=1
        size = len(queue)
        for i in range(size):
            word = queue.popleft()
            if word == end:
                return distance
            for next_word in self.get_next_word(word,dict):
                if next_word in vistied:
                    continue
            vistied.add(next_word)
            queue.append(next_word)
            
    return 0 

def get_next_word(self,word,dict):
    next_word = []
    for i in range(len(word)):
        left, right = word[:i], word[i+1:]
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if word[i] == char:
                continue
            new_word = left + char + right
            if new_word in dict:
                next_word.append(new_word)
    return next_word

start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
q = word_ladder(start, end,dict)

print(q)