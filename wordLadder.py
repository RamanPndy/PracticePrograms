from collections import deque

def wordLadder(start, end, words):
    words.append(end)
    q = deque()
    q.append([start, 1])
    leng = len(start)
    while q:
        word, l = q.popleft()
        if word == end:
            return l
        for w in words:
            word_range=[w[i] != word[i] for i in range(leng)]
            if sum(word_range) == 1:
                words.remove(w)
                q.append([w, l+1])
    return 0

wordList = ["poon", "plee", "same", "poie", "plie", "poin", "plea"]
print (wordLadder("toon", "plea", wordList))