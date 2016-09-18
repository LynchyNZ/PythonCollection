def anagramcheck(word1, word2):
    anagram = "false"
    if len(word1) == len(word2):
        for letter in word1:
            if letter not in word2:
                answer = "false"
                break
            else:
                anagram = "true"
                word2 = word2.replace(letter, '', 1)
    return anagram

print(anagramcheck("tset", "ttes"))
                
            